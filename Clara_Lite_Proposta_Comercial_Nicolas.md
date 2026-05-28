# Clara Lite — Proposta Comercial
### Documento Interno · REMMED Telemedicina
---

## Visão Geral do Produto

**Clara Lite** é a versão da inteligência artificial da REMMED desenvolvida para médicos solo e pequenas clínicas que não possuem estrutura de secretaria digital ou sistema de triagem automatizada.

O produto entrega, em sua primeira versão, **exclusivamente a triagem clínica por WhatsApp** — que é exatamente o componente mais robusto e diferenciado que a REMMED já construiu, testou em produção e comprovou em volume real de pacientes.

---

## O Problema que Resolvemos

Um médico solo hoje enfrenta três problemas simultâneos no WhatsApp:

1. **Pacientes chegam sem preparação** — o médico não sabe o que vem antes da consulta
2. **Mensagens repetitivas tomam tempo** — horário, valor, como funciona, o que trazer
3. **Casos de urgência passam despercebidos** — paciente agenda telemedicina com sintoma de emergência

Nenhum dos concorrentes diretos (Carecode, ALMA) resolve os três ao mesmo tempo. O Carecode é agendamento com 1 pergunta de segurança. O ALMA é pós-consulta. **A Clara Lite resolve os três com uma única IA.**

---

## O que está incluído na versão inicial

### Módulo 1 — Triagem Clínica Inteligente
- Recebe o paciente no WhatsApp e identifica o motivo de contato
- Coleta: queixa principal, tempo de evolução, intensidade e sintomas associados
- Classifica por grupo clínico (respiratório, cardiovascular, neurológico, digestivo, musculoesquelético, dermatológico, geral)
- Identifica sinais de alarme e orienta busca de atendimento presencial/SAMU
- Gera resumo estruturado da queixa antes da consulta

### Módulo 2 — FAQ Automático
- Responde dúvidas frequentes: horário, valor, como funciona, documentos, atestado, CRM
- Reduz em até 80% as mensagens repetitivas que chegam fora do horário de atendimento
- Funciona 24h, 7 dias por semana

### Módulo 3 — Filtro de Segurança para Telemedicina
- Verifica elegibilidade do paciente para consulta online
- Aplica regra de consistência: se alarme foi relatado na conversa, bloqueia telemedicina mesmo que o paciente diga "melhorei"
- Orientação automática para pronto-socorro em casos de emergência

---

## O que NÃO está incluído nesta versão

Para manter o custo baixo e a entrega rápida, a versão inicial não inclui:

- Integração com agenda ou prontuário eletrônico
- Agendamento automático de consultas
- Relatórios e dashboards
- Módulo de retorno e follow-up pós-consulta
- Suporte a múltiplos médicos ou clínica com mais de 1 número WhatsApp

Esses módulos estão planejados como expansões futuras (Clara Pro).

---

## Diferencial Competitivo

| | **Carecode** | **ALMA** | **Clara Lite** |
|---|---|---|---|
| Triagem clínica por grupo de sintoma | ✗ | ✗ | ✅ |
| Identificação de sinais de alarme | Básico (1 pergunta) | ✗ | ✅ Completo |
| FAQ automático no WhatsApp | ✓ | ✗ | ✅ |
| Filtro de segurança telemedicina | Parcial | ✗ | ✅ Com regra de consistência |
| Funciona via WhatsApp nativo | ✓ | ✗ | ✅ |
| Foco no médico solo | ✗ | ✗ | ✅ |
| Preço mensal estimado | ~R$800–1.200 | ~R$500–900 | **R$700** |

---

## Estrutura de Preço

### Taxa de Implementação
**R$ 4.500,00** (pagamento único)

Inclui:
- Configuração do número WhatsApp Business API (Evolution API)
- Personalização da IA com nome do médico, especialidade e tom de voz
- Configuração do FAQ com dados reais do consultório (horário, valor, endereço)
- Integração e testes com o número do médico
- Treinamento de 1h com o médico para validar os fluxos
- 30 dias de suporte ativo pós-lançamento (ajustes finos inclusos)

### Mensalidade
**R$ 700,00/mês**

Inclui:
- Manutenção e operação da IA em produção
- Atualização de FAQ quando o médico solicitar (até 2x por mês)
- Monitoramento de erros e ajustes de comportamento
- Suporte via WhatsApp em horário comercial

### Modelo de Contrato
- Contrato mínimo: 6 meses
- Após 6 meses: renovação mensal automática
- Aviso de cancelamento: 30 dias de antecedência

---

## Análise Financeira para o Médico Cliente

### Retorno sobre o investimento

Um médico solo que faz 15 consultas por semana = ~60 consultas por mês.

Se a Clara Lite economizar **apenas 3 minutos por paciente** em mensagens repetitivas no WhatsApp:
- 60 pacientes × 3 min = **180 minutos por mês economizados**
- = 3 horas de consulta liberadas
- A R$79,90 por consulta: **R$239,70 de receita potencial adicional**

A mensalidade de R$700 é coberta com **menos de 9 consultas por mês**.

### Argumento de venda direto
> "Você paga R$700/mês para ter uma recepcionista que trabalha 24h, nunca falta, nunca erra o horário, triaga o paciente antes de chegar, e ainda bloqueia automaticamente casos de emergência que não podem ser atendidos por telemedicina."

---

## Perfil do Cliente Ideal (ICP)

### Médico Solo — Perfil Principal
- Especialidades prioritárias: clínica geral, telemedicina, medicina do trabalho, ginecologia, dermatologia, psiquiatria
- Atende por telemedicina (total ou parcialmente)
- Não tem secretária ou a secretária não atende WhatsApp fora do horário
- Recebe 30–200 mensagens de pacientes por mês via WhatsApp
- Já usa WhatsApp Business (ou está disposto a migrar)
- Faixa de renda: R$15.000–50.000/mês (pode pagar R$700 sem sentir)

### Sinais de que é um bom cliente
- Reclama que paciente manda mensagem de madrugada
- Já perdeu paciente por demora no retorno
- Faz telemedicina e tem medo de caso de urgência passando despercebido
- Quer crescer mas não quer contratar secretária

---

## Canais de Aquisição Recomendados

### Curto prazo (0–3 meses)
1. **Indicação direta** — médicos que já conhecem a REMMED ou usaram o serviço como paciente
2. **Grupos de médicos no WhatsApp/Telegram** — grupos de telemedicina, clínica geral, medicina do trabalho
3. **LinkedIn** — perfil do fundador + conteúdo sobre triagem por IA

### Médio prazo (3–6 meses)
4. **Parcerias com CFM/CRM estaduais** — validação institucional
5. **Instagram médico** — Reels mostrando a Clara funcionando (antes/depois de mensagens)
6. **Indicação de médico para médico** — programa de referral: 1 mês grátis para quem indicar

### Mensagem de marketing (hook)
> "Enquanto você dorme, a Clara está triando seu próximo paciente."

---

## Roteiro de Venda (para Nicolas usar na abordagem)

### Passo 1 — Abertura (identificar dor)
*"Você recebe mensagem de paciente fora do horário? E quanto tempo você gasta por semana respondendo sempre as mesmas perguntas?"*

### Passo 2 — Apresentação rápida (2 minutos)
*"A Clara é uma IA que atende seu paciente no WhatsApp antes mesmo de você entrar na consulta. Ela faz a triagem, responde as dúvidas básicas, e filtra quem pode ser atendido por telemedicina e quem precisa ir ao pronto-socorro."*

### Passo 3 — Demo ao vivo
Mandar uma mensagem no número de demonstração da REMMED e mostrar a triagem funcionando em tempo real.

### Passo 4 — Objeções comuns

| Objeção | Resposta |
|---|---|
| "Meu paciente vai achar estranho" | "Mais de 80% dos pacientes preferem resolver no WhatsApp. A IA é apresentada com seu nome e especialidade." |
| "E se ela errar?" | "Ela não fecha diagnóstico. Ela coleta e organiza. O médico continua sendo o médico." |
| "R$700 é caro" | "É menos de 9 consultas. E você recupera isso na primeira semana de tempo economizado." |
| "Não quero mudar meu número" | "Você mantém seu número. Configuramos um número dedicado ou integramos com o seu atual." |

### Passo 5 — Fechamento
*"Posso te mostrar como ficaria a Clara com seu nome e sua especialidade? Demora 15 minutos."*

---

## Plano de Onboarding (pós-venda)

### Semana 1 — Configuração
- Coleta dos dados do consultório (formulário enviado ao médico)
- Configuração técnica (n8n + Evolution API + Supabase)
- Personalização: nome do médico, especialidade, FAQ inicial

### Semana 2 — Testes
- Testes internos com cenários reais
- Demo ao médico + ajustes de tom e linguagem
- Aprovação do médico

### Semana 3 — Lançamento
- Ativação do número em produção
- Acompanhamento diário dos primeiros 7 dias
- Ajustes finos conforme feedback

### Semana 4 — Entrega
- Reunião de 30 min: revisão dos primeiros atendimentos
- Ajuste do FAQ com dúvidas que apareceram
- Início do período de suporte mensal padrão

---

## Métricas de Sucesso (para o médico perceber valor)

Ao final do primeiro mês, mostrar para o médico:
- Quantas mensagens a Clara respondeu automaticamente
- Quantos casos de alarme foram identificados e redirecionados
- Quantas perguntas de FAQ foram respondidas sem o médico
- Horário de pico de mensagens (dado útil para o médico)

---

## Próximos Passos para Nicolas

1. **Definir número de demonstração** — um número WhatsApp dedicado apenas para demos de venda
2. **Criar formulário de onboarding** — coleta os dados do médico: nome, especialidade, horário, valor, endereço, FAQ inicial
3. **Parametrizar o prompt** — adaptar o prompt da Clara para receber nome/especialidade/FAQ de forma dinâmica por cliente
4. **Criar instância separada** — cada cliente roda em instância própria no Evolution API
5. **Testar com 1 médico piloto** — de preferência alguém próximo, sem cobrar setup, para gerar depoimento e validar o fluxo completo

---

*Documento gerado em 28/05/2026 · REMMED Telemedicina · Uso interno*
