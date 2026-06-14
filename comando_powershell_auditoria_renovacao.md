# COMANDO POWERSHELL — Auditoria de Conversas de Renovação

## 1) Puxar as conversas de renovação do Supabase

```sql
SELECT
  telefone,
  nome_paciente,
  setor,
  estado,
  mensagens,
  created_at,
  updated_at
FROM conversas
WHERE setor ILIKE '%RENOVACAO%'
   OR setor = 'ENCERRADO'
ORDER BY updated_at DESC
LIMIT 50;
```

---

## 2) Instrução de análise (colar no PowerShell junto com a conversa)

> Você é auditor do fluxo de RENOVAÇÃO da Clara (REMMED). Recebe uma conversa
> e verifica se a Clara seguiu o fluxo correto. Para CADA conversa, responda
> apenas com os ERROS encontrados, no formato:
> `[telefone] — ERRO Nº: descrição curta + onde no fluxo falhou`
> Se não houver erro, responda `[telefone] — OK`.

### CHECKLIST DE ERROS A PROCURAR

**ERRO 1 — Prazo de 6 meses calculado errado / mensagens contraditórias**
- A Clara reverteu uma decisão sobre prazo já tomada?
- O paciente respondeu com mês/data e a Clara calculou errado?
- A fonte de verdade é a resposta SIM/NÃO sobre "menos de 6 meses".

**ERRO 2 — Tipo de consulta errado para antidepressivo C1**
- Medicamento é antidepressivo C1 (Sertralina, Fluoxetina, Desvenlafaxina/Elifore,
  Escitalopram, Venlafaxina, Bupropiona, Mirtazapina, Amitriptilina, Donaren/Trazodona)?
- Prazo venceu (mais de 6 meses) → DEVE oferecer Consulta de Saúde Mental R$249,00.
- ERRO se ofereceu clínico geral R$79,90 nesse caso.

**ERRO 3 — Pulou confirmação de cadastro**
- A Clara avançou para endereço/pagamento sem exibir resumo dos dados e
  receber SIM explícito do paciente?

**ERRO 4 — Cobrança gerada sem CEP/cidade**
- Chamou gerar_cobranca_direta sem ter coletado endereço antes?

**ERRO 5 — Renovou com mudança**
- Paciente pediu trocar remédio/dose/forma e a Clara renovou mesmo assim?
  (Renovação = cópia exata; mudança exige consulta.)

**ERRO 6 — Receita azul/amarela tratada errada**
- Benzodiazepínico (Rivotril etc.) ou amarela (Venvanse, Ritalina etc.)?
  → DEVE encerrar SEM oferecer consulta. ERRO se ofereceu consulta.

**ERRO 7 — Emagrecimento tratado errado**
- GLP-1 (Ozempic, Mounjaro, Saxenda etc.)?
  → DEVE encaminhar Consulta de Controle de Peso R$249,00. ERRO se renovou
  ou ofereceu R$79,90.

**ERRO 8 — Pediu CPF/nome repetido**
- A Clara pediu CPF ou nome mais de uma vez tendo o dado em mãos?

**ERRO 9 — Follow-up após encerramento**
- Conversa com setor ENCERRADO ou comprovante enviado recebeu follow-up?

---

## 3) Saída esperada

Lista enxuta só com os erros, agrupada por telefone, pronta para passar pro Nicolas.
```
Exemplo:
5516XXXXXXXX — ERRO 2: Elifore (desvenlafaxina) + prazo vencido → ofereceu R$79,90 (deveria R$249)
5516XXXXXXXX — ERRO 3: foi pra cobrança sem confirmar cadastro
5516YYYYYYYY — OK
```
