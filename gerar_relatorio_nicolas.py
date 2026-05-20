from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import datetime

doc = Document()

# ── Margens ──────────────────────────────────────────────────────────────────
section = doc.sections[0]
section.top_margin    = Cm(2.5)
section.bottom_margin = Cm(2.5)
section.left_margin   = Cm(3)
section.right_margin  = Cm(2.5)

# ── Helpers ──────────────────────────────────────────────────────────────────
def set_font(run, size=11, bold=False, color=None, italic=False):
    run.bold   = bold
    run.italic = italic
    run.font.size = Pt(size)
    run.font.name = "Calibri"
    if color:
        run.font.color.rgb = RGBColor(*color)

def add_heading(doc, text, level=1, color=(0, 0, 0)):
    p = doc.add_heading(level=level)
    p.clear()
    run = p.add_run(text)
    set_font(run, size=14 if level == 1 else 12, bold=True, color=color)
    return p

def add_paragraph(doc, text="", bold=False, color=None, size=11, before=0, after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after  = Pt(after)
    if text:
        run = p.add_run(text)
        set_font(run, size=size, bold=bold, color=color)
    return p

def add_bullet(doc, text, bold_prefix=None, color=None):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(3)
    if bold_prefix:
        r1 = p.add_run(bold_prefix)
        set_font(r1, bold=True, color=color)
        r2 = p.add_run(text)
        set_font(r2, color=color)
    else:
        run = p.add_run(text)
        set_font(run, color=color)

def add_code_block(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(1)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(text)
    run.font.name = "Courier New"
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(30, 30, 30)
    # fundo cinza claro via shading
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), "F2F2F2")
    pPr.append(shd)
    return p

def add_divider(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after  = Pt(2)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "CCCCCC")
    pBdr.append(bottom)
    pPr.append(pBdr)

# ── CORES ────────────────────────────────────────────────────────────────────
VERMELHO   = (192, 0, 0)
LARANJA    = (197, 90, 17)
CINZA      = (89, 89, 89)
AZUL_TITULO = (31, 73, 125)
VERDE      = (56, 118, 29)
PRETO      = (0, 0, 0)

# ════════════════════════════════════════════════════════════════════════════
# CAPA / CABEÇALHO
# ════════════════════════════════════════════════════════════════════════════
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("REMMED TELEMEDICINA")
set_font(run, size=18, bold=True, color=AZUL_TITULO)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("Relatório de Bugs — Agente de Pagamento")
set_font(run, size=14, bold=True, color=PRETO)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
today = datetime.date.today().strftime("%d/%m/%Y")
run = p.add_run(f"Data: {today}  |  Para: Nicolas  |  Preparado por: Equipe Técnica")
set_font(run, size=10, color=CINZA)

add_divider(doc)
doc.add_paragraph()

# ════════════════════════════════════════════════════════════════════════════
# SUMÁRIO EXECUTIVO
# ════════════════════════════════════════════════════════════════════════════
add_heading(doc, "Sumário Executivo", level=1, color=AZUL_TITULO)
add_paragraph(doc,
    "Foram identificados bugs no fluxo de pagamento do agente de Renovação de Receitas, "
    "observados em duas conversas reais com pacientes. Os problemas afetam diretamente a "
    "conversão de pagamento: em um caso o link foi gerado mas não enviado ao paciente; em "
    "outro o paciente recebeu o link mas não conseguiu pagar. Além disso, o agente entrou "
    "em loop ao não saber tratar a ausência de resposta do paciente.",
    size=11, after=6)

# Tabela resumo
add_paragraph(doc, "Visão geral dos bugs:", bold=True, after=4)

table = doc.add_table(rows=1, cols=4)
table.style = "Table Grid"
table.alignment = WD_TABLE_ALIGNMENT.CENTER

hdr = table.rows[0].cells
headers = ["#", "Severidade", "Descrição", "Origem"]
for i, h in enumerate(headers):
    hdr[i].text = h
    run = hdr[i].paragraphs[0].runs[0]
    set_font(run, bold=True, size=10)
    hdr[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

rows_data = [
    ("1", "🔴 CRÍTICO",  "Link de pagamento gerado mas não enviado",          "Prompt Renovação"),
    ("2", "🟡 MÉDIO",    "Endereço em múltiplas mensagens quebra fluxo",       "Prompt Renovação"),
    ("3", "🟡 MÉDIO",    "Mensagens simultâneas causam resposta duplicada",    "N8N / Concorrência"),
    ("4", "🟢 BAIXO",    "Paciente com link não conseguiu pagar (Conversa Silvio)", "Asaas / Externo"),
]
for num, sev, desc, orig in rows_data:
    row = table.add_row().cells
    row[0].text = num
    row[1].text = sev
    row[2].text = desc
    row[3].text = orig
    for cell in row:
        cell.paragraphs[0].paragraph_format.space_after = Pt(3)

doc.add_paragraph()
add_divider(doc)
doc.add_paragraph()

# ════════════════════════════════════════════════════════════════════════════
# SEÇÃO 1 — CONVERSA SAMUEL (detalhes dos bugs)
# ════════════════════════════════════════════════════════════════════════════
add_heading(doc, "1. Detalhes dos Bugs — Conversa com Samuel", level=1, color=AZUL_TITULO)
add_paragraph(doc,
    "Todos os três bugs abaixo foram observados na mesma conversa, em sequência, o que "
    "resultou no paciente não conseguindo finalizar o pagamento.",
    size=11, after=8)

# ── Bug 1 ─────────────────────────────────────────────────────────────────
add_heading(doc, "Bug 1 — Pergunta de pagamento repetida", level=2, color=VERMELHO)

add_paragraph(doc, "O que aconteceu:", bold=True, after=2)
add_paragraph(doc,
    "O paciente Samuel enviou seu endereço em 4 mensagens separadas (CEP, rua, cidade, "
    "estado). Cada mensagem disparou o agente individualmente. Na última mensagem "
    "(\"Df\" — sigla do Distrito Federal), o agente avançou o setor e perguntou a forma "
    "de pagamento. Quando Samuel respondeu \"1\" (PIX), o agente processou mas não "
    "reconheceu o \"1\" como seleção válida e repetiu a pergunta de pagamento.",
    size=11, after=6)

add_paragraph(doc, "Causa técnica:", bold=True, after=2)
add_paragraph(doc,
    "O prompt do agente de Renovação aguarda o endereço em uma única resposta e "
    "imediatamente avança o setor para pagamento. Quando o endereço chega em múltiplas "
    "mensagens, cada mensagem cria uma execução do agente, e o estado interno fica "
    "inconsistente entre as execuções. O agente pode avançar o setor com dados incompletos "
    "e perder o contexto de que a resposta seguinte (\"1\") é a escolha de pagamento.",
    size=11, after=6)

add_paragraph(doc, "Fix no prompt:", bold=True, after=2)
add_paragraph(doc,
    "Instruir o agente a verificar se CEP e cidade estão presentes na mensagem antes de "
    "avançar o setor. Se incompleto, pedir o endereço completo em uma única mensagem:",
    size=11, after=3)
add_code_block(doc,
    '🔴 Verificar se a mensagem contém CEP e cidade/endereço completo.\n'
    '🔴 Se faltar CEP ou endereço → NÃO avançar setor. Pedir:\n'
    '"Preciso do endereço completo numa única mensagem 😊\n'
    'Exemplo: Rua das Flores, 100, Bairro Centro, São Paulo/SP, CEP 01310-000"\n'
    '🔴 Somente quando CEP e cidade estiverem presentes → salvar e avançar.'
)

doc.add_paragraph()

# ── Bug 2 ─────────────────────────────────────────────────────────────────
add_heading(doc, "Bug 2 — Link de pagamento não foi enviado", level=2, color=VERMELHO)

add_paragraph(doc, "O que aconteceu:", bold=True, after=2)
add_paragraph(doc,
    "Após Samuel enviar \"1\" pela segunda vez, o agente respondeu: \"Seu link de "
    "pagamento já foi gerado!\" — mas não incluiu o URL do link. O agente chamou a tool "
    "gerar_cobranca_direta (e ela executou com sucesso), porém o retorno com a URL não "
    "foi incluído na mensagem enviada ao paciente.",
    size=11, after=6)

add_paragraph(doc, "Causa técnica:", bold=True, after=2)
add_paragraph(doc,
    "O prompt instrui o agente a aguardar o retorno de gerar_cobranca_direta, mas não "
    "instrui a extrair e incluir o link/URL do retorno no output final. O agente apenas "
    "confirma que o pagamento foi gerado, sem enviar o link.",
    size=11, after=6)

add_paragraph(doc, "Fix no prompt (aplicar nas 3 seções de pagamento):", bold=True, after=2)
add_paragraph(doc,
    "Antes do output final, adicionar instrução para extrair o link do retorno da tool "
    "e incluí-lo na mensagem:",
    size=11, after=3)
add_code_block(doc,
    '⚡ Chame gerar_cobranca_direta com:\n'
    '  valor           = 79.90\n'
    '  descricao       = "renovacao_receita_[NOME_MEDICAMENTO]"\n'
    '  forma_pagamento = FORMA_PAGAMENTO\n\n'
    '🔴 Aguardar retorno da tool ANTES de qualquer output.\n'
    '🔴 Extrair o campo de link/URL do retorno → salvar como LINK_PAGAMENTO.\n'
    '🔴 Erro → repetir uma vez. Segunda falha → escalar_humano.\n\n'
    '⚡ Chame atualizar_setor com setor = "ENCERRADO"\n'
    'Output:\n'
    '"Pagamento gerado! 😊\n\n'
    '🔗 [LINK_PAGAMENTO]\n\n'
    'Assim que confirmado, o médico irá realizar a renovação da sua receita.\n'
    'Você receberá sua nova receita por aqui em breve. 🧡"'
)

add_paragraph(doc,
    "⚠️ Ação necessária: confirmar com Nicolas o nome exato do campo retornado por "
    "gerar_cobranca_direta (ex: link, url, payment_url, invoiceUrl).",
    size=10, color=LARANJA, after=6)

doc.add_paragraph()

# ── Bug 3 ─────────────────────────────────────────────────────────────────
add_heading(doc, "Bug 3 — Mesma mensagem repetida 3 vezes em loop", level=2, color=LARANJA)

add_paragraph(doc, "O que aconteceu:", bold=True, after=2)
add_paragraph(doc,
    "Sem receber o link de pagamento, Samuel ficou sem ação e enviou \"?\". O agente não "
    "soube interpretar e repetiu a última mensagem 3 vezes em sequência.",
    size=11, after=6)

add_paragraph(doc, "Causa técnica:", bold=True, after=2)
add_paragraph(doc,
    "Há dois fatores combinados: (1) o prompt não instrui como tratar símbolos isolados "
    "sem conteúdo (\"?\", \".\") quando o agente está aguardando seleção de pagamento; "
    "(2) o N8N não possui controle de concorrência por paciente — se o paciente enviar "
    "múltiplas mensagens rapidamente, múltiplas execuções do agente são disparadas "
    "simultaneamente e todas produzem o mesmo output.",
    size=11, after=6)

add_paragraph(doc, "Fix no prompt (paliativo):", bold=True, after=2)
add_code_block(doc,
    '🔴 Se resposta inválida for apenas símbolo ("?", ".", "!") sem número:\n'
    '   → Tratar como tentativa inválida.\n'
    '   → Contar no limite de tentativas.\n'
    '   → NÃO repetir a pergunta mais de uma vez por turno.\n'
    '   → Na 2ª tentativa inválida → escalar_humano.'
)
add_paragraph(doc, "Fix definitivo (N8N):", bold=True, after=2)
add_paragraph(doc,
    "Implementar lock/mutex por número de telefone no N8N para evitar execuções paralelas "
    "do mesmo paciente. Esta é uma configuração de infraestrutura, não de prompt.",
    size=11, after=6)

add_divider(doc)
doc.add_paragraph()

# ════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2 — CONVERSA SILVIO
# ════════════════════════════════════════════════════════════════════════════
add_heading(doc, "2. Detalhes — Conversa com Silvio", level=1, color=AZUL_TITULO)

add_paragraph(doc, "O que aconteceu:", bold=True, after=2)
add_paragraph(doc,
    "O link de pagamento foi gerado e enviado corretamente para Silvio "
    "(https://www.asaas.com/i/f5tkup3eeamnz4dp). O paciente tentou pagar mas não conseguiu.",
    size=11, after=6)

add_paragraph(doc, "Possíveis causas:", bold=True, after=2)
add_bullet(doc, "O link Asaas expira em 10 minutos após a geração. Se o paciente demorou para clicar, o link pode ter expirado.", bold_prefix="Expiração do link: ")
add_bullet(doc, "O cartão ou chave Pix pode ter sido recusado pelo banco do paciente.", bold_prefix="Recusa bancária: ")
add_bullet(doc, "Falha temporária na plataforma Asaas no momento do pagamento.", bold_prefix="Falha Asaas: ")

doc.add_paragraph()
add_paragraph(doc, "Ação recomendada:", bold=True, after=2)
add_bullet(doc, "Verificar no painel Asaas se a cobrança foi criada e qual status retornou.")
add_bullet(doc, "Confirmar com o Nicolas se o tempo de expiração pode ser aumentado ou se há opção de reenvio automático do link.")
add_bullet(doc, "Não é bug de prompt — o agente funcionou corretamente neste caso.")

add_divider(doc)
doc.add_paragraph()

# ════════════════════════════════════════════════════════════════════════════
# SEÇÃO 3 — PLANO DE AÇÃO
# ════════════════════════════════════════════════════════════════════════════
add_heading(doc, "3. Plano de Ação", level=1, color=AZUL_TITULO)

table2 = doc.add_table(rows=1, cols=5)
table2.style = "Table Grid"
table2.alignment = WD_TABLE_ALIGNMENT.CENTER

hdr2 = table2.rows[0].cells
headers2 = ["#", "Ação", "Tipo", "Prioridade", "Responsável"]
for i, h in enumerate(headers2):
    hdr2[i].text = h
    run = hdr2[i].paragraphs[0].runs[0]
    set_font(run, bold=True, size=10)
    hdr2[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

acoes = [
    ("1", "Confirmar nome do campo URL retornado por gerar_cobranca_direta",     "Técnica",  "🔴 Urgente",    "Nicolas"),
    ("2", "Incluir [LINK_PAGAMENTO] no output dos 3 blocos de pagamento",         "Prompt",   "🔴 Urgente",    "Equipe Prompt"),
    ("3", "Adicionar validação de CEP+cidade antes de avançar setor de endereço","Prompt",   "🟡 Alta",       "Equipe Prompt"),
    ("4", "Adicionar tratamento de símbolo isolado ('?') no pagamento",           "Prompt",   "🟡 Alta",       "Equipe Prompt"),
    ("5", "Implementar lock/mutex por telefone no N8N",                           "N8N",      "🟡 Alta",       "Nicolas / Dev"),
    ("6", "Verificar tempo de expiração dos links Asaas",                         "Asaas",    "🟢 Normal",     "Nicolas"),
    ("7", "Testar fluxo completo de renovação com endereço em 1 mensagem",        "QA",       "🟢 Normal",     "Equipe Teste"),
]
for num, acao, tipo, prio, resp in acoes:
    row2 = table2.add_row().cells
    data = [num, acao, tipo, prio, resp]
    for i, val in enumerate(data):
        row2[i].text = val
        row2[i].paragraphs[0].paragraph_format.space_after = Pt(3)

doc.add_paragraph()
add_divider(doc)
doc.add_paragraph()

# ════════════════════════════════════════════════════════════════════════════
# RODAPÉ
# ════════════════════════════════════════════════════════════════════════════
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run(
    "Este documento é interno e confidencial — REMMED Telemedicina  |  "
    f"Gerado em {today}"
)
set_font(run, size=9, color=CINZA, italic=True)

# ── Salvar ───────────────────────────────────────────────────────────────
path = "/home/user/clara-/Bugs_Pagamento_Nicolas.docx"
doc.save(path)
print(f"Documento salvo em: {path}")
