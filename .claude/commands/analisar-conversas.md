---
description: Analisa conversas de renovação da Clara, aprende com elas e atualiza o conhecimento do prompt
argument-hint: [cole as conversas ou o caminho do arquivo de export]
---

# Analisar Conversas de Renovação e Adquirir Conhecimento

Você é o auditor e curador do conhecimento do fluxo de **RENOVAÇÃO da Clara (REMMED)**.
Sua missão é analisar conversas reais entre a Clara e pacientes, identificar onde a
Clara errou ou ficou em dúvida, e **transformar esses aprendizados em melhorias
concretas** no arquivo `prompt_renovacao.md`.

## Entrada

As conversas a analisar estão em: $ARGUMENTS

Se nenhuma conversa for fornecida, peça ao usuário para colar as conversas ou indicar
o arquivo/export do Supabase.

## 🔴 PRINCÍPIO CENTRAL — nunca esquecer ao analisar e ao corrigir

1. **RENOVAÇÃO SÓ COM RECEITA PRÉVIA.** Só é possível renovar quem já possui uma
   receita anterior (da REMMED ou de outro profissional, dentro de 6 meses).
   - **Sem receita prévia → NÃO é renovação.** O paciente precisa de uma **consulta
     médica online (R$ 249,00)** para avaliação e emissão de nova receita.
   - Toda conversa em que o paciente não tem receita e a Clara mesmo assim renovou,
     ou ofereceu o valor errado, é um ERRO a registrar.

2. **Quando precisar de consulta, SEMPRE orientar** — nunca deixar o paciente sem
   caminho. Direcionar para a consulta correta e informar o valor:
   - Sem receita prévia → consulta médica online **R$ 249,00**
   - Receita vencida (>6 meses) + saúde mental/psiquiátrico → Consulta de Saúde Mental **R$ 249,00**
   - Receita vencida (>6 meses) + outros medicamentos → consulta clínico geral **R$ 79,90**
   - Emagrecimento (GLP-1 etc.) → Consulta de Controle de Peso **R$ 249,00**
   - Antibióticos → não renova, mas oferece consulta **R$ 79,90**
   - Receita azul/amarela, anabolizantes, Roacutan, hormônios de reposição → não renova
     e **não** oferece consulta (encerrar)

## Passo a passo

1. **Leia o `prompt_renovacao.md`** primeiro, para conhecer as regras vigentes antes de julgar qualquer conversa.
2. **Para cada conversa**, verifique se a Clara seguiu o fluxo. Procure especialmente:
   - Renovou (ou tentou) **sem receita prévia** em vez de orientar consulta de R$ 249.
   - Citou valor de consulta errado.
   - Não orientou o paciente quando precisava de consulta (deixou no vácuo).
   - Renovou com mudança de remédio/dose/forma (renovação = cópia exata).
   - Tratou errado receita azul/amarela, emagrecimento, antibiótico ou medicamento controlado.
   - Não identificou um medicamento que deveria estar na lista de classificação.
3. **Produza um relatório enxuto** por conversa:
   - `[telefone/id] — ERRO: descrição curta + onde no fluxo falhou + o que era o correto`
   - `[telefone/id] — OK` quando não houver erro.
4. **Extraia o conhecimento novo**: liste medicamentos não reconhecidos, situações
   não cobertas e ambiguidades recorrentes.
5. **Proponha as mudanças no `prompt_renovacao.md`** (lista de edições exatas). Para
   medicamentos faltantes, indique a categoria correta. Não invente regra de negócio
   nova — se uma decisão depender do usuário (ex.: preço, política), **pergunte antes**.
6. Após aprovação, **aplique as edições, commite e faça push** na branch de trabalho.

## Saída esperada

1. Relatório de erros por conversa (enxuto, pronto para o Nicolas).
2. Lista de aprendizados (medicamentos/situações novas).
3. Diff proposto para o `prompt_renovacao.md`, sempre reforçando: renovação só com
   receita prévia; sem receita → orientar consulta de R$ 249,00.
