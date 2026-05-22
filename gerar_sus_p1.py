"""Módulo 1 SUS — pages 1-24 content builder."""
import sys; sys.path.insert(0, '/home/user/clara-')
from pdf_helpers import *
from reportlab.platypus import PageBreak, KeepTogether
_S = S

def pages_1_to_24():
    S_ = []
    def add(*items):
        for x in items:
            if isinstance(x, list): S_.extend(x)
            else: S_.append(x)

    # ── P1: Capa + Sumário ──────────────────────────────────────────────────
    cover_p = Paragraph(
        'MÓDULO 1<br/>SISTEMA ÚNICO DE SAÚDE<br/>(SUS — Legislação e Políticas de Saúde)',
        S('cv', fontName='Helvetica-Bold', fontSize=20, leading=28, textColor=WHITE, alignment=1))
    cov = Table([[cover_p]], colWidths=[BW])
    cov.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),NAVY),
        ('TOPPADDING',(0,0),(-1,-1),35),('BOTTOMPADDING',(0,0),(-1,-1),35),
        ('LEFTPADDING',(0,0),(-1,-1),20),('RIGHTPADDING',(0,0),(-1,-1),20),
    ]))
    add(cov, sp(8))

    sub_p = Paragraph(
        'Concurso Praia Grande 001/2026 · IBAM · Médico de Família e Comunidade<br/>'
        'Baseado no Edital Oficial e Legislação Vigente — Atualizado mai/2026',
        S('cs', fontName='Helvetica', fontSize=10, leading=14, textColor=NAVY, alignment=1))
    add(sub_p, sp(10))

    # Sumário
    add(sec_hdr('SUMÁRIO'), sp(3))
    sumario = [
        ('1','CF/88 — Saúde como Direito Fundamental','3'),
        ('2','Lei 8.080/1990 — Lei Orgânica da Saúde','4'),
        ('3','Lei 8.142/1990 — Participação e Controle Social','6'),
        ('4','Decreto 7.508/2011 — Regulamentação da Lei 8.080','7'),
        ('5','LC 141/2012 — Financiamento','8'),
        ('6','PNAB 2017 — Política Nacional de Atenção Básica','9'),
        ('7','Financiamento SUS — Emenda 29/2000, EC 86/2015, EC 95/2016','11'),
        ('8','RAS — Redes de Atenção à Saúde','12'),
        ('9','Promoção da Saúde — Ottawa e PNPS 2014','13'),
        ('10','Determinantes Sociais da Saúde (DSS)','14'),
        ('11','Territorialização e Diagnóstico Situacional','15'),
        ('12','Vigilância em Saúde — Epidemiológica, Sanitária, Ambiental','16'),
        ('13','LNDC — Lei Nº 13.979/2020 e Emergências','18'),
        ('14','Sistemas de Informação em Saúde (SIS)','19'),
        ('15','Planejamento em Saúde — PNS, PMS, PPA','20'),
        ('16','HumanizaSUS — PNH 2004','21'),
        ('17','Políticas Específicas (PNSI, PNSM, PNCD, PNCT)','22'),
        ('18','PNI — Programa Nacional de Imunizações','23'),
        ('19','Macetes e Pegadinhas','25'),
        ('20','Questões de Revisão','30'),
        ('21','Checklist Final de Revisão','38'),
        ('22','Complemento — Gestão e Auditoria','39'),
    ]
    add(mk_tbl(['Nº','Tema','Pág.'], sumario, [30,380,72], hbg=NAVY), sp(4))
    add(PageBreak())

    # ── P2: CF/88 ───────────────────────────────────────────────────────────
    add(sec_hdr('1. CF/88 — SAÚDE COMO DIREITO FUNDAMENTAL'), sp(4))
    add(h2('Art. 196 a 200 — Seção II da CF/88'), sp(2))
    add(mk_tbl(
        ['Artigo','Dispositivo','Conteúdo Principal'],
        [
            ('Art. 196','Direito à Saúde','Saúde é direito de todos e dever do Estado; acesso universal e igualitário; promoção, proteção e recuperação'),
            ('Art. 197','Relevância Pública','Ações e serviços de saúde são de relevância pública; regulamentação, fiscalização e controle pelo Poder Público'),
            ('Art. 198','SUS','Sistema único com rede regionalizada e hierarquizada; descentralização; atendimento integral; participação da comunidade'),
            ('Art. 199','Setor Privado','Participação livre da iniciativa privada; vedada destinação de recursos públicos para auxílio a entidades lucrativas'),
            ('Art. 200','Competências do SUS','Controle e fiscalização; vigilância nutricional; formulação da política farmacêutica; ordenar a formação de RH; fiscalizar e inspecionar alimentos; colaborar na proteção do meio ambiente'),
        ],
        [60,110,312]
    ), sp(4))

    add(mac('Macete — Art. 198 CF/88: Três Diretrizes', [
        '→ Descentralização (com direção única em cada esfera)',
        '→ Atendimento integral (com prioridade para atividades preventivas)',
        '→ Participação da comunidade',
    ]), sp(3))

    add(peg('Pegadinha — Setor Privado (Art. 199)', [
        '→ A participação da iniciativa privada é LIVRE (complementar, não exclusiva)',
        '→ VEDADO: destinar recursos públicos para auxiliar entidades lucrativas',
        '→ Contratos e convênios são preferencialmente com entidades filantrópicas e sem fins lucrativos',
    ]), sp(4))
    add(PageBreak())

    # ── P3: Lei 8.080/1990 ──────────────────────────────────────────────────
    add(sec_hdr('2. LEI 8.080/1990 — LEI ORGÂNICA DA SAÚDE'), sp(4))
    add(mk_tbl(
        ['Tema','Artigos','Conteúdo'],
        [
            ('Objeto','Art. 1-2','Regula as ações e serviços de saúde; saúde como direito fundamental do ser humano'),
            ('Fatores Determinantes','Art. 3','Alimentação, moradia, saneamento, meio ambiente, trabalho, renda, educação, atividade física, transporte, lazer; acrescentado pela Lei 12.864/2013: atividade física'),
            ('Objetivos do SUS','Art. 5','Identificação e divulgação dos fatores condicionantes e determinantes; formulação de política de saúde; assistência às pessoas'),
            ('Atribuições do SUS','Art. 6','Vigilância epidemiológica; vigilância sanitária; saúde do trabalhador; assistência terapêutica; fiscalização de alimentos; formulação da política do medicamento; ordenação da formação de RH'),
            ('Princípios','Art. 7','Universalidade, integralidade, equidade; descentralização; regionalização; hierarquização; participação; conjugação de recursos; capacidade resolutiva; organização dos serviços'),
            ('Organização','Art. 8-10','Organização em distritos sanitários; consórcios administrativos intermunicipais; princípio da municipalização'),
            ('Direção do SUS','Art. 16-19','Ministério da Saúde (nacional); Secretarias Estaduais (estadual); Secretarias Municipais (municipal)'),
            ('Competências MS','Art. 16','Formular política nacional; participar da formulação dos planos; definir e coordenar políticas de saúde mental, hanseníase, tuberculose, DST, AIDS; normas e padrões'),
            ('Financiamento','Art. 31-34','Orçamentos da União, Estados, DF e Municípios; contribuições sociais; receitas próprias das instituições públicas'),
        ],
        [110,70,302]
    ), sp(3))

    add(atc('Atenção — Acréscimo Art. 3 pela Lei 12.864/2013', [
        '→ A prática de atividade física foi incluída como fator determinante e condicionante da saúde',
        '→ Banca frequentemente cita "a Lei 8.080 em sua redação original" — fique atento ao acréscimo de 2013',
    ]), sp(3))

    add(mk_tbl(
        ['Princípio','Definição'],
        [
            ('Universalidade','Garantia de atenção à saúde a todo e qualquer cidadão'),
            ('Integralidade','Assistência ao indivíduo de forma integral, com ações de promoção, proteção e recuperação'),
            ('Equidade','Priorizar quem mais precisa, reduzindo desigualdades; tratar desigualmente os desiguais'),
            ('Descentralização','Redistribuição de poder e recursos entre esferas de governo'),
            ('Regionalização','Organização dos serviços segundo regiões de saúde'),
            ('Hierarquização','Organização dos serviços em níveis de complexidade crescente'),
            ('Participação','Participação da comunidade (controle social)'),
            ('Conjugação de Recursos','União de recursos das três esferas de governo'),
            ('Capacidade Resolutiva','Serviços em todos os níveis de atenção devem ser capazes de resolver os problemas de saúde da população'),
            ('Organização','Organização dos serviços públicos de saúde'),
        ],
        [140,342]
    ), sp(4))
    add(PageBreak())

    # ── P4: Lei 8.142/1990 ──────────────────────────────────────────────────
    add(sec_hdr('3. LEI 8.142/1990 — PARTICIPAÇÃO E CONTROLE SOCIAL'), sp(4))
    add(mk_tbl(
        ['Instância','Composição','Reunião/Quórum','Função Principal'],
        [
            ('Conferência de Saúde','Representantes do governo, prestadores, profissionais e usuários (paritária: 50% usuários)','A cada 4 anos (ou extraordinária)','Avaliar a situação de saúde e propor diretrizes para a política de saúde'),
            ('Conselho de Saúde','50% usuários, 25% trabalhadores, 25% governo+prestadores','Reunião mensal (mínimo)','Atuar na formulação de estratégias e no controle da execução; caráter permanente e deliberativo'),
        ],
        [95,148,108,131]
    ), sp(3))

    add(peg('Pegadinha — Conselho vs Conferência', [
        '→ Conselho: caráter PERMANENTE e DELIBERATIVO (decide, não apenas recomenda)',
        '→ Conferência: a cada 4 anos (não é permanente)',
        '→ Composição do Conselho: 50% usuários (não profissionais)',
        '→ Resolução do Conselho precisa ser HOMOLOGADA pelo chefe do poder executivo correspondente',
    ]), sp(3))

    add(mk_tbl(
        ['Tema','Dispositivo'],
        [
            ('Transferências Regulares','Municípios e Estados que não constituírem Fundos de Saúde, Conselhos e Planos perdem o direito ao repasse regular'),
            ('Fundo de Saúde','Conta especial; movimentada sob fiscalização dos respectivos Conselhos de Saúde'),
            ('Plano de Saúde','Base das atividades e programações de cada nível de direção do SUS; em sua elaboração consideradas as deliberações da Conferência de Saúde'),
            ('Relatório de Gestão','Instrumento de controle; apresentado ao Conselho de Saúde ao final de cada exercício'),
        ],
        [120,362]
    ), sp(4))
    add(PageBreak())

    # ── P5: Decreto 7.508/2011 ──────────────────────────────────────────────
    add(sec_hdr('4. DECRETO 7.508/2011 — REGULAMENTAÇÃO DA LEI 8.080'), sp(4))
    add(mk_tbl(
        ['Conceito','Definição'],
        [
            ('Região de Saúde','Espaço geográfico contínuo constituído por agrupamentos de Municípios limítrofes delimitados a partir de identidades culturais, econômicas e sociais, de redes de comunicação e infraestrutura de transportes'),
            ('Contrato Organizativo da Ação Pública da Saúde (COAP)','Acordo de colaboração firmado entre entes federativos com a finalidade de organizar e integrar as ações e serviços de saúde na rede regionalizada e hierarquizada'),
            ('RENAME','Relação Nacional de Medicamentos Essenciais — referência para padronização da prescrição'),
            ('RENASES','Relação Nacional de Ações e Serviços de Saúde — define o conjunto de ações e serviços que o SUS oferece'),
            ('Portas de Entrada','APS, atenção de urgência, atenção psicossocial e especial de acesso aberto; acesso ao SUS dá-se preferencialmente pela APS'),
            ('Mapa da Saúde','Descrição geográfica da distribuição de recursos humanos e de ações e serviços de saúde ofertados pelo SUS e pela iniciativa privada'),
        ],
        [145,337]
    ), sp(3))

    add(atc('Atenção — Portas de Entrada SUS (Decreto 7.508)', [
        '→ APS é a PREFERENCIAL (não obrigatória para urgência/emergência)',
        '→ São quatro portas: APS · Urgência · Atenção Psicossocial · Especial de acesso aberto',
        '→ Serviços de apoio diagnóstico NÃO são portas de entrada',
    ]), sp(4))
    add(PageBreak())

    # ── P6: LC 141/2012 — Financiamento ─────────────────────────────────────
    add(sec_hdr('5. LC 141/2012 — FINANCIAMENTO DO SUS'), sp(4))
    add(mk_tbl(
        ['Esfera','Percentual Mínimo','Base de Cálculo'],
        [
            ('União','Valor apurado no ano anterior + variação nominal do PIB (EC 86); com EC 95/2016 (Teto de Gastos): reajuste pelo IPCA','Receita corrente líquida → substituída por regra de teto de gastos'),
            ('Estados','12% das receitas próprias','Arrecadação de impostos estaduais (inclui transferências constitucionais)'),
            ('Municípios','15% das receitas próprias','Arrecadação de impostos municipais (inclui transferências constitucionais)'),
            ('DF','12% e 15% (acumula)','Obrigações estaduais + municipais'),
        ],
        [110,175,197]
    ), sp(3))

    add(peg('Pegadinha — Percentuais de Financiamento', [
        '→ Estado: 12%; Município: 15% (lembrar: M de Municipal = mais = 15)',
        '→ Emenda Constitucional 29/2000: primeira norma a exigir percentuais mínimos',
        '→ LC 141/2012: regulamentou definitivamente os mínimos da EC 29',
        '→ EC 95/2016 (Teto de Gastos): congelou por 20 anos os gastos federais (reajuste pelo IPCA)',
        '→ O que NÃO conta como gasto em saúde: saneamento, merenda escolar, assistência social',
    ]), sp(3))

    add(mk_tbl(
        ['Transferência','Modalidade','Descrição'],
        [
            ('Fundo a Fundo','Regular e automática','Do Fundo Nacional para Fundos Estaduais e Municipais, sem convênio prévio'),
            ('Convênios','Específica','Para programas e projetos específicos; exige prestação de contas detalhada'),
            ('PAB Fixo','Per capita','Valor por habitante para custeio da APS; transferido mensalmente'),
            ('PAB Variável','Por adesão a programas','ESF, ACS, CEO, NASF — transferido conforme implantação'),
        ],
        [120,100,262]
    ), sp(4))
    add(PageBreak())

    # ── P7: PNAB 2017 ───────────────────────────────────────────────────────
    add(sec_hdr('6. PNAB 2017 — POLÍTICA NACIONAL DE ATENÇÃO BÁSICA'), sp(4))
    add(mk_tbl(
        ['Tema','Conteúdo'],
        [
            ('Conceito APS/AB','Conjunto de ações de saúde individuais, familiares e coletivas que envolvem promoção, prevenção, proteção, diagnóstico, tratamento, reabilitação, redução de danos, cuidados paliativos e vigilância em saúde'),
            ('Fundamentos','Territorialização; adscrição de clientela; continuidade do cuidado; coordenação do cuidado; longitudinalidade; integralidade; humanização; equidade; participação social'),
            ('ESF','Estratégia prioritária para expansão e consolidação da APS; equipe mínima: médico, enfermeiro, técnico/auxiliar de enfermagem e ACS'),
            ('Equipe mínima ESF','1 médico (MFC ou generalista) + 1 enfermeiro + 1 a 2 técnicos de enfermagem + 4 a 12 ACS'),
            ('Carga horária','40h semanais para médico e enfermeiro; ACS: 40h; população: até 4.000 pessoas por equipe'),
            ('NASF-AB','Amplia a abrangência, a resolutividade, a territorialização, a regionalização; equipes com pelo menos 5 profissionais de nível superior; não é porta de entrada'),
            ('Atribuições ACS','Visita domiciliar ≥ 1×/mês por família; cadastrar famílias; orientar; prevenir; acompanhar; articular ações sociais'),
            ('e-SUS APS','Sistema de informação; prontuário eletrônico; CDS ou PEC; base para financiamento do PAB variável'),
        ],
        [120,362]
    ), sp(3))

    add(atc('Atenção — PNAB 2017 vs PNAB 2012', [
        '→ PNAB 2017 extinguiu a obrigatoriedade do NASF como equipe padrão (passou a ser flexível)',
        '→ PNAB 2017 criou a possibilidade de eSF com 1 médico para populações menores',
        '→ Redução da cobertura mínima de ACS: não mais obrigatório 100% do território',
        '→ Banca ainda usa conceitos da PNAB 2012 — atenção ao enunciado',
    ]), sp(3))

    add(mk_tbl(
        ['Atributo (Starfield)','Definição Resumida'],
        [
            ('Acesso de primeiro contato','Porta de entrada preferencial; acessibilidade e uso a cada problema ou novo episódio'),
            ('Longitudinalidade','Vínculo continuado ao longo do tempo; responsabilização pela saúde das pessoas'),
            ('Integralidade','Atenção a todas as necessidades de saúde; encaminhamento quando necessário'),
            ('Coordenação do cuidado','Articulação entre os diferentes níveis; garantia da continuidade'),
            ('Focalização na família','Família como unidade de cuidado; contexto familiar considerado'),
            ('Orientação comunitária','Conhecimento das necessidades da comunidade; participação social'),
            ('Competência cultural','Respeito à diversidade cultural; adequação do cuidado à realidade local'),
        ],
        [145,337]
    ), sp(4))
    add(PageBreak())

    # ── P8: Financiamento Aprofundado ────────────────────────────────────────
    add(sec_hdr('7. FINANCIAMENTO SUS — EC 29, EC 86, EC 95, LC 141'), sp(4))
    add(mk_tbl(
        ['Norma','Ano','Principal Mudança'],
        [
            ('EC 29/2000','2000','Primeira emenda a exigir percentuais mínimos de gasto em saúde para todas as esferas; regulamentada pela LC 141/2012'),
            ('LC 141/2012','2012','Definiu critérios e base de cálculo dos gastos mínimos; definiu o que conta e o que não conta como despesa em saúde'),
            ('EC 86/2015','2015','Alterou o critério federal para percentual gradativo da Receita Corrente Líquida (chegando a 15% da RCL em 2020)'),
            ('EC 95/2016','2016','Teto dos gastos públicos federais por 20 anos (até 2036); reajuste apenas pelo IPCA; afeta investimentos em saúde'),
        ],
        [120,50,312]
    ), sp(3))

    add(mk_tbl(
        ['O que CONTA como despesa em saúde','O que NÃO conta como despesa em saúde'],
        [
            ('Ações e serviços de saúde (assistência, vigilância, promoção)','Saneamento básico (exceto controlado pelo MS)'),
            ('Remuneração dos profissionais de saúde em atividade no setor','Merenda escolar'),
            ('Pesquisa e desenvolvimento científico e tecnológico em saúde','Assistência social'),
            ('Produção, aquisição e distribuição de insumos para saúde','Pagamento de aposentadorias e pensões de profissionais de saúde'),
            ('Vigilância epidemiológica, sanitária e ambiental','Limpeza urbana e remoção de resíduos'),
        ],
        [241,241]
    ), sp(4))
    add(PageBreak())

    # ── P9: RAS ─────────────────────────────────────────────────────────────
    add(sec_hdr('8. RAS — REDES DE ATENÇÃO À SAÚDE (Portaria 4.279/2010)'), sp(4))
    add(p('As Redes de Atenção à Saúde são arranjos organizativos de ações e serviços de saúde, de diferentes densidades tecnológicas e missões, integrados através de sistemas de apoio técnico, logístico e de gestão, buscando garantir a integralidade do cuidado.'), sp(2))
    add(mk_tbl(
        ['Componente RAS','Descrição'],
        [
            ('Centro de Comunicação','APS é o centro de comunicação (não a ponta) — coordena e filtra o fluxo assistencial'),
            ('Pontos de Atenção','APS, Ambulatório Especializado, Urgência/Emergência, Hospitalar, Domiciliar'),
            ('Sistemas Logísticos','Cartão SUS, prontuário eletrônico, centrais de regulação, transporte sanitário'),
            ('Sistemas de Governança','Modelo de atenção, financiamento, gestão, organização, informação, trabalho e educação permanente'),
            ('Modelo de Atenção','Crônicas: Modelo de Atenção às Condições Crônicas (MACC); Agudas: RUE (Rede de Urgência e Emergência)'),
        ],
        [140,342]
    ), sp(3))

    add(mk_tbl(
        ['Rede Temática','Portaria/Decreto','Foco'],
        [
            ('Rede Cegonha','GM/MS 1.459/2011','Atenção ao pré-natal, parto, puerpério e criança até 24 meses'),
            ('RUE — Rede Urgência e Emergência','GM/MS 1.600/2011','SAMU, UPA 24h, sala de estabilização, UBS com atenção às urgências, hospitais'),
            ('Rede de Atenção Psicossocial (RAPS)','GM/MS 3.088/2011','CAPS, UBS, SAMU, leitos, hospitais gerais, consultório na rua'),
            ('Rede de Atenção à Saúde Bucal','GM/MS 874/2013','CEO, LRPD, Equipes de Saúde Bucal, USF'),
            ('Rede de Cuidado à Saúde da Pessoa com Deficiência','GM/MS 793/2012','CER, CPOD, Oficinas Ortopédicas'),
        ],
        [135,120,227]
    ), sp(4))
    add(PageBreak())

    # ── P10: Promoção da Saúde ──────────────────────────────────────────────
    add(sec_hdr('9. PROMOÇÃO DA SAÚDE — OTTAWA E PNPS 2014'), sp(4))
    add(mk_tbl(
        ['Carta de Ottawa (1986) — Cinco Eixos','Descrição'],
        [
            ('Elaboração e implementação de políticas públicas saudáveis','Saúde na pauta política; legislação protetora'),
            ('Criação de ambientes favoráveis à saúde','Ambiente físico e social como suporte à saúde'),
            ('Reforço da ação comunitária','Empoderamento das comunidades'),
            ('Desenvolvimento de habilidades pessoais','Educação para a saúde; habilidades para a vida'),
            ('Reorientação dos serviços de saúde','Serviços além da cura; responsabilidade compartilhada'),
        ],
        [200,282]
    ), sp(3))

    add(mk_tbl(
        ['PNPS 2014 — Temas Prioritários','Estratégia'],
        [
            ('Formação e Educação Permanente','Capacitação contínua dos profissionais de saúde'),
            ('Alimentação Adequada e Saudável','PNAE, rotulagem, regulação de alimentos ultraprocessados'),
            ('Práticas Corporais e Atividade Física','NASF, academia da saúde, PNUD'),
            ('Enfrentamento do Tabagismo','INCA, abordagem na APS, lei antifumo'),
            ('Enfrentamento do Álcool e outras Drogas','CAPS AD, políticas intersetoriais'),
            ('Mobilidade Urbana e Trânsito','Acidentes como problema de saúde pública'),
            ('Paz, Violência e Cultura da Paz','Prevenção da violência; cultura de paz'),
            ('Ambientes e Trabalho Saudáveis','RENAST, saúde do trabalhador integrada à APS'),
        ],
        [175,307]
    ), sp(4))
    add(PageBreak())

    # ── P11: DSS ─────────────────────────────────────────────────────────────
    add(sec_hdr('10. DETERMINANTES SOCIAIS DA SAÚDE (DSS)'), sp(4))
    add(mk_tbl(
        ['Modelo/Autor','Descrição'],
        [
            ('Dahlgren e Whitehead (1991)','Modelo "arco-íris": camadas dos determinantes — estilo de vida individual; redes sociais e comunitárias; condições de vida e trabalho; condições socioeconômicas, culturais e ambientais'),
            ('CSDH/OMS — Comissão Marmot','Determinantes estruturais (posição social, raça, gênero, renda, educação) geram determinantes intermediários (condições materiais, comportamentos, fatores psicossociais)'),
            ('CNDSS Brasil (2008)','Comissão Nacional sobre DSS — propôs três eixos: eixo iniquidades, eixo determinação e eixo intervenção'),
        ],
        [155,327]
    ), sp(3))

    add(mk_tbl(
        ['Tipo de Iniquidade','Definição'],
        [
            ('Iniquidades de saúde','Diferenças evitáveis, injustas e desnecessárias nas condições de saúde entre grupos populacionais'),
            ('Equidade horizontal','Igual tratamento para necessidades iguais'),
            ('Equidade vertical','Tratamento diferenciado para necessidades diferentes (priorizar quem mais precisa)'),
        ],
        [130,352]
    ), sp(3))

    add(atc('Atenção — DSS vs Fatores de Risco', [
        '→ DSS = condições em que as pessoas NASCEM, CRESCEM, VIVEM, TRABALHAM e ENVELHECEM',
        '→ Diferente de fatores de risco individuais (tabagismo, sedentarismo)',
        '→ Banca confunde os dois — DSS é o contexto estrutural e social',
    ]), sp(4))
    add(PageBreak())

    # ── P12: Territorialização ───────────────────────────────────────────────
    add(sec_hdr('11. TERRITORIALIZAÇÃO E DIAGNÓSTICO SITUACIONAL'), sp(4))
    add(mk_tbl(
        ['Conceito','Definição/Aplicação'],
        [
            ('Território','Espaço geográfico e social delimitado; não apenas limite geográfico mas dinâmica social, cultural e epidemiológica'),
            ('Microárea','Subdivisão do território da equipe; responsabilidade do ACS (mínimo 400, máximo 750 pessoas)'),
            ('Área de abrangência ESF','Até 4.000 pessoas por equipe (ideal 2.000 a 3.500); em áreas de alta vulnerabilidade: mínimo 400/ACS'),
            ('Diagnóstico Situacional','Levantamento das condições de saúde, estrutura da UBS, perfil epidemiológico; base para o planejamento em saúde local'),
            ('Mapa de vulnerabilidade','Instrumento de visualização das necessidades do território; orienta as visitas domiciliares prioritárias'),
        ],
        [130,352]
    ), sp(3))

    add(mk_tbl(
        ['Ferramenta','Uso na Territorialização'],
        [
            ('Cadastro familiar (e-SUS)','Levantamento de características socioeconômicas, sanitárias e de saúde de cada família'),
            ('Ficha A (antigo sistema)','Ficha de cadastro domiciliar — substituída pelo CDS/PEC no e-SUS'),
            ('Ficha de Visita Domiciliar','Registro das atividades do ACS por família'),
            ('SIAB/SISAB','Sistema de Informação da Atenção Básica — alimentado pelos dados do e-SUS'),
        ],
        [130,352]
    ), sp(4))
    add(PageBreak())

    # ── P13: Vigilância em Saúde ─────────────────────────────────────────────
    add(sec_hdr('12. VIGILÂNCIA EM SAÚDE — EPIDEMIOLÓGICA, SANITÁRIA E AMBIENTAL'), sp(4))
    add(mk_tbl(
        ['Tipo','Base Legal','Função Principal','Exemplos de Ações'],
        [
            ('Vigilância Epidemiológica','Lei 6.259/1975; Lei 8.080/1990 Art. 6','Monitorar a ocorrência de doenças e agravos; prevenir e controlar epidemias','SINAN; SINASC; SIM; investigação de surtos; notificação compulsória'),
            ('Vigilância Sanitária (VISA)','Lei 9.782/1999 (ANVISA)','Eliminar, diminuir ou prevenir riscos à saúde relacionados a produtos e serviços','Fiscalização de alimentos, medicamentos, cosméticos, estabelecimentos de saúde'),
            ('Vigilância em Saúde do Trabalhador (VISAT)','Lei 8.080 Art. 6; Decreto 7.602/2011','Promover e proteger a saúde dos trabalhadores; RENAST','Diagnóstico de LER/DORT, silicose, câncer ocupacional'),
            ('Vigilância Ambiental','SINVSA; PNVS','Identificar fatores do ambiente que interferem na saúde','Água para consumo humano, ar, solo, vetores, desastres naturais'),
            ('Vigilância Nutricional','SISVAN; PNAN','Monitorar estado nutricional da população','Anemia, desnutrição, obesidade, consumo alimentar'),
        ],
        [90,110,155,127]
    ), sp(3))

    add(mk_tbl(
        ['Sistema de Informação','Sigla','O que registra'],
        [
            ('Sistema de Informação de Agravos de Notificação','SINAN','Doenças de notificação compulsória; fichas de investigação epidemiológica'),
            ('Sistema de Informações sobre Nascidos Vivos','SINASC','Declarações de nascidos vivos; dados materno-infantis'),
            ('Sistema de Informações sobre Mortalidade','SIM','Declarações de óbito; causa básica de morte; mortalidade proporcional'),
            ('Sistema de Informação de Vigilância Alimentar e Nutricional','SISVAN','Estado nutricional de crianças, gestantes, adolescentes, adultos e idosos'),
            ('Sistema de Informação da Atenção Básica','SISAB/e-SUS','Produção das equipes de APS; indicadores do PMAQ/Previne Brasil'),
        ],
        [220,65,197]
    ), sp(3))

    add(peg('Pegadinhas — Vigilância', [
        '→ VISA (Vigilância Sanitária) ≠ Vigilância Epidemiológica — são sistemas diferentes',
        '→ A ANVISA foi criada pela Lei 9.782/1999 — não é uma lei orgânica do SUS',
        '→ O SINAN registra AGRAVOS DE NOTIFICAÇÃO — não todos os atendimentos',
        '→ O SIM usa a Declaração de Óbito (DO) — preenchida pelo médico',
    ]), sp(4))
    add(PageBreak())

    # ── P14: LNDC / Emergências ──────────────────────────────────────────────
    add(sec_hdr('13. LNDC — LEI 13.979/2020 E EMERGÊNCIAS EM SAÚDE PÚBLICA'), sp(4))
    add(mk_tbl(
        ['Tema','Conteúdo'],
        [
            ('Lei 13.979/2020','Dispõe sobre medidas para enfrentamento de emergência de saúde pública de importância internacional; disciplina: isolamento, quarentena, exames, vacinação compulsória'),
            ('Isolamento','Separação de pessoas doentes ou contaminadas; duração mínima necessária para eliminação do risco'),
            ('Quarentena','Restrição de atividades de pessoas que possam ter sido expostas, mas não apresentam sintomas'),
            ('Vacinação Compulsória','Poderá ser determinada por autoridade sanitária — exceção ao princípio da autonomia'),
            ('ESPIN','Emergência de Saúde Pública de Importância Nacional; declarada pelo Ministério da Saúde'),
            ('PHEIC/ESPII','Public Health Emergency of International Concern; declarada pela OMS'),
            ('RSI','Regulamento Sanitário Internacional (2005) — instrumento da OMS para governança de emergências globais'),
            ('Notificação Compulsória','Lista nacional de DANT (Doenças e Agravos de Notificação) atualizada pela ANVISA/SVS; inclui agravos de notificação imediata e semanal'),
        ],
        [120,362]
    ), sp(3))

    add(atc('Atenção — Quarentena vs Isolamento', [
        '→ Isolamento: pessoa DOENTE ou CONTAMINADA (confirmada)',
        '→ Quarentena: pessoa EXPOSTA mas ainda sem sintomas (suspeita)',
        '→ Banca troca os dois — lembre pelo contexto clínico',
    ]), sp(4))
    add(PageBreak())

    # ── P15: Sistemas de Informação ──────────────────────────────────────────
    add(sec_hdr('14. SISTEMAS DE INFORMAÇÃO EM SAÚDE (SIS)'), sp(4))
    add(mk_tbl(
        ['SIS','Gestão','Indicadores Gerados'],
        [
            ('SINAN','SVS/MS','Taxa de incidência, prevalência, mortalidade por doença notificável; oportunidade de investigação'),
            ('SIM','CGIAE/MS','Taxa de mortalidade geral, infantil, materna; mortalidade proporcional; YPLL'),
            ('SINASC','CGIAE/MS','Taxa de natalidade; baixo peso ao nascer; APGAR; prematuridade; cobertura de pré-natal'),
            ('SISVAN','DAB/MS','Prevalência de desnutrição, sobrepeso, obesidade; déficit de crescimento'),
            ('SISAB/e-SUS','DAB/MS','Cobertura ESF; produção por equipe; indicadores Previne Brasil'),
            ('SIHSUS','DRAC/MS','Internações hospitalares; AIH; procedimentos realizados; mortalidade hospitalar'),
            ('SIASUS','DRAC/MS','Procedimentos ambulatoriais do SUS; BPA; APAC'),
            ('CNES','DRAC/MS','Cadastro Nacional de Estabelecimentos de Saúde; leitos; equipamentos; profissionais'),
        ],
        [80,80,322]
    ), sp(3))

    add(mac('Macete — Principais SIS para prova', [
        '→ SIM → óbito → Declaração de Óbito (DO)',
        '→ SINASC → nascimento → Declaração de Nascido Vivo (DNV)',
        '→ SINAN → agravos notificáveis → Ficha de Notificação/Investigação',
        '→ SISAB/e-SUS → produção APS → prontuário eletrônico/CDS',
    ]), sp(4))
    add(PageBreak())

    # ── P16: Planejamento em Saúde ───────────────────────────────────────────
    add(sec_hdr('15. PLANEJAMENTO EM SAÚDE — PNS, PMS, PPA, RAG'), sp(4))
    add(mk_tbl(
        ['Instrumento','Esfera','Período','Conteúdo'],
        [
            ('PPA — Plano Plurianual','Todas','4 anos','Programas e ações governamentais de médio prazo; aprovado pelo Legislativo'),
            ('PNS — Plano Nacional de Saúde','Federal','4 anos','Objetivos, diretrizes e metas nacionais; elaborado pelo MS; aprovado pelo CNS'),
            ('PES — Plano Estadual de Saúde','Estadual','4 anos','Traduz o PNS para o contexto estadual; aprovado pelo CES'),
            ('PMS — Plano Municipal de Saúde','Municipal','4 anos','Traduz o PES para o contexto municipal; aprovado pelo CMS'),
            ('PAS — Programação Anual de Saúde','Todas','1 ano','Instrumento operativo do Plano de Saúde; detalha metas anuais'),
            ('RAG — Relatório Anual de Gestão','Todas','1 ano','Presta contas ao Conselho de Saúde; avalia o cumprimento do PAS'),
        ],
        [120,70,65,227]
    ), sp(3))

    add(peg('Pegadinha — Quem aprova o Plano de Saúde?', [
        '→ O Plano de Saúde é elaborado pelo gestor (Secretaria) e APROVADO pelo Conselho de Saúde correspondente',
        '→ O RAG é apresentado ao Conselho de Saúde — não ao Legislativo',
        '→ PPA é aprovado pelo Legislativo (Câmara/Assembleia/Congresso)',
    ]), sp(3))

    add(mk_tbl(
        ['Método/Ferramenta','Uso no Planejamento em Saúde'],
        [
            ('SWOT (FOFA)','Análise de Forças, Oportunidades, Fraquezas e Ameaças; diagnóstico estratégico'),
            ('PES — Planejamento Estratégico Situacional (Matus)','Momentos: explicativo, normativo, estratégico e tático-operacional'),
            ('Marco Lógico','Estrutura de objetivos, indicadores, meios de verificação e pressupostos'),
            ('Planilha de Priorização','Método de análise de vulnerabilidade + impacto para priorizar problemas de saúde'),
        ],
        [145,337]
    ), sp(4))
    add(PageBreak())

    # ── P17: HumanizaSUS ─────────────────────────────────────────────────────
    add(sec_hdr('16. HUMANIZASUS — POLÍTICA NACIONAL DE HUMANIZAÇÃO (PNH 2004)'), sp(4))
    add(mk_tbl(
        ['Princípio PNH','Descrição'],
        [
            ('Transversalidade','A humanização deve perpassar todas as políticas de saúde — não é programa isolado'),
            ('Indissociabilidade entre atenção e gestão','Quem cuida precisa ser cuidado; mudar práticas de gestão e atenção juntos'),
            ('Protagonismo, corresponsabilidade e autonomia dos sujeitos','Usuários, trabalhadores e gestores como coautores do processo de produção de saúde'),
        ],
        [145,337]
    ), sp(3))

    add(mk_tbl(
        ['Dispositivo HumanizaSUS','Onde se aplica','Função'],
        [
            ('Acolhimento','APS e todos os níveis','Receber, ouvir, responsabilizar-se; não é triagem, mas atitude'),
            ('Clínica Ampliada','APS e especializada','Ampliar o objeto de trabalho; considerar o sujeito; compartilhar saberes'),
            ('Projeto Terapêutico Singular (PTS)','Equipe multiprofissional','Conjunto de propostas articuladas para um sujeito específico'),
            ('Apoio Matricial (Matriciamento)','NASF-AB / CAPS','Suporte técnico e pedagógico de equipes especializadas à APS'),
            ('Equipe de Referência','Multiprofissional','Responsabiliza-se longitudinalmente pelo usuário'),
            ('Visita Aberta e Direito a Acompanhante','Hospital','Direito do paciente de ter acompanhante e visitas abertas'),
            ('Colegiado Gestor','Gestão','Gestão compartilhada; decisões coletivas'),
            ('Ouvidoria e GTE','Gestão e atenção','Grupo de Trabalho de Humanização; voz do usuário'),
        ],
        [145,100,237]
    ), sp(4))
    add(PageBreak())

    # ── P18: Políticas Específicas ───────────────────────────────────────────
    add(sec_hdr('17. POLÍTICAS ESPECÍFICAS — PNSI, PNSM, PNCD, PNCT, PNAB'), sp(4))
    add(mk_tbl(
        ['Política','Sigla','Foco Principal','Destaques para Prova'],
        [
            ('Política Nacional de Saúde Integral da População Negra','PNSIPN (2009)','Equidade racial na saúde; combate ao racismo institucional','Doença falciforme; hipertensão; acesso desigual'),
            ('Política Nacional de Saúde da Pessoa Idosa','PNSPI (2006)','Envelhecimento saudável; funcionalidade; cuidado integral','Avaliação Geriátrica Ampla (AGA); prevenção de quedas'),
            ('Política Nacional de Saúde Mental','PNSM / Lei 10.216/2001','Reforma Psiquiátrica; desinstitucionalização; RAPS','CAPS como dispositivo central; internação como último recurso'),
            ('Política Nacional de Controle do Diabetes','PNCD','Rastreamento; tratamento; automonitoramento','Metas glicêmicas; HbA1c; Previne Brasil'),
            ('Política Nacional de Controle do Tabagismo','PNCT / INCA','Abordagem mínima e intensiva; TRN; vareniclina','5As: Ask, Advise, Assess, Assist, Arrange'),
            ('Política Nacional de Alimentação e Nutrição','PNAN 2012','Alimentação adequada e saudável; SISVAN; PNAE','Marco de referência de educação alimentar e nutricional'),
            ('Política Nacional de Práticas Integrativas e Complementares','PNPIC 2006','Acupuntura, plantas medicinais, homeopatia, termalismo, meditação','Ampliada em 2017 e 2018 para 29 práticas'),
        ],
        [120,60,130,172]
    ), sp(4))
    add(PageBreak())

    # ── P19: PNI ─────────────────────────────────────────────────────────────
    add(sec_hdr('18. PNI — PROGRAMA NACIONAL DE IMUNIZAÇÕES'), sp(4))
    add(mk_tbl(
        ['Tema','Conteúdo'],
        [
            ('Base Legal','Lei 6.259/1975; Decreto 78.231/1976; Lei 8.080/1990 (Art. 6 — vigilância epidemiológica e sanitária); Lei 13.979/2020 (vacinação compulsória em emergência)'),
            ('Criação do PNI','1973 — antes da CF/88 e do SUS; Calendário Nacional de Vacinação atualizado anualmente pelo MS'),
            ('Calendário Atual','Criança, adolescente, adulto, idoso, gestante, indígena, trabalhadores de saúde; disponível no site do MS/CONASS'),
            ('Vacinação Compulsória','Crianças: obrigatória por lei (sanção: matrícula escolar negada); adultos: obrigatória em emergência epidemiológica'),
            ('Salas de Vacina','Estrutura mínima: geladeira exclusiva, termômetro, caderneta, EPI; rede de frio rigorosa'),
            ('Rede de Frio','Temperatura de conservação: +2°C a +8°C (maioria); algumas vacinas NÃO podem ser congeladas (ex: hepatite B, dupla adulto, anti-rábica)'),
            ('VIP vs VOP','VIP (inativada): substituiu VOP para crianças em 2016 (esquema 3 doses + reforços); VOP (oral) mantida em campanha'),
            ('BCG','Ao nascer (maternidade); dose única; contraindicada em imunodeprimidos graves'),
            ('Tríplice Viral (SCR)','2 doses; a 1ª aos 12 meses e 2ª aos 15 meses (junto à tetra viral/SCR + Varicela)'),
        ],
        [120,362]
    ), sp(3))

    add(peg('Pegadinha — PNI e Vacinação', [
        '→ VOP ("Sabin") está sendo substituída pela VIP ("Salk") no esquema básico — mas VOP ainda é usada em campanhas',
        '→ BCG: contraindicada para imunodeprimidos (HIV com CD4 <200, corticoterapia imunossupressora)',
        '→ Vacina da Influenza: anual; reformulada; grávidas, idosos, profissionais de saúde têm prioridade',
        '→ Hepatite B: 3 doses (0, 1, 6 meses); conservar em +2°C a +8°C; NÃO congelar',
    ]), sp(4))
    add(PageBreak())

    return S_
