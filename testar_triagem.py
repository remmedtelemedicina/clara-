#!/usr/bin/env python3
"""
Simulador de triagem REMMED
Testa queixas de pacientes contra o prompt de triagem.

Uso:
  python testar_triagem.py                    # modo interativo
  python testar_triagem.py "dor abdominal"    # teste único
  python testar_triagem.py --lista            # testa lista predefinida
"""

import sys
import os
import anthropic

PROMPT_FILE = os.path.join(os.path.dirname(__file__), "triagem_prompt_corrigido.txt")

# Contexto simulado: paciente já passou pela leveza e está em TRIAGEM_ALARME
CONTEXTO_SIMULADO = """
Telefone: 5511999999999
Setor atual: TRIAGEM_ALARME
AGORA: Monday, 19/05/2026, 10:00

---
CONTEXTO DA CONVERSA:
- opcao = "1" (consulta clínica geral)
- Paciente confirmou sintomas leves (SIM na leveza)
- Agora está informando o sintoma principal

O agente deve processar o MOMENTO 1 da ETAPA 3B:
aplicar VERIFICAÇÃO 0 e identificar o grupo de sintoma.

IMPORTANTE: Simule as ferramentas internamente.
- Se chamar atualizar_setor, registre o setor mas não execute nada real.
- Se a mensagem deve ser ROTEAR, diga apenas ROTEAR.
- Se deve bloquear, mostre a mensagem de bloqueio.
- Se deve mostrar checklist, mostre o checklist do grupo.
"""

LISTA_TESTES = [
    # Digestivo
    "dor abdominal",
    "dor de barriga",
    "dor na barriga",
    "cólica",
    "diarreia",
    "náusea e vômito",
    "refluxo",
    # Neurológico
    "dor de cabeça",
    "dor de cabeça forte",
    "enxaqueca",
    "muita dor de cabeça e enjôo",
    "tontura",
    # Respiratório
    "tosse",
    "dor de garganta",
    "falta de ar",
    # Alarmes que devem bloquear
    "barriga rígida",
    "vômito com sangue",
    "febre há 3 dias",
    "dor no peito",
    "convulsão",
    "boca torta",
    # Outros grupos
    "ardência ao urinar",
    "dor nas costas",
    "olho vermelho",
    "coceira na pele",
    "dor de ouvido",
    "afta",
    "insônia",
    "ansiedade",
    "cansaço",
    "corrimento vaginal",
    "furúnculo com febre",
    "torção no pé",
]


def carregar_prompt():
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        return f.read()


def testar_queixa(client, prompt_triagem, queixa):
    system = CONTEXTO_SIMULADO + "\n\n---\n\n# PROMPT DA TRIAGEM\n\n" + prompt_triagem

    tools = [
        {
            "name": "atualizar_setor",
            "description": "Atualiza o setor do paciente",
            "input_schema": {
                "type": "object",
                "properties": {"setor": {"type": "string"}},
                "required": ["setor"],
            },
        },
        {
            "name": "supabase_save_triagem",
            "description": "Salva peso e altura",
            "input_schema": {
                "type": "object",
                "properties": {
                    "peso_kg": {"type": "number"},
                    "altura_cm": {"type": "number"},
                },
                "required": ["peso_kg", "altura_cm"],
            },
        },
        {
            "name": "faq_remmed",
            "description": "Responde dúvidas frequentes",
            "input_schema": {
                "type": "object",
                "properties": {"tema": {"type": "string"}},
                "required": ["tema"],
            },
        },
    ]

    messages = [{"role": "user", "content": queixa}]

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=system,
        tools=tools,
        messages=messages,
    )

    # Extrair resultado
    setor_atualizado = None
    texto_output = []

    for block in response.content:
        if block.type == "tool_use":
            if block.name == "atualizar_setor":
                setor_atualizado = block.input.get("setor", "?")
        elif block.type == "text":
            texto_output.append(block.text.strip())

    texto = " | ".join(texto_output) if texto_output else ""

    # Classificar resultado
    if setor_atualizado in ("ENCERRADO", "HUMANO"):
        if "SAMU" in texto or "pronto-atendimento" in texto or "emergência" in texto:
            resultado = "🚫 BLOQUEIA"
        else:
            resultado = "⛔ ENCERRA"
    elif setor_atualizado in ("TRIAGEM_MENTAL_AGENDA", "TRIAGEM_PESO_AGENDA", "TRIAGEM_SONO_AGENDA"):
        resultado = "↗️  REDIRECIONA"
    elif setor_atualizado == "TRIAGEM_ALARME" or texto:
        if "checklist" in texto.lower() or "sinais de alarme" in texto or "NÃO" in texto:
            resultado = "✅ PASSA (checklist)"
        elif texto == "ROTEAR":
            resultado = "✅ PASSA (rotear)"
        else:
            resultado = "✅ PASSA"
    elif texto == "ROTEAR":
        resultado = "✅ PASSA (rotear)"
    else:
        resultado = "❓ INDEFINIDO"

    return resultado, setor_atualizado, texto[:120] if texto else "(sem texto)"


def modo_lista(client, prompt_triagem):
    print("\n" + "=" * 70)
    print("SIMULAÇÃO DE TRIAGEM REMMED — LISTA COMPLETA")
    print("=" * 70)
    print(f"{'#':<3} {'Queixa':<35} {'Resultado':<22} {'Setor'}")
    print("-" * 70)

    for i, queixa in enumerate(LISTA_TESTES, 1):
        try:
            resultado, setor, _ = testar_queixa(client, prompt_triagem, queixa)
            setor_str = setor or "-"
            print(f"{i:<3} {queixa:<35} {resultado:<22} {setor_str}")
        except Exception as e:
            print(f"{i:<3} {queixa:<35} ❌ ERRO: {e}")

    print("=" * 70)


def modo_interativo(client, prompt_triagem):
    print("\n" + "=" * 50)
    print("SIMULADOR DE TRIAGEM REMMED")
    print("Digite a queixa do paciente. 'sair' para encerrar.")
    print("=" * 50)

    while True:
        queixa = input("\nQueixa do paciente: ").strip()
        if queixa.lower() in ("sair", "exit", "q"):
            break
        if not queixa:
            continue

        print("Testando...", end=" ", flush=True)
        try:
            resultado, setor, texto = testar_queixa(client, prompt_triagem, queixa)
            print(f"\n{resultado}")
            print(f"Setor → {setor or 'não alterado'}")
            print(f"Resposta: {texto}")
        except Exception as e:
            print(f"\n❌ Erro: {e}")


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ ANTHROPIC_API_KEY não encontrada.")
        print("   Configure: export ANTHROPIC_API_KEY=sua_chave")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    prompt_triagem = carregar_prompt()

    if len(sys.argv) > 1:
        if sys.argv[1] == "--lista":
            modo_lista(client, prompt_triagem)
        else:
            queixa = " ".join(sys.argv[1:])
            print(f"Testando: '{queixa}'")
            resultado, setor, texto = testar_queixa(client, prompt_triagem, queixa)
            print(f"Resultado: {resultado}")
            print(f"Setor: {setor or 'não alterado'}")
            print(f"Resposta: {texto}")
    else:
        modo_interativo(client, prompt_triagem)


if __name__ == "__main__":
    main()
