"""Módulo 1 SUS — pages 20-48 content builder."""
import sys; sys.path.insert(0, '/home/user/clara-')
from pdf_helpers import *
from reportlab.platypus import PageBreak, KeepTogether
_S = S

def pages_20_to_48():
    S_ = []
    def add(*items):
        for x in items:
            if isinstance(x, list): S_.extend(x)
            else: S_.append(x)

    # ── P20: Macetes e Pegadinhas ────────────────────────────────────────────
    add(sec_hdr('19. MACETES E PEGADINHAS — SUS'), sp(4))

    add(mac('Macete — As 3 Leis Fundamentais do SUS', [
        '→ CF/88 Arts. 196-200: base constitucional',
        '→ Lei 8.080/1990: organização, princípios, diretrizes do SUS',
        '→ Lei 8.142/1990: controle social (conselhos e conferências)',
        '→ Decreto 7.508/2011: regulamenta a Lei 8.080 (COAP, RENASES, RENAME, portas de entrada)',
    ]), sp(3))

    add(mac('Macete — Princípios Doutrinários vs Organizativos', [
        '→ DOUTRINÁRIOS (UV Integral): Universalidade · eqUidade · Integralidade',
        '→ ORGANIZATIVOS: Descentralização · Regionalização · Hierarquização · Participação',
        '→ Banca chama de "diretrizes" a descentralização, integralidade e participação (Art. 198 CF/88)',
    ]), sp(3))

    add(mac('Macete — Conselhos de Saúde (Lei 8.142)', [
        '→ 50% USUÁRIOS (maioria) · 25% trabalhadores · 25% governo + prestadores',
        '→ PERMANENTE e DELIBERATIVO (não apenas consultivo)',
        '→ Resolução: deve ser HOMOLOGADA pelo chefe do executivo',
        '→ Reunião: ordinária mensal (mínimo)',
    ]), sp(3))

    add(mac('Macete — Financiamento (LC 141/2012)', [
        '→ Estado: 12% · Município: 15% (M de Municipal = maior = 15)',
        '→ EC 29/2000 criou; LC 141/2012 regulamentou',
        '→ EC 95/2016: teto de gastos por 20 anos → reajuste pelo IPCA',
        '→ Não conta: saneamento, merenda, assistência social, aposentadorias',
    ]), sp(3))

    add(mac('Macete — RENASES vs RENAME', [
        '→ RENASES = Relação de AÇÕES E SERVIÇOS (o que o SUS oferece)',
        '→ RENAME = Relação de MEDICAMENTOS Essenciais (o que o SUS dispensa)',
        '→ Ambas definidas no Decreto 7.508/2011',
    ]), sp(3))

    add(mac('Macete — Sistemas de Informação', [
        '→ SIM → óbito (Declaração de Óbito)',
        '→ SINASC → nascimento (Declaração de Nascido Vivo)',
        '→ SINAN → agravos notificáveis (Ficha de Notificação)',
        '→ SISAB/e-SUS → produção APS',
        '→ CNES → cadastro de estabelecimentos e profissionais',
    ]), sp(3))

    add(mac('Macete — Ottawa (1986): 5 Eixos', [
        '→ 1. Políticas públicas saudáveis',
        '→ 2. Ambientes favoráveis',
        '→ 3. Ação comunitária',
        '→ 4. Habilidades pessoais',
        '→ 5. Reorientação dos serviços',
        '→ Lembrar: "PA ACH RE" → Políticas · Ambientes · Ação · Competências · Habilidades · Reorientação',
    ]), sp(3))

    add(mac('Macete — HumanizaSUS (PNH 2004)', [
        '→ 3 princípios: Transversalidade · Indissociabilidade atenção/gestão · Protagonismo/autonomia',
        '→ Acolhimento ≠ triagem: é atitude, não procedimento',
        '→ Apoio Matricial = matriciamento = NASF apoia ESF',
        '→ PTS = Projeto Terapêutico Singular (para casos complexos)',
    ]), sp(4))
    add(PageBreak())

    # ── P21: Pegadinhas ──────────────────────────────────────────────────────
    add(sec_hdr('PEGADINHAS CLÁSSICAS — SUS (25 Questões Pega-Fácil)'), sp(4))

    pegs = [
        ('1','Saúde como DIREITO e DEVER',
         'A CF/88 diz que a saúde é direito de TODOS e dever do ESTADO (não apenas do governo federal). '
         'Banca frequentemente troca "dever do Estado" por "dever da União" — errado.'),
        ('2','Setor Privado no SUS',
         'A participação da iniciativa privada no SUS é COMPLEMENTAR e LIVRE — não é proibida. '
         'O que é vedado: destinar recursos públicos para entidades LUCRATIVAS (Art. 199, §2°, CF/88).'),
        ('3','Conferência de Saúde — periodicidade',
         'A cada 4 ANOS (não a cada 2). Pode ser convocada extraordinariamente. '
         'Não é permanente (ao contrário do Conselho de Saúde, que é permanente e deliberativo).'),
        ('4','Conselho de Saúde — composição',
         '50% USUÁRIOS (não profissionais, não gestores). '
         'Os outros 50%: 25% trabalhadores de saúde + 25% governo e prestadores de serviços.'),
        ('5','Art. 3 da Lei 8.080 — acréscimo',
         'A prática de ATIVIDADE FÍSICA foi incluída nos fatores determinantes pela Lei 12.864/2013. '
         'O texto original de 1990 não incluía atividade física.'),
        ('6','Portas de entrada do SUS (Decreto 7.508)',
         'São 4 portas: APS · Urgência · Atenção Psicossocial · Especial de acesso aberto. '
         'Serviços de apoio diagnóstico (laboratório, imagem) NÃO são portas de entrada.'),
        ('7','COAP — o que é',
         'Contrato Organizativo da Ação Pública da Saúde. '
         'Acordo entre ENTES FEDERATIVOS (não entre prestadores e gestor). Instrumento do Decreto 7.508.'),
        ('8','EC 29/2000 vs LC 141/2012',
         'EC 29 de 2000 CRIOU a obrigação dos percentuais mínimos. '
         'LC 141/2012 REGULAMENTOU e definiu os critérios detalhados. Banca testa a ordem cronológica.'),
        ('9','Percentuais: Estado 12%, Município 15%',
         'ESTADO: mínimo 12%. MUNICÍPIO: mínimo 15%. '
         '"M de Municipal = maior = 15%." DF aplica as duas obrigações simultaneamente.'),
        ('10','O que NÃO é gasto em saúde (LC 141)',
         'Saneamento básico, merenda escolar, assistência social e pagamento de aposentadorias '
         'de ex-profissionais de saúde NÃO contam como despesa em saúde para fins da LC 141.'),
        ('11','NASF — porta de entrada?',
         'NASF-AB NÃO é porta de entrada do SUS. '
         'Apoia as equipes de APS por meio do matriciamento. Não faz atendimento direto sem referência da ESF.'),
        ('12','ACS — vínculo empregatício',
         'O ACS deve residir na comunidade onde trabalha. '
         'Deve realizar ≥1 visita domiciliar por mês por família. '
         'NÃO precisa ser de nível superior (ensino médio é suficiente).'),
        ('13','Acolhimento ≠ triagem',
         'Acolhimento (HumanizaSUS/PNH) NÃO é triagem por ordem de chegada. '
         'É reconhecer as necessidades do usuário e responsabilizar-se. '
         'Pode ser feito por qualquer profissional de saúde.'),
        ('14','Apoio Matricial vs Referência e Contrarreferência',
         'Matriciamento = equipe especializada APOIA a APS sem substituir. '
         'Referência = encaminhamento para nível mais complexo. '
         'Contrarreferência = retorno ao nível anterior com relatório.'),
        ('15','Lei 10.216/2001 — Reforma Psiquiátrica',
         'Redireciona o modelo assistencial; prioriza tratamento em liberdade. '
         'A internação psiquiátrica deve ser ÚLTIMO RECURSO. '
         'CAPS é o dispositivo central da RAPS — não o hospital psiquiátrico.'),
        ('16','PNI — VOP substituída pela VIP',
         'Desde 2016, a VOP (oral, "Sabin") foi substituída pela VIP (inativada, "Salk") '
         'no esquema básico de criança. VOP ainda é usada em campanhas nacionais.'),
        ('17','Quarentena vs Isolamento (Lei 13.979/2020)',
         'Isolamento: para pessoa DOENTE/confirmada. '
         'Quarentena: para pessoa EXPOSTA mas sem sintomas. '
         'Banca frequentemente inverte os conceitos.'),
        ('18','SIM vs SINASC vs SINAN',
         'SIM → MORTALIDADE (Declaração de Óbito). '
         'SINASC → NASCIMENTOS (Declaração de Nascido Vivo). '
         'SINAN → AGRAVOS NOTIFICÁVEIS (Ficha de Notificação). Não confundir.'),
        ('19','RAG — quem apresenta e a quem',
         'O Relatório Anual de Gestão é apresentado pelo GESTOR ao CONSELHO DE SAÚDE '
         '(não ao Legislativo, não à Conferência). Prazo: ao final de cada exercício.'),
        ('20','Plano de Saúde — quem aprova',
         'O Plano de Saúde (PNS/PES/PMS) é elaborado pela Secretaria/Ministério '
         'e APROVADO pelo respectivo Conselho de Saúde. '
         'NÃO é aprovado pelo Legislativo (diferente do PPA).'),
        ('21','Equidade ≠ Igualdade',
         'Igualdade: tratar todos da mesma forma. '
         'Equidade: tratar desigualmente os desiguais — priorizar quem mais precisa. '
         'O SUS adota o princípio da EQUIDADE, não da igualdade pura.'),
        ('22','PNAB 2017 — NASF não é obrigatório',
         'A PNAB 2017 tornou o NASF OPCIONAL (não obrigatório). '
         'A PNAB 2012 exigia mínimo de profissionais. '
         'Banca usa enunciados sobre "equipe mínima da ESF" — NASF não integra a equipe mínima.'),
        ('23','Carta de Ottawa — local e ano',
         'Ottawa, CANADÁ, 1986. '
         'Não confundir com Alma-Ata (URSS, 1978) — que propôs "Saúde para todos até o ano 2000" '
         'e os Cuidados Primários de Saúde (CPS).'),
        ('24','Territorialização — número de famílias por ACS',
         'Cada ACS é responsável por 400 a 750 pessoas (não famílias). '
         'Equipe ESF: até 4.000 pessoas (ideal 2.000-3.500). '
         'Em área de alta vulnerabilidade: o mínimo por ACS pode ser 400 pessoas.'),
        ('25','Fundo de Saúde — quem fiscaliza',
         'O Fundo de Saúde é uma conta especial. '
         'A movimentação é feita pelo gestor, MAS sob fiscalização do CONSELHO DE SAÚDE. '
         'Não é fiscalizado pela Receita Federal diretamente.'),
    ]

    for num, titulo, exp in pegs:
        add(KeepTogether(ni(num, titulo, exp)))
        add(sp(2))

    add(PageBreak())

    # ── P22-27: Questões de Revisão ──────────────────────────────────────────
    add(sec_hdr('20. QUESTÕES DE REVISÃO — SUS'), sp(4))

    questoes = [
        ('Q1','Segundo a CF/88 (Art. 198), são diretrizes do SUS, EXCETO:',
         ['A) Descentralização, com direção única em cada esfera de governo',
          'B) Atendimento integral, com prioridade para atividades preventivas',
          'C) Participação da comunidade',
          'D) Universalidade de acesso em todos os níveis de assistência',
          'E) Descentralização e regionalização dos serviços'],
         'D',
         'As diretrizes do Art. 198 são: descentralização, atendimento integral e participação. '
         'Universalidade é princípio doutrinário (Art. 7, Lei 8.080), não diretriz constitucional do Art. 198.'),

        ('Q2','A Lei 8.142/1990 estabelece que os Conselhos de Saúde têm caráter:',
         ['A) Consultivo e temporário',
          'B) Deliberativo e permanente',
          'C) Fiscalizador e consultivo',
          'D) Normativo e provisório',
          'E) Legislativo e permanente'],
         'B',
         'Os Conselhos de Saúde são PERMANENTES e DELIBERATIVOS (tomam decisões vinculantes, não apenas '
         'recomendam). As resoluções devem ser homologadas pelo chefe do executivo.'),

        ('Q3','De acordo com a LC 141/2012, o percentual mínimo de aplicação em ações e serviços de saúde '
         'pelos Municípios é de:',
         ['A) 10%', 'B) 12%', 'C) 15%', 'D) 18%', 'E) 20%'],
         'C',
         'Municípios: 15%. Estados: 12%. "M de Municipal = Maior = 15%." '
         'União: segue regra da EC 86/95 (percentual da RCL ou teto pelo IPCA).'),

        ('Q4','O Decreto 7.508/2011 define como PORTAS DE ENTRADA preferencial do SUS:',
         ['A) A Atenção Primária à Saúde (APS)',
          'B) Os serviços de urgência e emergência',
          'C) Os ambulatórios de especialidades',
          'D) Os serviços de apoio diagnóstico e terapêutico',
          'E) Os hospitais de alta complexidade'],
         'A',
         'A APS é a PORTA PREFERENCIAL. As 4 portas são: APS, urgência, atenção psicossocial e especial '
         'de acesso aberto. Apoio diagnóstico NÃO é porta de entrada.'),

        ('Q5','Sobre o NASF-AB, segundo a PNAB 2017, é CORRETO afirmar:',
         ['A) É porta de entrada obrigatória do SUS',
          'B) Integra a equipe mínima da Estratégia Saúde da Família',
          'C) Amplia a resolutividade das equipes de APS por meio do apoio matricial',
          'D) Realiza atendimentos diretos sem necessidade de encaminhamento pela ESF',
          'E) É obrigatório em todos os municípios com ESF implantada'],
         'C',
         'NASF-AB faz apoio matricial (matriciamento) às equipes de APS — não é porta de entrada, '
         'não é obrigatório e não integra a equipe mínima da ESF.'),

        ('Q6','Qual dos seguintes NÃO é considerado gasto em saúde para fins da LC 141/2012?',
         ['A) Remuneração dos profissionais de saúde da rede pública',
          'B) Aquisição de medicamentos para a rede hospitalar',
          'C) Programas de saneamento básico municipal',
          'D) Ações de vigilância epidemiológica',
          'E) Campanhas de vacinação'],
         'C',
         'Saneamento básico NÃO conta como despesa em saúde para fins dos mínimos constitucionais. '
         'Também não contam: merenda escolar, assistência social, aposentadorias de ex-profissionais.'),

        ('Q7','A Carta de Ottawa (1986) identifica cinco campos de ação para a promoção da saúde. '
         'NÃO é um desses campos:',
         ['A) Criação de ambientes favoráveis à saúde',
          'B) Reforço da ação comunitária',
          'C) Reorientação dos serviços de saúde',
          'D) Controle de doenças crônicas não transmissíveis',
          'E) Elaboração de políticas públicas saudáveis'],
         'D',
         'Os 5 campos da Carta de Ottawa são: políticas saudáveis, ambientes favoráveis, ação comunitária, '
         'habilidades pessoais e reorientação dos serviços. "Controle de DCNT" não é um dos campos originais.'),

        ('Q8','Segundo a Lei 13.979/2020, a medida que restringe atividades de pessoas EXPOSTAS '
         'mas assintomáticas é denominada:',
         ['A) Isolamento', 'B) Quarentena', 'C) Internação compulsória',
          'D) Vigilância sanitária', 'E) Notificação compulsória'],
         'B',
         'Quarentena: pessoas EXPOSTAS (assintomáticas). '
         'Isolamento: pessoas DOENTES/contaminadas. Esta inversão é a pegadinha mais clássica do tema.'),

        ('Q9','Em relação à composição dos Conselhos de Saúde, é CORRETO afirmar que:',
         ['A) 50% são trabalhadores de saúde e 50% são usuários',
          'B) 25% são usuários, 25% são trabalhadores e 50% são gestores',
          'C) 50% são usuários, 25% são trabalhadores e 25% são governo e prestadores',
          'D) 33% são usuários, 33% trabalhadores e 33% governo',
          'E) A composição varia conforme legislação estadual ou municipal'],
         'C',
         '50% USUÁRIOS + 25% trabalhadores + 25% governo/prestadores. '
         'Isso garante a maioria dos usuários (paridade usuários vs restante).'),

        ('Q10','O Sistema de Informação que registra a MORTALIDADE da população brasileira, '
         'por meio da Declaração de Óbito, é:',
         ['A) SINAN', 'B) SINASC', 'C) SIM', 'D) SISAB', 'E) CNES'],
         'C',
         'SIM = Sistema de Informações sobre Mortalidade → Declaração de Óbito (DO). '
         'SINASC → nascimentos (DNV). SINAN → agravos notificáveis.'),

        ('Q11','Sobre o Apoio Matricial (Matriciamento), é CORRETO que:',
         ['A) Substitui o atendimento das equipes de APS por profissionais especializados',
          'B) É realizado exclusivamente por médicos especialistas',
          'C) Consiste no suporte técnico e pedagógico de equipes especializadas às equipes de APS',
          'D) Requer encaminhamento formal (referência) para cada caso',
          'E) É sinônimo de referência e contrarreferência'],
         'C',
         'Matriciamento = apoio técnico-pedagógico, não substituição. '
         'O NASF-AB realiza apoio matricial. A ESF mantém a responsabilidade pelo cuidado.'),

        ('Q12','Qual instrumento do planejamento em saúde detalha as metas ANUAIS e operacionaliza '
         'o Plano de Saúde?',
         ['A) Relatório Anual de Gestão (RAG)',
          'B) Programação Anual de Saúde (PAS)',
          'C) Plano Plurianual (PPA)',
          'D) Plano Nacional de Saúde (PNS)',
          'E) Plano Municipal de Saúde (PMS)'],
         'B',
         'PAS = Programação Anual de Saúde → instrumento operativo ANUAL do Plano de Saúde. '
         'RAG = presta contas do cumprimento do PAS ao final do exercício.'),

        ('Q13','A Política Nacional de Humanização (PNH/HumanizaSUS) tem como princípio fundante:',
         ['A) A hierarquização dos serviços de saúde',
          'B) A transversalidade, perpassando todas as políticas de saúde',
          'C) A especialização do cuidado por níveis de atenção',
          'D) A regionalização como eixo central de reorganização',
          'E) A informatização dos prontuários como ferramenta de humanização'],
         'B',
         'TRANSVERSALIDADE é o princípio fundante da PNH: a humanização deve perpassar '
         'todas as políticas de saúde, não ser um programa isolado.'),

        ('Q14','O COAP (Contrato Organizativo da Ação Pública da Saúde) é definido pelo Decreto 7.508/2011 '
         'como um acordo firmado entre:',
         ['A) Prestadores privados e gestores municipais',
          'B) Entes federativos (União, Estados, DF e Municípios)',
          'C) Hospitais públicos e Secretarias de Saúde',
          'D) Conselhos de Saúde e Ministério da Saúde',
          'E) Fundações públicas e autarquias de saúde'],
         'B',
         'COAP é acordo entre ENTES FEDERATIVOS para organizar as ações e serviços de saúde '
         'na rede regionalizada. Não é contrato com prestadores privados.'),

        ('Q15','Segundo a PNAB 2017, o número máximo de pessoas por equipe de Saúde da Família é:',
         ['A) 2.000', 'B) 3.000', 'C) 3.500', 'D) 4.000', 'E) 5.000'],
         'D',
         'Máximo: 4.000 pessoas por equipe ESF. Ideal: 2.000 a 3.500. '
         'Em área de alta vulnerabilidade: mínimo pode ser 400 pessoas por ACS.'),

        ('Q16','A Emenda Constitucional 29/2000 teve sua regulamentação complementada pela:',
         ['A) Lei 9.782/1999 (ANVISA)',
          'B) Lei 8.142/1990',
          'C) Lei Complementar 141/2012',
          'D) Decreto 7.508/2011',
          'E) EC 95/2016'],
         'C',
         'EC 29/2000 CRIOU os percentuais mínimos. LC 141/2012 os REGULAMENTOU em detalhes '
         '(base de cálculo, o que conta e não conta como gasto em saúde).'),

        ('Q17','Na Rede de Atenção à Saúde (RAS), a APS é descrita como:',
         ['A) Ponta da rede assistencial',
          'B) Centro de comunicação da rede',
          'C) Nível de maior densidade tecnológica',
          'D) Porta de saída do sistema',
          'E) Nível exclusivo de urgência e emergência'],
         'B',
         'APS é o CENTRO DE COMUNICAÇÃO da RAS (não a ponta). '
         'Ela coordena e filtra o fluxo assistencial para os demais pontos da rede.'),

        ('Q18','Qual das seguintes afirmativas sobre a Lei 8.080/1990 está INCORRETA?',
         ['A) Define os princípios e diretrizes do SUS',
          'B) Inclui a atividade física como fator determinante da saúde desde 1990',
          'C) Prevê a vigilância sanitária e epidemiológica como atribuições do SUS',
          'D) Estabelece que a direção do SUS é única em cada esfera de governo',
          'E) Define os objetivos do SUS, incluindo a assistência às pessoas'],
         'B',
         'INCORRETA: A atividade física foi incluída como fator determinante pela Lei 12.864/2013, '
         'não desde 1990. A Lei 8.080 original não previa atividade física no Art. 3.'),
    ]

    for q in questoes:
        add(KeepTogether(q_block(*q)))

    add(PageBreak())

    # ── P28: Checklist Final ─────────────────────────────────────────────────
    add(sec_hdr('21. CHECKLIST FINAL DE REVISÃO — SUS', bg=DK_GRN), sp(4))

    add(checklist('CF/88 — Arts. 196-200', [
        'Art. 196: saúde = direito de TODOS + dever do ESTADO',
        'Art. 198: diretrizes = descentralização + integralidade + participação',
        'Art. 199: setor privado = COMPLEMENTAR; vedado recurso público para entidade lucrativa',
        'Art. 200: atribuições do SUS (8 incisos)',
    ]), sp(3))

    add(checklist('Lei 8.080/1990', [
        'Art. 3: fatores determinantes incluem atividade física (acréscimo 2013)',
        'Art. 7: princípios doutrinários (universalidade, integralidade, equidade) + organizativos',
        'Art. 16: competências do Ministério da Saúde',
        'Direção única em cada esfera',
    ]), sp(3))

    add(checklist('Lei 8.142/1990', [
        'Conselho de Saúde: permanente, deliberativo, 50% usuários',
        'Conferência de Saúde: a cada 4 anos',
        'Transferências condicionadas: Fundo + Conselho + Plano',
        'RAG apresentado ao Conselho ao final de cada exercício',
    ]), sp(3))

    add(checklist('Decreto 7.508/2011', [
        'Região de Saúde: espaço geográfico contínuo',
        'COAP: acordo entre entes federativos',
        'RENASES: ações e serviços',
        'RENAME: medicamentos essenciais',
        '4 portas de entrada: APS (preferencial), urgência, psicossocial, especial',
    ]), sp(3))

    add(checklist('Financiamento (LC 141/2012)', [
        'Estado: 12%; Município: 15%; DF: ambos',
        'EC 29/2000 criou; LC 141 regulamentou',
        'EC 95/2016: teto de gastos 20 anos, reajuste IPCA',
        'Não conta: saneamento, merenda, assistência social, aposentadorias',
    ]), sp(3))

    add(checklist('Promoção da Saúde', [
        'Alma-Ata 1978: cuidados primários, "Saúde para todos até 2000"',
        'Ottawa 1986: 5 campos de ação (políticas, ambientes, comunidade, habilidades, serviços)',
        'PNPS 2014: 8 temas prioritários',
        'DSS: Dahlgren-Whitehead (arco-íris); CSDH/OMS (Marmot)',
    ]), sp(3))

    add(checklist('PNAB e Atenção Básica', [
        'ESF: equipe mínima = médico + enfermeiro + técnico + ACS',
        'Até 4.000 pessoas por equipe; ideal 2.000-3.500',
        'NASF: apoio matricial, não é porta de entrada, não é obrigatório (PNAB 2017)',
        'ACS: ≥1 visita/mês por família; mora na comunidade',
        'Atributos Starfield: 1° contato, longitudinalidade, integralidade, coordenação, família, comunidade, cultura',
    ]), sp(3))

    add(checklist('Sistemas de Informação', [
        'SIM → óbito (DO)',
        'SINASC → nascimento (DNV)',
        'SINAN → agravos notificáveis (Ficha de Notificação)',
        'SISAB/e-SUS → produção APS',
        'CNES → cadastro de estabelecimentos',
    ]), sp(3))

    add(checklist('HumanizaSUS (PNH 2004)', [
        '3 princípios: transversalidade, indissociabilidade atenção/gestão, protagonismo',
        'Acolhimento ≠ triagem; é atitude de qualquer profissional',
        'Apoio Matricial = NASF apoia ESF sem substituir',
        'PTS = Projeto Terapêutico Singular',
    ]), sp(4))

    add(PageBreak())

    # ── P29-30: Complemento — Gestão e Auditoria ─────────────────────────────
    add(sec_hdr('22. COMPLEMENTO — GESTÃO, REGULAÇÃO E AUDITORIA NO SUS'), sp(4))

    add(h2('Regulação no SUS'), sp(2))
    add(mk_tbl(
        ['Tipo de Regulação','Conceito','Exemplos'],
        [
            ('Regulação de Sistemas de Saúde','Controle, avaliação e auditoria; acreditação','DAF, DENASUS, TCU, CGU'),
            ('Regulação da Atenção à Saúde','Organização e controle da oferta de serviços; acesso','Centrais de regulação, SISREG, TFD'),
            ('Regulação Assistencial','Ordenação do acesso aos serviços; priorização por risco clínico','CROSS, regulação de leitos, SAMU'),
        ],
        [130,175,177]
    ), sp(3))

    add(h2('Auditoria e Controle no SUS'), sp(2))
    add(mk_tbl(
        ['Instância','Sigla','Função'],
        [
            ('Departamento Nacional de Auditoria do SUS','DENASUS','Auditoria das ações e serviços de saúde no âmbito federal'),
            ('Componente Estadual do SNA','CESAS','Auditoria estadual do SUS'),
            ('Componente Municipal do SNA','CESMU','Auditoria municipal do SUS'),
            ('Tribunal de Contas da União','TCU','Controle externo dos recursos federais da saúde'),
            ('Controladoria-Geral da União','CGU','Controle interno do Poder Executivo federal'),
            ('Ministério Público','MP','Fiscalização do cumprimento da legislação do SUS'),
        ],
        [165,70,247]
    ), sp(3))

    add(h2('Acreditação Hospitalar'), sp(2))
    add(mk_tbl(
        ['Nível','Denominação','Requisitos'],
        [
            ('Nível 1','Acreditado','Cumpre requisitos básicos de segurança e qualidade assistencial'),
            ('Nível 2','Acreditado Pleno','Cumpre requisitos + evidências de organização e incorpora gestão'),
            ('Nível 3','Acreditado com Excelência','Cumpre nível 2 + ciclos de melhoria contínua; benchmarking'),
        ],
        [70,130,282]
    ), sp(3))

    add(mac('Macete — DENASUS e Sistema Nacional de Auditoria', [
        '→ SNA = Sistema Nacional de Auditoria (Lei 8.080, Art. 17)',
        '→ 3 componentes: DENASUS (federal) + CESAS (estadual) + CESMU (municipal)',
        '→ Auditoria ≠ fiscalização: auditoria avalia a qualidade e eficiência; fiscalização verifica a conformidade legal',
    ]), sp(3))

    add(h2('Consórcios Públicos de Saúde'), sp(2))
    add(mk_tbl(
        ['Tema','Definição'],
        [
            ('Base Legal','Lei 11.107/2005; regulamentada pelo Decreto 6.017/2007'),
            ('Conceito','Pessoas jurídicas formadas exclusivamente por entes da federação para realização de objetivos de interesse comum'),
            ('Modalidades','Consórcio Público de Direito Público (associação pública) ou Direito Privado'),
            ('Uso em Saúde','Consórcios intermunicipais de saúde para oferta de serviços especializados, SAMU, diagnóstico por imagem, TFD'),
            ('Vantagem','Municípios pequenos compartilham serviços que sozinhos não conseguiriam manter'),
        ],
        [120,362]
    ), sp(4))

    return S_
