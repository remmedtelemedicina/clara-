#!/usr/bin/env python3
"""
Simulador de triagem REMMED — usa API do OpenAI (GPT)
Testa queixas de pacientes contra o prompt de triagem.

Uso:
  python testar_triagem.py                    # modo interativo
  python testar_triagem.py "dor abdominal"    # teste único
  python testar_triagem.py --lista            # testa lista predefinida
"""

import sys
import os
import json
from openai import OpenAI

PROMPT_FILE = os.path.join(os.path.dirname(__file__), "triagem_prompt_corrigido.txt")

CONTEXTO_SIMULADO = """
Telefone: 5511999999999
Setor atual: TRIAGEM_ALARME
AGORA: Monday, 19/05/2026, 10:00

CONTEXTO DA CONVERSA:
- opcao = "1" (consulta clínica geral)
- Paciente confirmou sintomas leves
- Agora informa o sintoma principal

Execute o MOMENTO 1 da ETAPA 3B:
aplique VERIFICAÇÃO 0 e identifique o grupo de sintoma.

INSTRUÇÕES PARA SIMULAÇÃO:
- Quando chamar atualizar_setor, registre o setor internamente.
- Se deve bloquear (VERIFICAÇÃO 0 ativada): chame atualizar_setor com "ENCERRADO" e mostre a mensagem de bloqueio.
- Se deve mostrar checklist: chame atualizar_setor com "TRIAGEM_ALARME" e mostre o texto exato do grupo.
- Se deve ROTEAR: chame atualizar_setor com o setor correto e output = "ROTEAR".
"""

LISTA_TESTES = [
    "dor abdominal",
    "dor de barriga",
    "dor na barriga",
    "cólica",
    "diarreia",
    "náusea e vômito",
    "refluxo",
    "dor de cabeça",
    "dor de cabeça forte",
    "enxaqueca",
    "muita dor de cabeça e enjôo",
    "tontura",
    "tosse",
    "dor de garganta",
    "falta de ar",
    "barriga rígida",
    "vômito com sangue",
    "febre há 3 dias",
    "dor no peito",
    "convulsão",
    "boca torta",
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

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "atualizar_setor",
            "description": "Atualiza o setor do paciente no workflow",
            "parameters": {
                "type": "object",
                "properties": {
                    "setor": {
                        "type": "string",
                        "description": "O próximo setor do paciente",
                    }
                },
                "required": ["setor"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "supabase_save_triagem",
            "description": "Salva peso e altura do paciente",
            "parameters": {
                "type": "object",
                "properties": {
                    "peso_kg": {"type": "number"},
                    "altura_cm": {"type": "number"},
                },
                "required": ["peso_kg", "altura_cm"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "faq_remmed",
            "description": "Responde dúvidas frequentes",
            "parameters": {
                "type": "object",
                "properties": {"tema": {"type": "string"}},
                "required": ["tema"],
            },
        },
    },
]


def carregar_prompt():
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        return f.read()


def testar_queixa(client, prompt_triagem, queixa, modelo="gpt-4o"):
    system = CONTEXTO_SIMULADO + "\n\n---\n\n" + prompt_triagem

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": queixa},
    ]

    response = client.chat.completions.create(
        model=modelo,
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
        max_tokens=1024,
        temperature=0,
    )

    msg = response.choices[0].message
    setor_atualizado = None
    texto_output = ""

    # Processar tool calls
    if msg.tool_calls:
        for tc in msg.tool_calls:
            if tc.function.name == "atualizar_setor":
                args = json.loads(tc.function.arguments)
                setor_atualizado = args.get("setor", "?")

    # Texto da resposta
    if msg.content:
        texto_output = msg.content.strip()

    # Classificar resultado
    if setor_atualizado == "ENCERRADO":
        if any(x in texto_output for x in ["SAMU", "pronto-atendimento", "emergência", "192"]):
            resultado = "🚫 BLOQUEIA"
        elif "ouvido" in texto_output.lower() or "otoscópio" in texto_output.lower():
            resultado = "⛔ ENCERRA (ouvido)"
        elif any(x in texto_output for x in ["gestante", "gravidez", "menor de 5"]):
            resultado = "⛔ ENCERRA (regra especial)"
        else:
            resultado = "⛔ ENCERRA"
    elif setor_atualizado in ("TRIAGEM_MENTAL_AGENDA",):
        resultado = "↗️  REDIRECIONA (Saúde Mental)"
    elif setor_atualizado in ("TRIAGEM_PESO_AGENDA",):
        resultado = "↗️  REDIRECIONA (Peso)"
    elif setor_atualizado in ("TRIAGEM_SONO_AGENDA",):
        resultado = "↗️  REDIRECIONA (Sono)"
    elif setor_atualizado == "AGENDANDO_CONFIRMACAO_TIPO" or texto_output == "ROTEAR":
        resultado = "✅ PASSA → ROTEAR"
    elif setor_atualizado == "TRIAGEM_ALARME" or "sinais de alarme" in texto_output:
        resultado = "✅ PASSA (checklist)"
    elif texto_output == "ROTEAR":
        resultado = "✅ PASSA → ROTEAR"
    else:
        resultado = "❓ VERIFICAR"

    return resultado, setor_atualizado, texto_output[:150] if texto_output else "(sem texto)"


def modo_lista(client, prompt_triagem, modelo):
    print("\n" + "=" * 72)
    print(f"SIMULAÇÃO REMMED — LISTA ({modelo})")
    print("=" * 72)
    print(f"{'#':<3} {'Queixa':<35} {'Resultado':<28} {'Setor'}")
    print("-" * 72)

    passou = bloqueia = encerra = redireciona = indefinido = 0

    for i, queixa in enumerate(LISTA_TESTES, 1):
        try:
            resultado, setor, _ = testar_queixa(client, prompt_triagem, queixa, modelo)
            setor_str = setor or "-"
            print(f"{i:<3} {queixa:<35} {resultado:<28} {setor_str}")
            if "PASSA" in resultado:
                passou += 1
            elif "BLOQUEIA" in resultado:
                bloqueia += 1
            elif "ENCERRA" in resultado:
                encerra += 1
            elif "REDIRECIONA" in resultado:
                redireciona += 1
            else:
                indefinido += 1
        except Exception as e:
            print(f"{i:<3} {queixa:<35} ❌ ERRO: {str(e)[:40]}")
            indefinido += 1

    print("=" * 72)
    print(f"✅ Passa: {passou}  🚫 Bloqueia: {bloqueia}  ⛔ Encerra: {encerra}  ↗️ Redireciona: {redireciona}  ❓ Indefinido: {indefinido}")
    print("=" * 72)


def modo_interativo(client, prompt_triagem, modelo):
    print("\n" + "=" * 55)
    print(f"SIMULADOR DE TRIAGEM REMMED ({modelo})")
    print("Digite a queixa do paciente. 'sair' para encerrar.")
    print("=" * 55)

    while True:
        queixa = input("\nQueixa: ").strip()
        if queixa.lower() in ("sair", "exit", "q"):
            break
        if not queixa:
            continue

        print("Testando...", end=" ", flush=True)
        try:
            resultado, setor, texto = testar_queixa(client, prompt_triagem, queixa, modelo)
            print(f"\n{resultado}")
            print(f"Setor → {setor or 'não alterado'}")
            if texto and texto != "ROTEAR":
                print(f"Resposta:\n{texto[:400]}")
        except Exception as e:
            print(f"\n❌ Erro: {e}")


def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("❌ OPENAI_API_KEY não encontrada.")
        print("   Configure: export OPENAI_API_KEY=sua_chave")
        sys.exit(1)

    modelo = os.environ.get("OPENAI_MODEL", "gpt-4o")
    client = OpenAI(api_key=api_key)
    prompt_triagem = carregar_prompt()

    if len(sys.argv) > 1:
        if sys.argv[1] == "--lista":
            modo_lista(client, prompt_triagem, modelo)
        else:
            queixa = " ".join(sys.argv[1:])
            print(f"Testando: '{queixa}' com {modelo}")
            resultado, setor, texto = testar_queixa(client, prompt_triagem, queixa, modelo)
            print(f"Resultado: {resultado}")
            print(f"Setor: {setor or 'não alterado'}")
            if texto and texto != "ROTEAR":
                print(f"Resposta:\n{texto}")
    else:
        modo_interativo(client, prompt_triagem, modelo)


if __name__ == "__main__":
    main()
