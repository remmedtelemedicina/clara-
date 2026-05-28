# REMMED — Visão Estratégica Completa
### Documento para Nicolas · Confidencial · Maio 2026

---

## Por que este documento existe

Nas últimas semanas, a estratégia da REMMED evoluiu de forma significativa. O que começou como uma operação de telemedicina se transformou em uma tese de startup com três camadas distintas. Este documento consolida tudo o que foi pensado, estruturado e validado — para que você, Nicolas, entenda a visão completa e saiba exatamente o que precisa ser construído e em qual ordem.

Isso não é mais "uma ideia de Uber da saúde."

É uma tese de infraestrutura de acesso à saúde — com um modelo de aquisição de oferta que nenhuma empresa está fazendo no Brasil.

---

## O Gap que ninguém resolveu

O comportamento do consumidor brasileiro foi completamente transformado por três plataformas:

- **iFood** — "quero comida agora" → resolvido
- **Uber** — "quero transporte agora" → resolvido
- **Airbnb** — "quero hospedagem agora" → resolvido

O que ainda não existe:

> **"Quero um médico agora"** → ❌ não resolvido

O Doctoralia agenda para amanhã. A Conexa é B2B (empresa paga). O DrConsulta é presencial. Nenhuma plataforma entrega consulta médica sob demanda, via WhatsApp, em menos de 30 minutos.

**Esse é o espaço que a REMMED vai ocupar.**

---

## O que estamos construindo — 3 Camadas

### CAMADA 1 — Clara Lite (produto de entrada já em desenvolvimento)

**O que é:**
SaaS de triagem inteligente para médicos solo via WhatsApp.

**Para quem:**
Médico recém-formado ou recém-especializado, atendendo por telemedicina, sem equipe, sem secretária. O cara que ganha R$11k no interior de SP, faz plantão para complementar, e quer crescer sem contratar ninguém por enquanto.

**O que entrega:**
- Triagem clínica automática antes da consulta (7 grupos de sintomas)
- FAQ automático 24h (horário, valor, documentos, atestado)
- Filtro de segurança para telemedicina (identifica urgências)
- Resumo estruturado da queixa antes de o médico abrir a conversa

**Precificação:**
- Setup: R$1.500 (versão entrada) ou R$4.500 (versão completa)
- Mensalidade: R$400–700/mês
- Contrato mínimo: 6 meses

**Por que isso importa estrategicamente:**
A Clara Lite não é o produto final. Ela é o **cavalo de Troia**.

O médico entra pagando pela automação. Mas ao entrar, ele se torna **oferta disponível dentro do marketplace futuro**. A REMMED adquire médicos com receita positiva — a maioria dos marketplaces paga para adquirir oferta. Aqui, a oferta paga para entrar.

---

### CAMADA 2 — REMMED Network (próxima fase)

**O que é:**
Rede de médicos parceiros com disponibilidade ativa. O médico "liga" sua disponibilidade quando está livre e recebe pacientes encaminhados pela REMMED.

**Fluxo:**
```
Paciente → WhatsApp REMMED
→ Clara faz triagem
→ "Temos um [especialidade] disponível agora. Consulta: R$99,90."
→ Paciente confirma
→ Pix gerado para o médico
→ Link de videochamada enviado
→ REMMED retém 20–25% da transação
```

**Sem app. Sem download. Funciona com a infraestrutura que já existe.**

**Modelo financeiro:**

| Consulta | Valor | Médico recebe | REMMED recebe |
|---|---|---|---|
| Padrão | R$99,90 | R$75,00 | R$24,90 (25%) |
| Urgente | R$149,90 | R$110,00 | R$39,90 (27%) |
| Retorno | R$59,90 | R$45,00 | R$14,90 (25%) |

Com 10 médicos × 3 consultas/dia = 30 consultas/dia × R$25 = **R$750/dia → R$22.500/mês** só no marketplace. Isso sem contar as mensalidades da Clara Lite.

---

### CAMADA 3 — Marketplace de Acesso Imediato (visão futura)

**O que é:**
Plataforma de acesso médico sob demanda — o "Uber da Saúde".

**Diferença do Uber:**
O Uber manda o motorista mais próximo. A REMMED, com a triagem da Clara, manda o **médico certo**:

> Paciente descreve tosse + falta de ar → Clara identifica grupo respiratório → encaminha para pneumologista disponível agora, não para clínico geral que vai redirecionar depois.

**Isso é matching inteligente. Nenhuma plataforma faz isso hoje.**

**Posicionamento:**
Não é "telemedicina". Não é "clínica online". É:

> **"Infraestrutura de acesso médico imediato — o médico certo, no momento certo, pelo canal onde o paciente já está."**

**O app vem por último.** Só depois de ter 50+ médicos ativos e fluxo comprovado vale o investimento em desenvolvimento mobile.

---

## Por que o WhatsApp é o maior ativo

97% dos smartphones brasileiros têm WhatsApp instalado. O custo de aquisição de usuário via WhatsApp é praticamente zero. Nenhum concorrente está usando WhatsApp como infraestrutura principal de marketplace.

Isso significa que a REMMED resolve o maior problema de qualquer marketplace — fricção de entrada — antes mesmo de ter um produto.

O paciente não precisa baixar nada. Não precisa criar conta. Não precisa aprender uma interface nova. Ele só manda mensagem.

---

## Estrutura Jurídica — Atenção Máxima

Este ponto é crítico e precisa estar correto desde o início.

### Modelo correto: Plataforma, não clínica

A REMMED deve se posicionar juridicamente como **fornecedora de tecnologia e intermediadora**, não como prestadora de serviço médico.

**O contrato do paciente é com o médico — não com a REMMED.**

A REMMED:
- Fornece a tecnologia (SaaS)
- Intermedia a conexão
- Facilita o pagamento
- Não presta o ato médico

**O que isso muda na prática:**
- Termos de uso: "A REMMED é uma plataforma de conexão. O serviço médico é prestado pelo profissional autônomo cadastrado."
- Pagamento: o Pix pode ir para o médico direto ou passar pela REMMED como intermediário financeiro — mas o contrato precisa deixar claro que é repasse
- Comunicação: nunca dizer "a REMMED vai te atender" — sempre "conectamos você com um médico disponível"

**CFM Resolução 2.314/2022:** A telemedicina é regulada, mas empresas de tecnologia podem intermediar desde que o responsável pelo ato médico seja o profissional com CRM. A estrutura do Doctoralia e do Zocdoc nos EUA funcionam exatamente assim.

---

## O Problema que a Clara Resolve para o Marketplace

Todo marketplace de saúde enfrenta um problema operacional imenso: médico recebe paciente sem contexto, paciente chega sem preparação, a consulta perde tempo na coleta de informações básicas.

A Clara resolve isso antes do paciente entrar na consulta.

**Sem Clara:**
```
Paciente entra → médico passa 10 minutos coletando queixa → 20 minutos de consulta efetiva
```

**Com Clara:**
```
Paciente triado → médico já sabe: queixa principal, tempo, intensidade, sintomas associados, alertas
→ 30 minutos de consulta efetiva desde o início
```

A Clara não é um produto à parte. Ela é a **inteligência operacional do marketplace** — o que torna o sistema escalável sem virar caos.

---

## O Número que Valida Tudo

Antes de qualquer investimento em app ou escala, precisamos de um número:

> **Taxa de conversão: triagem → consulta efetivada**

Se 100 pacientes entram na triagem e 30 consultam = 30% de conversão. Esse é o número que valida o modelo inteiro. Todo o restante — projeção de receita, LTV por médico, custo de aquisição — deriva daí.

**Como medir:** implementar o fluxo manual primeiro (ver próxima seção) e rastrear quantas triagens viram consulta nas primeiras 4 semanas.

---

## Plano de Execução — 90 Dias

### Fase 0 — O que já existe (hoje)
- ✅ Clara com triagem funcional (7 grupos de sintomas)
- ✅ FAQ automático via WhatsApp
- ✅ Identificação de sinais de alarme
- ✅ Infraestrutura n8n + Evolution API + Supabase
- ✅ Número WhatsApp ativo com fluxo validado

### Fase 1 — Semanas 1–4: Validação manual

**Objetivo:** Provar que o modelo funciona antes de automatizar.

**O que Nicolas precisa construir:**
1. Parametrizar o prompt da Clara por cliente (nome do médico, especialidade, FAQ)
2. Criar instância separada no Evolution API por médico contratante
3. Formulário de onboarding para coleta dos dados do médico (Google Forms resolve)
4. Fluxo de Pix para repasse (pode ser manual nas primeiras semanas)

**O que fazer em paralelo:**
- Recrutar 3–5 médicos parceiros dispostos a entrar na rede de disponibilidade
- Testar fluxo completo: triagem → match → link de reunião → pagamento

**Meta da fase:** 3 médicos ativos, 30 consultas efetivadas via plataforma

---

### Fase 2 — Semanas 5–8: Automatização do fluxo

**Objetivo:** Remover o trabalho manual do processo.

**O que Nicolas precisa construir:**
1. **Roteamento automático:** quando a Clara finaliza triagem e identifica especialidade, notifica médicos disponíveis automaticamente
2. **Sistema de disponibilidade:** médico consegue ligar/desligar sua disponibilidade via WhatsApp (comando simples: "disponível" / "indisponível")
3. **Geração de Pix automática:** integração com API de pagamento (Pagar.me, Asaas, ou PrimePag — já usam PIX dinâmico)
4. **Envio automático do link de videochamada** após confirmação de pagamento
5. **Notificação ao médico** com resumo da triagem antes da consulta

**Stack sugerida:**
- Pagamento: Asaas (API simples, split de pagamento nativo)
- Videochamada: Daily.co ou Whereby (API, gera link por demanda)
- Tudo dentro do n8n (sem novo backend por enquanto)

**Meta da fase:** fluxo 100% automático, zero intervenção manual por consulta

---

### Fase 3 — Semanas 9–12: Escala e métricas

**Objetivo:** Ter dados que provam o modelo para apresentar externamente.

**O que Nicolas precisa construir:**
1. **Dashboard simples** (pode ser Metabase ou até Google Sheets automatizado):
   - Consultas por dia
   - Taxa de conversão triagem → consulta
   - Receita por médico
   - Especialidades mais demandadas
   - Horários de pico
2. **Relatório automático mensal** para cada médico parceiro
3. **Sistema de avaliação pós-consulta** (1 pergunta via WhatsApp 2h após a consulta)

**Meta da fase:** 10+ médicos ativos, 100+ consultas efetivadas, taxa de conversão documentada

---

## Próximos passos imediatos (esta semana)

| Prioridade | Ação | Responsável |
|---|---|---|
| 1 | Definir número WhatsApp de demonstração da Clara Lite | Nicolas |
| 2 | Criar formulário de onboarding do médico | Nicolas |
| 3 | Parametrizar prompt da Clara por cliente | Nicolas |
| 4 | Identificar 3 médicos para piloto da rede | Raíssa |
| 5 | Definir contrato simples médico ↔ REMMED | Raíssa + jurídico |
| 6 | Configurar conta Asaas para split de pagamento | Nicolas |

---

## Visão de Médio Prazo (6–18 meses)

**6 meses:** 20 médicos ativos na rede, 500+ consultas/mês, Clara Lite com 15 contratos, receita recorrente de R$35–50k/mês

**12 meses:** 100 médicos, 3.000 consultas/mês, início de desenvolvimento do app mobile, apresentação para fundos de investimento seed

**18 meses:** App lançado, 500 médicos, presença em 3 estados, rodada seed de R$2–5M para escala nacional

---

## O Posicionamento Final

Não "telemedicina". Não "clínica online". Não "consulta por WhatsApp".

> **"REMMED é a infraestrutura que conecta o paciente ao médico certo, no momento em que ele precisa, pelo canal onde ele já está."**

Isso é uma tese de infraestrutura de saúde. E infraestrutura é o negócio mais defensável que existe — quem chega primeiro e constrói confiança não é substituído.

O app não é o negócio. O negócio é: **rede + confiança + liquidez.**

E os três estão sendo construídos agora.

---

*REMMED Telemedicina · Documento interno · Maio 2026*
*Uso restrito: Raíssa e Nicolas*
