"""Módulo 2 MFC — pages 1-14 content builder."""
import sys; sys.path.insert(0, '/home/user/clara-')
from pdf_helpers import *
from reportlab.platypus import PageBreak, KeepTogether
_S = S

def pages_1_to_14():
    S = []
    def add(*items):
        for x in items:
            if isinstance(x, list): S.extend(x)
            else: S.append(x)

    # ── P1: Cover + Sumário ─────────────────────────────────────────────────
    cover_p = Paragraph(
        'MÓDULO 2<br/>MEDICINA DE FAMÍLIA E COMUNIDADE<br/>(Específicos MFC)',
        _S('cv', fontName='Helvetica-Bold', fontSize=20, leading=28, textColor=WHITE, alignment=1))
    cov = Table([[cover_p]], colWidths=[BW])
    cov.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),NAVY),
        ('TOPPADDING',(0,0),(-1,-1),35),('BOTTOMPADDING',(0,0),(-1,-1),35),
        ('LEFTPADDING',(0,0),(-1,-1),15),('RIGHTPADDING',(0,0),(-1,-1),15),
    ]))
    add(cov, sp(10))
    add(Paragraph('SUMÁRIO', _S('st', fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=NAVY)))
    add(HRFlowable(width=BW, thickness=1, color=NAVY), sp(2))
    for it in [
        '1. Guia Estratégico',
        '2. MFC — Conceitos e Atributos (Starfield)',
        '3. Abordagem Centrada na Pessoa, Família e Comunidade',
        '4. Organização do Processo de Trabalho na APS',
        '5. Ética Médica, Sigilo, Prontuário e Consentimento',
        '6. Biossegurança e Segurança do Paciente',
        '7. Calendário Vacinal 2026 (PNI atualizado)',
        '8. Saúde da Criança — Puericultura e Triagem Neonatal',
        '9. Saúde da Mulher — Pré-natal e Planejamento Reprodutivo',
        '10. Rastreamento de Cânceres — Colo Útero (2025) e Mama (2025)',
        '11. HAS — Diretriz SBC 2025',
        '12. Diabetes Mellitus — Diretriz SBD 2024-2025',
        '13. Saúde do Adulto e do Idoso',
        '14. Saúde Mental na APS',
        '15. Demanda Programada/Espontânea e Visita Domiciliar',
        '16. Cuidado Compartilhado e Apoio Matricial',
        '17. Grupos Prioritários e Vulneráveis — Políticas Específicas',
        '18. Educação em Saúde',
        '19. Pegadinhas Clássicas IBAM (25)',
        '20. Questões de Revisão Comentadas (18)',
    ]: add(bul(it, 15))
    add(PageBreak())

    # ── P2: Guia Estratégico ────────────────────────────────────────────────
    add(sec_hdr('1. GUIA ESTRATÉGICO — MÓDULO 2'), sp(4))
    add(mk_tbl(
        ['Área','Questões','Peso','Pontos','Prioridade'],
        [['SUS/Saúde Coletiva (Módulo 1)','20','2','40','██████'],
         ['Específicos MFC (ESTE módulo)','10','3','30','████████ — maior peso/questão'],
         ['Língua Portuguesa','10','1','10','████']],
        [175,60,42,52,153]), sp(3))
    add(atc('ESTRATÉGIA',[
        'Cada questão aqui vale 3 pts — errar uma dói mais que errar no SUS.',
        'O IBAM cobra CONCEITOS e DEFINIÇÕES — não casos clínicos complexos.',
        'Foco máximo: atributos Starfield, rastreamentos (mudanças 2025!), calendário vacinal, HAS e DM.',
    ]), sp(4))
    add(mk_tbl(
        ['Tema','Frequência IBAM','Novidade 2025'],
        [['Atributos APS — Starfield (4 essenciais + 3 derivados)','Alta','Não'],
         ['Rastreamento colo útero — DNA-HPV como 1ª linha','Alta','SIM — crítico'],
         ['Rastreamento mama — 40 a 74 anos','Alta','SIM — Lei 15.284/2025'],
         ['HAS — Diretriz SBC 2025 (pré-hipertensão nova)','Alta','SIM'],
         ['DM — Diretriz SBD 2024-2025 (TOTG-1h)','Alta','SIM'],
         ['Calendário vacinal — vacina VSR gestante','Alta','SIM'],
         ['Processo de trabalho APS / acolhimento / demanda','Média-Alta','Não'],
         ['Saúde da criança — puericultura / 4 testes neonatais','Média-Alta','Não'],
         ['Saúde mental na APS — o que tratar vs encaminhar','Média','Não'],
         ['Grupos vulneráveis — políticas','Média','Não']],
        [235,118,129]))
    add(PageBreak())

    # ── P3: 2. MFC / Starfield ──────────────────────────────────────────────
    add(sec_hdr('2. MEDICINA DE FAMÍLIA — CONCEITOS E ATRIBUTOS DA APS (Starfield)'), sp(4))
    add(h3('2.1 Definição da Especialidade:'), sp(2))
    add(pj('A MFC provê atenção continuada, integral e centrada na pessoa, à família e à comunidade. '
           'O médico de família cuida de PESSOAS — não de órgãos isolados — em todas as fases da vida.'), sp(4))
    add(h3('2.2 Atributos da APS — Barbara Starfield:'), sp(2))
    add(mk_tbl(
        ['Atributo','Tipo','Definição','Pegadinha'],
        [['Primeiro Contato','ESSENCIAL','APS = porta de entrada PREFERENCIAL do sistema','A prova coloca "qualquer problema" → INCOMPLETO'],
         ['Longitudinalidade','ESSENCIAL','Vínculo contínuo profissional-paciente ao longo do tempo','Não é "continuidade de tratamento". Inclui pacientes saudáveis'],
         ['Integralidade','ESSENCIAL','Conjunto articulado: promoção + prevenção + reabilitação','Não é "resolver tudo na APS". É oferecer o conjunto e coordenar'],
         ['Coordenação do Cuidado','ESSENCIAL','APS organiza o cuidado ao longo dos pontos da rede','A prova coloca "coordenar hospital/UPA" → ERRADO: coordenação é função da APS'],
         ['Orientação Familiar','DERIVADO','Família como unidade de cuidado — genograma, APGAR familiar','Não obrigatório em toda APS; não existe em todo sistema'],
         ['Orientação Comunitária','DERIVADO','Conhecer e usar os recursos da comunidade/território, ACS, PSE','Não obrigatório em todos os sistemas'],
         ['Competência Cultural','DERIVADO','Adaptar cuidado à diversidade étnica, cultural e religiosa','Especialmente para população indígena']],
        [115,65,168,134]), sp(3))
    add(mac('MACETE — Atributos',[
        '4 ESSENCIAIS = PLIC: Primeiro contato | Longitudinalidade | Integralidade | Coordenação',
        '3 DERIVADOS: Orientação Familiar | Orientação Comunitária | Competência Cultural',
        'Essenciais = existem em qualquer APS de qualidade. Derivados = qualificam ainda mais.',
    ]), sp(2))
    add(peg('PEGADINHAS — Atributos',[
        'Longitudinalidade ≠ continuidade de tratamento. Vínculo inclui paciente SAUDÁVEL.',
        'Integralidade ≠ resolver tudo na APS. É oferecer o conjunto e coordenar o restante.',
        'São 4 essenciais — a prova cita 3 omitindo Coordenação ou coloca 5.',
    ]))
    add(PageBreak())

    # ── P4: 3. Abordagem Centrada ───────────────────────────────────────────
    add(sec_hdr('3. ABORDAGEM CENTRADA NA PESSOA, FAMÍLIA E COMUNIDADE'), sp(4))
    add(h3('3.1 Método SOAP (RCOP — Registro Clínico Orientado por Problemas):'), sp(2))
    add(mk_tbl(
        ['Componente','O que registra'],
        [['S — Subjetivo','Queixa principal, história da doença, medicamentos em uso, alergias — o que o paciente relata'],
         ['O — Objetivo','Sinais vitais, exame físico, resultados de exames — o que o profissional observa'],
         ['A — Avaliação','Hipóteses diagnósticas, diagnósticos, problemas identificados — raciocínio clínico'],
         ['P — Plano','Conduta: exames, prescrições, orientações, encaminhamentos, retorno']],
        [130,352]), sp(4))
    add(h3('3.2 Ferramentas de Avaliação Familiar:'), sp(2))
    add(mk_tbl(
        ['Ferramenta','Descrição'],
        [['Genograma','Representação gráfica da família em ≥3 gerações. Identifica padrões de doença e dinâmica. ■ = homem, ■ = mulher, X = falecido'],
         ['Ecomapa','Relações da família com ambiente externo: trabalho, amigos, serviços, comunidade'],
         ['APGAR Familiar','5 itens (0-2 cada): Adaptação | Participação | Crescimento (Growth) | Afeto | Resolução. 0-3=disfunção grave; 4-6=moderada; 7-10=boa função'],
         ['Ciclo de vida familiar','Estágios: formação → filhos pequenos → adolescentes → ninho vazio → velhice. Crises normativas em cada transição']],
        [120,362]), sp(2))
    add(mac('APGAR Familiar — cobrado pelo IBAM',[
        'A = Adaptação | P = Participação | G = Growth (Crescimento) | A = Afeto | R = Resolução',
        'Pontuação: cada item 0 (nunca), 1 (às vezes), 2 (sempre). Total 0-10.',
        'Mnêmonico: "APGAR" — igual ao Apgar do RN mas para a família.',
    ]), sp(4))
    add(h3('3.3 Modelo Biopsicossocial (Engel, 1977):'), sp(2))
    add(mk_tbl(
        ['Modelo','Foco','Base'],
        [['Biomédico','Doença como problema biológico isolado','Apenas biologia — ignora psique e contexto social'],
         ['Biopsicossocial (MFC)','Pessoa em seu contexto: corpo + mente + relações sociais','Bio + Psico + Social — base epistemológica da MFC']],
        [100,200,182]))
    add(PageBreak())

    # ── P5: 4. Processo de Trabalho ─────────────────────────────────────────
    add(sec_hdr('4. ORGANIZAÇÃO DO PROCESSO DE TRABALHO NA APS'), sp(4))
    add(h3('4.1 Demanda Programada vs Espontânea:'), sp(2))
    add(mk_tbl(
        ['Tipo','Definição','Exemplos','Organização'],
        [['Programada','Consultas agendadas — condições crônicas','HAS, DM, pré-natal, puericultura, idosos frágeis','60-70% da agenda. Blocos por programa.'],
         ['Espontânea','Queixas agudas, sem agendamento prévio','Faringite, lombalgia súbita, ansiedade','20-30% da agenda. Acolhimento com classificação de risco'],
         ['Visita domiciliar','Cuidado no território','Acamados, RN, puérperas, saúde mental','~10% da agenda']],
        [85,160,120,117]), sp(4))
    add(h3('4.2 Acolhimento:'), sp(2))
    add(pj('Postura ética de ESCUTA QUALIFICADA adotada por TODOS os profissionais em TODOS os momentos. '
           'Não é triagem. Não é sala de espera. Implica receber, ouvir, responsabilizar e direcionar.'), sp(4))
    add(h3('4.3 Classificação de Risco na APS:'), sp(2))
    add(mk_tbl(
        ['Cor','Prazo','Conduta'],
        [['Vermelho — Emergência','Imediata','Estabilização + SAMU ou transferência imediata'],
         ['Laranja — Urgência','≤15 min','Atendimento médico breve; monitorar'],
         ['Amarelo — Pouco urgente','≤30-60 min','Atendimento na sessão, pode aguardar'],
         ['Verde — Não urgente','≤120 min','Pode ser agendado ou atendido na sessão'],
         ['Azul — Eletivo','Agendamento','Orientação e consulta programada']],
        [135,100,247]), sp(3))
    add(peg('PEGADINHAS — Processo de Trabalho',[
        'Acolhimento ≠ triagem. Triagem = separar/filtrar. Acolhimento = escuta e responsabilização de TODOS.',
        '"Agenda fechada" não existe no SUS — UBS sempre avalia quem chega com demanda.',
        'Coordenação do cuidado é da APS — não do hospital nem do especialista.',
    ]))
    add(PageBreak())

    # ── P6: 5. Ética Médica ─────────────────────────────────────────────────
    add(sec_hdr('5. ÉTICA MÉDICA, SIGILO, PRONTUÁRIO E CONSENTIMENTO'), sp(4))
    add(h3('5.1 Lei 12.842/2013 — Exercício da Medicina:'), sp(2))
    add(mk_tbl(
        ['Ponto','Regra'],
        [['Atos privativos','Diagnóstico, prescrição, solicitação de exames, alta/internação, atestados, laudos, declaração de óbito'],
         ['Direção técnica','Chefia imediata de serviço de saúde = privativo do médico'],
         ['Emergência','Médico NUNCA pode recusar atendimento em emergência — mesmo em consultório particular'],
         ['Declaração de óbito','Médico assistente emite. SVO: quando não havia médico assistente. IML: suspeita de morte violenta']],
        [130,352]), sp(4))
    add(h3('5.2 Código de Ética Médica — CFM 2.217/2018:'), sp(2))
    add(mk_tbl(
        ['Tema','Regra','Exceção / Pegadinha'],
        [['Sigilo profissional','Dever de manter sigilo das informações do paciente','Exceção (Art. 73): notificação compulsória, proteção de terceiros, ordem judicial'],
         ['Notificação compulsória','DEVER do médico — mesmo sem autorização do paciente','NÃO viola sigilo. É exceção prevista em lei.'],
         ['Consentimento informado','Esclarecer sobre diagnóstico, tratamento, riscos e alternativas','Paciente PODE RECUSAR tratamento — mesmo com risco de vida (autônomo)'],
         ['Prontuário','Obrigatório. Prazo mínimo: 20 anos. Pertence ao SERVIÇO/INSTITUIÇÃO','A prova diz "pertence ao médico" → ERRADO. Paciente tem direito de acesso.'],
         ['Telemedicina','Permitida — Resolução CFM 2.314/2022. Exige sigilo e qualidade','A prova generaliza "ilegaldiade" → ERRADO']],
        [115,190,177]))
    add(PageBreak())

    # ── P7: 6. Biossegurança ────────────────────────────────────────────────
    add(sec_hdr('6. BIOSSEGURANÇA E SEGURANÇA DO PACIENTE'), sp(4))
    add(h3('6.1 Resíduos de Serviços de Saúde — RDC ANVISA 222/2018:'), sp(2))
    add(mk_tbl(
        ['Grupo','Tipo','Exemplos','Descarte'],
        [['A','Biológico','Sangue, secreções, curativo, placenta','Saco branco leitoso → autoclave'],
         ['B','Químico','Medicamentos vencidos, reagentes, mercúrio','Saco laranja ou recipiente específico'],
         ['C','Radioativo','Radiofármacos','Recipiente com símbolo de radioatividade'],
         ['D','Comum','Papéis, embalagens do refeitório','Saco preto — lixo comum'],
         ['E','Perfurocortante','Agulhas, lâminas, bisturis','Caixa amarela rígida (descarpak) — NUNCA no lixo comum']],
        [28,80,180,194]), sp(2))
    add(mac('MACETE — RSS',[
        'A=biológico | B=químico | C=radioativo | D=doméstico(comum) | E=perfurocortante(agulha)',
        'Agulha → SEMPRE caixa amarela (E). Nunca na lixeira comum.',
    ]), sp(4))
    add(h3('6.2 Segurança do Paciente — PNSP (Portaria 529/2013) — 6 Metas:'), sp(2))
    add(mk_tbl(
        ['Meta','Descrição','Na APS'],
        [['1. Identificar o paciente','≥2 identificadores: nome + data de nascimento','Conferir antes de vacinar ou medicar'],
         ['2. Comunicação efetiva','Passagem de casos clara — ISBAR','Carta de referência completa; prontuário legível'],
         ['3. Medicamentos seguros','Alta vigilância: insulina, anticoagulantes, cloreto de potássio','Conferir dose e via antes de injeções na UBS'],
         ['4. Cirurgia segura','Checklist OMS','Procedimentos menores (sutura) — técnica asséptica'],
         ['5. Higienizar as mãos','5 momentos da OMS — principal medida','Obrigatório antes e após todo atendimento'],
         ['6. Reduzir quedas/UP','Escala de Braden; avaliar risco de quedas','Visita domiciliar: ambiente seguro para o idoso']],
        [115,175,192]), sp(2))
    add(mac('5 Momentos da Higienização das Mãos',[
        '1. ANTES de tocar o paciente | 2. ANTES de procedimento asséptico',
        '3. APÓS risco de exposição a fluidos | 4. APÓS tocar o paciente',
        '5. APÓS tocar superfícies próximas ao paciente',
    ]))
    add(PageBreak())

    # ── P8: 7. Calendário Vacinal — Criança ─────────────────────────────────
    add(sec_hdr('7. CALENDÁRIO VACINAL 2026 — PNI (INSTRUÇÃO NORMATIVA CNV 2026 — ATUALIZADO 30/01/2026)'), sp(3))
    add(atc('NOVA VACINA 2025-2026 — VSR PARA GESTANTE',[
        'Vacina VSR (Vírus Sincicial Respiratório): 1 dose a partir da 28ª semana, em CADA gestação.',
        'Objetivo: proteger o RN contra bronquiolite e pneumonia por VSR — principal causa de hospitalização em lactentes.',
        'Anticorpo Nirsevimabe: alternativa para RN cujas mães não foram vacinadas.',
    ]), sp(3))
    add(h3('7.1 Calendário da Criança (0-9 anos):'), sp(2))
    add(mk_tbl(
        ['Idade','Vacinas','Observação Crítica'],
        [['Ao nascer (12-24h)','BCG dose única + HepB 1ª','BCG = dose única, sem reforço. HepB = obrigatória antes da alta.'],
         ['2 meses','Pentavalente 1ª + VIP 1ª + Rotavírus 1ª + Pneumo10 1ª + MenC 1ª','Rotavírus: JANELA — 1ª dose até 3m7d. Fora da janela = NÃO vacinar.'],
         ['3 meses','MenC 1ª','Esquema MenC: 3-5-12 meses'],
         ['4 meses','Pentavalente 2ª + VIP 2ª + Rotavírus 2ª + Pneumo10 2ª','Rotavírus: 2ª e ÚLTIMA dose — janela até 7m29d'],
         ['5 meses','MenC 2ª',''],
         ['6 meses','Pentavalente 3ª + VIP 3ª + Influenza','Influenza: anual. 1ª vez (<9 anos): 2 doses com 30d de intervalo'],
         ['9 meses','Febre Amarela 1ª dose','Antecipar 6-8 meses SOMENTE em área de risco com transmissão ativa'],
         ['12 meses','Pneumo10 reforço + MenC reforço + SCR + HepA','SCR = Sarampo + Caxumba + Rubéola'],
         ['15 meses','DTP reforço + VOP reforço + Varicela (SCRV)','DTP reforço. Varicela 2ª'],
         ['4 anos','DTP 2º reforço + VOP 2º reforço + FA reforço','FA: após 5 anos → dose ÚNICA vitalícia'],
         ['9 anos','HPV 4v (1 dose) — meninas E meninos','9-14a: dose única. ≥15a: 2 doses. Imunodeprimidos: 3 doses.'],
         ['COVID-19','Disponível a partir de 6 meses','Esquema conforme recomendação vigente']],
        [95,220,167]), sp(2))
    add(peg('PEGADINHAS — Calendário da Criança',[
        'BCG: dose ÚNICA — sem reforço. FA: 1ª dose até 9m, reforço 4a. Após 5 anos: dose única vitalícia.',
        'Rotavírus: JANELA RÍGIDA. 1ª até 3m7d. 2ª até 7m29d. Não vacinar fora do prazo.',
        'HPV: dose única para 9-14 anos (meninas E meninos). ≥15a: 2 doses.',
        'Influenza: anual. Primeira vez (<9a): 2 doses com 30 dias de intervalo.',
    ]), sp(4))
    add(h3('7.2 Calendário da Gestante:'), sp(2))
    add(mk_tbl(
        ['Vacina','Esquema','Observação'],
        [['dTpa','1 dose em CADA gestação — 27ª-36ª semana','Proteção do RN contra coqueluche. OBRIGATÓRIA em cada gestação.'],
         ['Influenza','1 dose em qualquer trimestre — anual','Protege gestante e RN'],
         ['Hepatite B','3 doses se não vacinada','Se já vacinada: não repetir'],
         ['COVID-19','Manter esquema atualizado','Segura em todos os trimestres'],
         ['VSR','1 dose a partir da 28ª semana, em CADA gestação','Nova 2025-2026. Protege RN de VSR.'],
         ['Febre Amarela','CONTRAINDICADA (vírus vivo)','Excepcionalmente: surto com risco real — avaliar após 1º trimestre'],
         ['SCR / Varicela','CONTRAINDICADAS (vírus vivos)','Administrar no puerpério imediato se não vacinada']],
        [100,200,182]))
    add(PageBreak())

    # ── P9: Gestante pegadinhas + Adulto/Idoso ──────────────────────────────
    add(peg('PEGADINHAS — Gestante',[
        'dTpa: em CADA gestação, não apenas na primeira.',
        'Febre Amarela: CONTRAINDICADA. Vírus vivo. A prova tenta colocar como obrigatória → ERRADO.',
        'VSR: nova vacina — não estava em provas anteriores.',
    ]), sp(4))
    add(h3('7.3 Adulto e Idoso (resumo):'), sp(2))
    add(mk_tbl(
        ['Vacina','Adulto (20-59a)','Idoso (≥60a)'],
        [['dT','Reforço a cada 10 anos','Reforço a cada 10 anos'],
         ['dTpa','1 dose em substituição ao dT (convive com bebê/gestante)','1 dose se nunca recebeu'],
         ['Influenza','Grupos de risco (gestante, prof. saúde, comorbidades)','OBRIGATÓRIA nas campanhas'],
         ['HepB','3 doses se não vacinado','3 doses se não vacinado'],
         ['Febre Amarela','1 dose única vitalícia (se área de risco)','Avaliar risco-benefício ≥60a'],
         ['Pneumo23','Não rotineira para saudável','Acamados/institucionalizados: 2 doses, intervalo 5 anos']],
        [100,192,190]))
    add(PageBreak())

    # ── P10: 8. Saúde da Criança ────────────────────────────────────────────
    add(sec_hdr('8. SAÚDE DA CRIANÇA — PUERICULTURA E TRIAGEM NEONATAL'), sp(4))
    add(h3('8.1 Puericultura — Frequência das Consultas:'), sp(2))
    add(mk_tbl(
        ['Faixa Etária','Frequência','Foco'],
        [['RN 0-28 dias','1ª consulta até 7 dias (ideal 3-5 dias)','Triagem neonatal, icterícia, coto umbilical, vínculo'],
         ['1-6 meses','Mensalmente','Crescimento, desenvolvimento, vacinação, aleitamento exclusivo'],
         ['6-12 meses','A cada 2 meses','Introdução alimentar, marcos de desenvolvimento'],
         ['1-2 anos','A cada 3 meses','Linguagem, marcha, desenvolvimento cognitivo'],
         ['2-6 anos','A cada 6 meses','Saúde bucal, visão, audição'],
         ['6-10 anos','Anual','Saúde escolar, crescimento, puberdade']],
        [120,120,242]), sp(4))
    add(h3('8.2 Triagem Neonatal — Os 4 Testes + 1:'), sp(2))
    add(mk_tbl(
        ['Teste','Prazo Ideal','O que Detecta','Detalhe Crítico'],
        [['Pezinho','3-5 dias de vida (até 30 dias)','Hipotireoidismo, Falciforme, Fibrose cística, Fenilcetonúria e outras','Pode ir até 30 dias em casos específicos. Ideal: 3-5 dias.'],
         ['Orelhinha','Antes da alta (até 1 mês)','Perda auditiva congênita','Obrigatória em hospitais com >500 partos/ano. OAE ou PEATE.'],
         ['Olhinho (Reflexo Vermelho)','Na maternidade ou 1ª consulta','Catarata, glaucoma, retinoblastoma','Reflexo ausente = encaminhar URGENTE à oftalmologia'],
         ['Coraçãozinho (Oximetria)','24-48h de vida','Cardiopatia congênita crítica','SpO2 ≥95% em MSD e MMII. Diferença ≤3%. Antes da alta.'],
         ['Linguinha','Antes da alta (complementar)','Anquiloglossia (freio curto)','Protocolo PIBF. Pode ser feito por enfermeiro treinado.']],
        [100,95,155,132]), sp(2))
    add(mac('Marcos de Desenvolvimento Motor — Referência Rápida',[
        '2m: sustenta cabeça em pronação | 4m: rola prono→ supino | 6m: senta com apoio',
        '9m: engatinha, pinça inferior, senta sem apoio | 12m: fica em pé, 1-3 palavras',
        '18m: anda bem, torre de 3 cubos | 24m: corre, frases de 2 palavras',
    ]), sp(4))
    add(h3('8.3 Aleitamento Materno:'), sp(2))
    add(mk_tbl(
        ['Aspecto','Recomendação Oficial (OMS + MS)'],
        [['Exclusivo','Apenas leite materno até 6 meses — sem água, chá ou qualquer outro alimento'],
         ['Complementado','Leite materno + alimentação complementar de 6 meses até 2 anos ou mais'],
         ['Introdução alimentar','A partir de 6 meses completos — frutas, legumes, cereais, carnes'],
         ['Contraindicações','HIV materno, HTLV, galactosemia no lactente, drogas ilícitas'],
         ['HBsAg positivo','NÃO contraindica AM se RN recebeu imunoglobulina + HepB nas primeiras 12h']],
        [130,352]))
    add(PageBreak())

    # ── P11: 9. Saúde da Mulher ─────────────────────────────────────────────
    add(sec_hdr('9. SAÚDE DA MULHER — PRÉ-NATAL E PLANEJAMENTO REPRODUTIVO'), sp(4))
    add(h3('9.1 Pré-natal de Risco Habitual (PHPN + Rede Cegonha):'), sp(2))
    add(mk_tbl(
        ['Aspecto','Recomendação MS'],
        [['Início','Até 12 semanas (1º tri). Ideal: até 120 dias (4 meses).'],
         ['Nº mínimo de consultas','6 (SUS: PHPN). OMS recomenda ≥8. — 1º tri: 1 | 2º tri: 2 | 3º tri: 3'],
         ['Exames obrigatórios','Tipagem + Rh | VDRL | Anti-HIV | HBsAg | Urina I | Glicemia jejum | Hemograma | Toxoplasmose IgM/IgG | Rubéola IgG | Urocultura'],
         ['VDRL','1º trimestre + 3º trimestre + no parto'],
         ['Anti-HIV','1º e 3º trimestres — prevenção transmissão vertical'],
         ['USG','Idealmente até 14 semanas para datação'],
         ['Vinculação à maternidade','Gestante deve conhecer a maternidade de referência antes do parto'],
         ['Alto risco','Idade <16 ou >35a, gemelar, HAS, DM, cardiopatia, pré-eclâmpsia prévia → REFERENCIAR']],
        [130,352]), sp(2))
    add(peg('PEGADINHAS — Pré-natal',[
        'VDRL: 1º tri + 3º tri + parto. Não é apenas 1 vez.',
        'Anti-HIV: 1º e 3º trimestres — rastreio do binômio.',
        'Rubéola: NÃO vacinar na gestação (vírus vivo). Rastrear; vacinar no puerpério.',
        'HBsAg positivo: NÃO contraindica AM (diferente do HIV).',
    ]), sp(4))
    add(h3('9.2 Planejamento Reprodutivo — Métodos na APS:'), sp(2))
    add(mk_tbl(
        ['Método','Eficácia Típica','Na APS'],
        [['Preservativo masculino','~85%','Único que protege contra IST. Sempre recomendar.'],
         ['COC (pílula combinada)','~91%','1ª linha sem contraindicações. CI: HAS grave, migrânea com aura, tabagismo >35a, trombofilia'],
         ['Minipílula (progestágeno)','~91%','Puérpera amamentando, CI ao estrogênio.'],
         ['Injetável trimestral (Depo-Provera)','~94%','Retorno da fertilidade: até 18 meses.'],
         ['DIU de cobre','>99%','Muito eficaz, não hormonal, reversível. Disponível no SUS. 10 anos.'],
         ['DIU hormonal (Mirena)','>99%','Reduz fluxo. 5 anos. Pode tratar endometriose.'],
         ['Laqueadura','>99%','Permanente. Consentimento livre e informado. SUS oferece.'],
         ['Vasectomia','>99%','Mais simples que laqueadura. SUS oferece.']],
        [140,75,267]))
    add(PageBreak())

    # ── P12: 10. Rastreamento Cânceres ──────────────────────────────────────
    add(sec_hdr('10. RASTREAMENTO DE CÂNCERES NA APS — DIRETRIZES ATUALIZADAS 2025'), sp(3))
    add(atc('MUDANÇAS CRÍTICAS 2025 — ALTÍSSIMA PROBABILIDADE DE CAIR NA PROVA',[
        'Colo do útero: DNA-HPV SUBSTITUI Papanicolau como método PRIMÁRIO (Portaria SAES/SECTICS 13/2025).',
        'Mama: faixa etária AMPLIADA para 40-74 anos (Lei 15.284/2025).',
    ]), sp(3))
    add(h3('10.1 Câncer do Colo do Útero — Nova Diretriz 2025:'), sp(2))
    add(info_box('Portaria SAES/SECTICS 13/2025 — MUDANÇA PRINCIPAL',[
        'ANTES (até 2024): Papanicolau como método primário, a cada 3 anos, 25-64 anos.',
        'AGORA: DNA-HPV oncogênico = MÉTODO PRIMÁRIO. Papanicolau = exame REFLEXO (secundário).',
        'Transição gradual: onde não há DNA-HPV disponível, Papanicolau continua sendo usado.',
    ], bc=PURPLE, bg=colors.HexColor('#F3E5F5'), tc=PURPLE), sp(2))
    add(mk_tbl(
        ['Aspecto','Modelo Anterior (Papanicolau)','Modelo Atual 2025 (DNA-HPV)'],
        [['Método primário','Papanicolau (citologia)','DNA-HPV oncogênico'],
         ['Faixa etária','25-64 anos','25-64 anos (igual)'],
         ['Intervalo','A cada 3 anos','A cada 5 anos se negativo'],
         ['HPV 16 ou 18 positivo','Não se aplicava','→ Colposcopia DIRETA'],
         ['Outros tipos oncogênicos','Não se aplicava','→ Citologia reflexa na mesma amostra'],
         ['DNA-HPV negativo','Não se aplicava','→ Repetir em 5 anos'],
         ['Papanicolau agora','Método primário','Exame reflexo apenas em casos específicos']],
        [145,145,192]), sp(2))
    add(peg('PEGADINHAS — Colo do Útero',[
        'Antes de 25 anos: NÃO rastrear (alta regressão espontânea).',
        'Após 64 anos com 2 exames negativos nos últimos 5 anos: ENCERRAR.',
        'HPV 16/18 = colposcopia DIRETA — não esperar citologia.',
        'DNA-HPV negativo = repetir em 5 ANOS (não 3 anos, não 1 ano).',
    ]), sp(4))
    add(h3('10.2 Câncer de Mama — Lei 15.284/2025:'), sp(2))
    add(info_box('Lei 15.284/2025 + Nota Técnica INCA 626/2025',[
        'ANTES (até set/2025): rastreamento bienal para 50-69 anos.',
        '40-49 anos: acesso GARANTIDO à mamografia por DECISÃO COMPARTILHADA médico-paciente.',
        '50-74 anos: rastreamento BIENAL ATIVO (ampliado de 69 para 74 anos).',
        'Acima de 74 anos: decisão INDIVIDUALIZADA.',
    ], bc=PURPLE, bg=colors.HexColor('#F3E5F5'), tc=PURPLE), sp(2))
    add(mk_tbl(
        ['Faixa Etária','Conduta 2025','Periodicidade'],
        [['< 40 anos','Apenas com fatores de risco elevado (BRCA, familiar 1º grau)','Individual — pode ser anual com RM'],
         ['40-49 anos','Acesso garantido por decisão compartilhada (Lei 15.284/2025)','Bienal se optar'],
         ['50-74 anos','Rastreamento bienal ATIVO (INCA/MS)','A cada 2 anos'],
         ['≥75 anos','Decisão individualizada','Conforme caso clínico']],
        [100,230,152]))
    add(PageBreak())

    # ── P13: Mama pegadinhas + Outros Rastreamentos ──────────────────────────
    add(peg('PEGADINHAS — Mama',[
        '"Rastreamento para 50 a 69 anos" → DESATUALIZADO. Agora: 50-74 anos (ativo) + 40-49 (decisão compartilhada).',
        '"Mamografia anual" → ERRADO. É bienal (a cada 2 anos).',
        'INCA e Lei 15.284 não são contraditórios: INCA prioriza 50-74; Lei garante ACESSO a partir dos 40.',
    ]), sp(4))
    add(h3('10.3 Outros Rastreamentos na APS:'), sp(2))
    add(mk_tbl(
        ['Câncer','Recomendação','Quem / Quando'],
        [['Colorretal','PSOF anual + colonoscopia a cada 10 anos','Homens e mulheres ≥50 anos, risco médio'],
         ['Próstata','PSA + toque retal — DECISÃO COMPARTILHADA','Homens ≥50a (45a se negro ou familiar 1º grau)'],
         ['Pulmão','TC de baixa dose — apenas tabagistas alto risco','≥50a, ≥20 maços-ano, fumante atual ou parou <15a'],
         ['Pele','Exame oportunístico — sem rastreamento formal no SUS','Especialmente fotoexpostos — orientar protetor solar']],
        [80,200,202]))
    add(PageBreak())

    # ── P14: 11. HAS ────────────────────────────────────────────────────────
    add(sec_hdr('11. HIPERTENSÃO ARTERIAL SISTÊMICA — DIRETRIZ SBC 2025'), sp(3))
    add(info_box('ATUALIZAÇÃO CRÍTICA — Diretriz HAS SBC 2025',[
        'NOVA CATEGORIA: Pré-hipertensão = PAS 120-139 mmHg E/OU PAD 80-89 mmHg.',
        'PA Normal AGORA: PAS <120 E PAD <80. (Antes: 120/80 era "ótima" — categoria extinta).',
        '1ª diretriz com capítulo sobre HAS NA APS e HAS EM MULHERES.',
    ], bc=PURPLE, bg=colors.HexColor('#F3E5F5'), tc=PURPLE), sp(3))
    add(mk_tbl(
        ['Classificação SBC 2025','PAS (mmHg)','PAD (mmHg)','Conduta'],
        [['PA Normal','< 120','< 80','Reavaliar anualmente'],
         ['Pré-hipertensão (NOVA)','120-139','80-89','MEV. MAPA/MRPA se suspeita de hipertensão mascarada.'],
         ['HAS Estágio 1','140-159','90-99','Confirmar + MEV ± fármaco conforme risco CV'],
         ['HAS Estágio 2','160-179','100-109','MEV + tratamento farmacológico'],
         ['HAS Estágio 3','≥180','≥110','Tratamento imediato'],
         ['Urgência hipertensiva','≥180/120 SEM lesão órgão-alvo','','Reduzir PA em horas. Medicação oral.'],
         ['Emergência hipertensiva','≥180/120 COM lesão órgão-alvo','','Internação. Reduzir PA em minutos. Via IV.']],
        [138,70,70,204]), sp(3))
    add(mk_tbl(
        ['Aspecto','Detalhe — Diretriz SBC 2025'],
        [['Diagnóstico','≥140/90 em consultório. ≥2 medidas/consulta, ≥2 consultas em dias diferentes (ou MAPA/MRPA)'],
         ['MAPA','Padrão ouro 24h. Identifica avental branco, mascarada, hipertensão noturna'],
         ['HAS avental branco','Alta no consultório, normal fora (MAPA normal). NÃO é HAS — mas tem risco aumentado'],
         ['HAS mascarada','Normal no consultório, alta fora (MAPA alterado). É HAS — tratar'],
         ['Meta geral','< 140/90 mmHg para maioria'],
         ['Meta alto risco CV','< 130/80 — DCV estabelecida, DM, DRC, risco CV ≥20%'],
         ['1ª linha farmacológica','IECA ou BRA + BCC (bloqueador canal de cálcio) + Diurético tiazídico — qualquer dos 3'],
         ['HAS na gestante','CONTRAINDICADOS: IECA e BRA. Usar: metildopa (1ª linha), nifedipino, hidralazina'],
         ['Mudança estilo de vida','Sódio <2g/dia, dieta DASH, exercício, perda de peso, redução álcool, cessação tabagismo']],
        [145,337]), sp(2))
    add(peg('PEGADINHAS — HAS',[
        '120/80 = PA Normal. 120-139/80-89 = Pré-hipertensão (nova). ≥140/90 = HAS.',
        'IECA e BRA: CONTRAINDICADOS na gestação. A prova inclui como opção para gestante → ERRADO.',
        'Urgência = sem lesão órgão-alvo. Emergência = COM lesão. A prova confunde.',
        'Diagnóstico: não em uma medida isolada. Requer confirmação.',
    ]))
    add(PageBreak())

    return S

if __name__ == '__main__':
    print(f"Pages 1-14 builder: {len(pages_1_to_14())} flowables")
