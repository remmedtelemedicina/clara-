# Bugs Encontrados — Fluxo de Renovação de Receita
**Caso:** Rafaela · Data: 12/06 · Medicamento: Elifore 100mg (Desvenlafaxina — antidepressivo C1)

---

## BUG 1 — Cálculo de 6 meses errado + mensagens contraditórias

**O que aconteceu:**
Clara perguntou se a receita tinha mais ou menos de 6 meses. A paciente respondeu com um mês/data em vez de SIM/NÃO. Clara calculou errado e enviou mensagens contraditórias — primeiro disse que estava no prazo, depois reverteu.

**Causa raiz:** Prompt não instrui Clara a calcular a diferença a partir da data atual (topo da sessão). Sem âncora de data, Clara erra. E não há regra impedindo reversão da decisão.

**Correção necessária no prompt:**
> Na seção `# REGRAS ABSOLUTAS`: A resposta SIM/NÃO do paciente é a fonte de verdade. Se o paciente informar mês ou data, calcular diferença em relação à data da sessão. Uma vez decidido, NUNCA reverter. Em dúvida, perguntar uma única vez: "Sua última receita foi emitida há menos de 6 meses? (sim/não)"

---

## BUG 2 — Ofertou consulta errada para antidepressivo C1

**O que aconteceu:**
Elifore 100mg = Desvenlafaxina = antidepressivo C1. Como o prazo de 6 meses estava vencido, Clara deveria ter oferecido **Consulta de Saúde Mental R$249,00**. Em vez disso, ofertou consulta com clínico geral **R$79,90**.

**Causa raiz:** Prompt não tem regra explícita separando antidepressivos C1 do caminho de clínico geral.

**Correção necessária no prompt:**
> Na seção `# REGRAS ABSOLUTAS`: Antidepressivo C1 que precisa de consulta → SEMPRE Saúde Mental R$249,00. NUNCA clínico geral. Lista: Sertralina, Fluoxetina, Desvenlafaxina/Elifore, Escitalopram, Venlafaxina, Bupropiona, Mirtazapina, Amitriptilina, Trazodona e similares.

---

## BUG 3 — Pulou etapa de confirmação do cadastro

**O que aconteceu:**
Clara coletou nome, CPF e endereço mas avançou diretamente para cobrança sem exibir o resumo dos dados e pedir confirmação do paciente. Se qualquer dado estiver errado, o cadastro no Amplimed fica incorreto.

**Causa raiz:** Não há regra no prompt obrigando confirmação antes de avançar.

**Correção necessária no prompt:**
> Na seção `# REGRAS ABSOLUTAS`: NUNCA avançar para endereço/cobrança sem: (1) exibir resumo dos dados coletados, (2) perguntar "Confirma que estão corretos? (sim/não)", (3) receber SIM explícito do paciente.

---

## BUG 4 — Follow-up enviado após pagamento já realizado

**O que aconteceu:**
Rafaela já havia enviado o comprovante de pagamento. Mesmo assim, o workflow de follow-up disparou mensagem perguntando se ela precisava de ajuda — como se o atendimento tivesse ficado no meio.

**Causa raiz:** Workflow de follow-up no n8n não verifica se o setor está "ENCERRADO" ou se comprovante foi recebido antes de disparar.

**Correção necessária no n8n (workflow de follow-up):**
> Adicionar condição antes do envio: se `setor = ENCERRADO` OU paciente enviou comprovante → NÃO enviar follow-up.

---

## Resumo das correções

| # | Onde corrigir | Urgência |
|---|---------------|----------|
| 1 | Prompt — seção REGRAS ABSOLUTAS | Alta |
| 2 | Prompt — seção REGRAS ABSOLUTAS + caminho "mais de 6 meses" | Alta |
| 3 | Prompt — seção REGRAS ABSOLUTAS | Média |
| 4 | n8n — workflow de follow-up | Média |
