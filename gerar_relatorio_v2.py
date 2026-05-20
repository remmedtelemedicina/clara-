from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import datetime

doc = Document()

# ── Margens ──────────────────────────────────────────────────────────────────
section = doc.sections[0]
section.top_margin    = Cm(2)
section.bottom_margin = Cm(2)
section.left_margin   = Cm(2.5)
section.right_margin  = Cm(2.5)

# ── CORES ────────────────────────────────────────────────────────────────────
VERMELHO      = (192, 0, 0)
VERMELHO_BG   = "FFE5E5"
LARANJA       = (197, 90, 17)
LARANJA_BG    = "FFF3E0"
AMARELO_BG    = "FFFDE7"
VERDE         = (56, 118, 29)
VERDE_BG      = "E8F5E9"
AZUL          = (31, 73, 125)
AZUL_CLARO_BG = "E3EEF9"
CINZA         = (89, 89, 89)
CINZA_BG      = "F5F5F5"
CINZA_ESCURO  = (50, 50, 50)
BRANCO        = (255, 255, 255)
PRETO         = (0, 0, 0)

# Whatsapp chat colors
WA_PACIENTE_BG = "DCF8C6"   # verde claro
WA_AGENTE_BG   = "FFFFFF"   # branco
WA_BG          = "E5DDD5"   # fundo cinza bege

# ── Helpers ──────────────────────────────────────────────────────────────────
def set_font(run, size=11, bold=False, color=None, italic=False, name="Calibri"):
    run.bold   = bold
    run.italic = italic
    run.font.size = Pt(size)
    run.font.name = name
    if color:
        run.font.color.rgb = RGBColor(*color)

def cell_bg(cell, hex_color):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd  = OxmlElement("w:shd")
    shd.set(qn("w:val"),   "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"),  hex_color)
    tcPr.append(shd)

def para_bg(p, hex_color):
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"),   "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"),  hex_color)
    pPr.append(shd)

def set_cell_border(cell, top=None, bottom=None, left=None, right=None):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement("w:tcBorders")
    for side, val in [("top",top),("bottom",bottom),("left",left),("right",right)]:
        if val:
            b = OxmlElement(f"w:{side}")
            b.set(qn("w:val"),   val.get("val","single"))
            b.set(qn("w:sz"),    val.get("sz","4"))
            b.set(qn("w:space"), "0")
            b.set(qn("w:color"), val.get("color","auto"))
            tcBorders.append(b)
    tcPr.append(tcBorders)

def no_border(table):
    tbl  = table._tbl
    tblPr = tbl.tblPr
    tblBorders = OxmlElement("w:tblBorders")
    for side in ["top","left","bottom","right","insideH","insideV"]:
        b = OxmlElement(f"w:{side}")
        b.set(qn("w:val"), "none")
        tblBorders.append(b)
    tblPr.append(tblBorders)

def add_divider(doc, color="CCCCCC"):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after  = Pt(2)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bot = OxmlElement("w:bottom")
    bot.set(qn("w:val"),   "single")
    bot.set(qn("w:sz"),    "6")
    bot.set(qn("w:space"), "1")
    bot.set(qn("w:color"), color)
    pBdr.append(bot)
    pPr.append(pBdr)

def add_para(doc, text="", bold=False, color=None, size=11, before=0, after=4, align=None, italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after  = Pt(after)
    if align:
        p.alignment = align
    if text:
        run = p.add_run(text)
        set_font(run, size=size, bold=bold, color=color, italic=italic)
    return p

def add_heading_custom(doc, text, size=14, color=AZUL, before=8, after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after  = Pt(after)
    run = p.add_run(text)
    set_font(run, size=size, bold=True, color=color)
    return p

def colored_box(doc, lines, bg_hex, text_color=PRETO, size=10.5, border_color=None):
    """Single-cell table acting as a colored box."""
    tbl = doc.add_table(rows=1, cols=1)
    tbl.style = "Table Grid"
    cell = tbl.rows[0].cells[0]
    cell_bg(cell, bg_hex)
    cell.width = Inches(6)
    if border_color:
        brd = {"val":"single","sz":"6","color":border_color}
        set_cell_border(cell, top=brd, bottom=brd, left=brd, right=brd)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after  = Pt(4)
    for i, line in enumerate(lines):
        if i == 0:
            run = p.add_run(line)
        else:
            run = p.add_run("\n" + line)
        set_font(run, size=size, color=text_color)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

# ── Chat bubble simulator ─────────────────────────────────────────────────────
def chat_table(doc, messages):
    """
    messages = list of (sender, text, is_bug)
    sender: "paciente" | "agente"
    is_bug: bool — highlight in red
    """
    # outer wrapper table with WA background
    outer = doc.add_table(rows=1, cols=1)
    outer.style = "Table Grid"
    outer_cell = outer.rows[0].cells[0]
    cell_bg(outer_cell, WA_BG)
    set_cell_border(outer_cell,
        top={"val":"single","sz":"4","color":"BBBBBB"},
        bottom={"val":"single","sz":"4","color":"BBBBBB"},
        left={"val":"single","sz":"4","color":"BBBBBB"},
        right={"val":"single","sz":"4","color":"BBBBBB"})

    for sender, text, is_bug in messages:
        p = outer_cell.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after  = Pt(2)
        p.paragraph_format.left_indent  = Cm(0) if sender == "paciente" else Cm(1.5)
        p.paragraph_format.right_indent = Cm(1.5) if sender == "paciente" else Cm(0)

        if is_bug:
            bg = "FF8A80"  # vermelho claro
            lbl = "🔴 "
        elif sender == "paciente":
            bg  = WA_PACIENTE_BG
            lbl = "👤 "
        else:
            bg  = WA_AGENTE_BG
            lbl = "🤖 "

        # label
        r1 = p.add_run(lbl + ("Paciente" if sender == "paciente" else "Agente Clara"))
        set_font(r1, size=8, bold=True, color=CINZA)
        r2 = p.add_run("\n" + text)
        set_font(r2, size=9.5, color=CINZA_ESCURO)
        para_bg(p, bg)

    # remove first empty paragraph
    if outer_cell.paragraphs and not outer_cell.paragraphs[0].text:
        p = outer_cell.paragraphs[0]._element
        p.getparent().remove(p)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def severity_badge(doc, level, text):
    """Inline severity indicator."""
    colors = {
        "CRÍTICO": ("🔴 CRÍTICO", VERMELHO, VERMELHO_BG, "FF0000"),
        "MÉDIO":   ("🟡 MÉDIO",   LARANJA,  LARANJA_BG,  "FFA000"),
        "BAIXO":   ("🟢 BAIXO",   VERDE,    VERDE_BG,    "388E3C"),
    }
    lbl, tc, bg, bc = colors[level]
    tbl = doc.add_table(rows=1, cols=2)
    tbl.style = "Table Grid"
    no_border(tbl)
    # badge cell
    c1 = tbl.rows[0].cells[0]
    c1.width = Cm(3.2)
    cell_bg(c1, bg)
    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p1.add_run(lbl)
    set_font(r1, size=9, bold=True, color=tc)
    # text cell
    c2 = tbl.rows[0].cells[1]
    cell_bg(c2, "F8F8F8")
    p2 = c2.paragraphs[0]
    r2 = p2.add_run(text)
    set_font(r2, size=10, bold=True, color=PRETO)
    doc.add_paragraph().paragraph_format.space_after = Pt(3)

# ════════════════════════════════════════════════════════════════════════════
# DOCUMENTO
# ════════════════════════════════════════════════════════════════════════════

today = datetime.date.today().strftime("%d/%m/%Y")

# ── CAPA ─────────────────────────────────────────────────────────────────────
# Faixa de topo azul
topo = doc.add_table(rows=1, cols=1)
topo.style = "Table Grid"
topo_cell = topo.rows[0].cells[0]
cell_bg(topo_cell, "1F497D")
set_cell_border(topo_cell,
    top={"val":"none"}, bottom={"val":"none"},
    left={"val":"none"}, right={"val":"none"})

p = topo_cell.paragraphs[0]
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(10)
p.paragraph_format.space_after  = Pt(4)
r = p.add_run("REMMED TELEMEDICINA")
set_font(r, size=20, bold=True, color=BRANCO)

p2 = topo_cell.add_paragraph()
p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p2.paragraph_format.space_after = Pt(10)
r2 = p2.add_run("Relatório Técnico de Bugs — Agente de Pagamento & Renovação")
set_font(r2, size=13, color=(200, 220, 255))

doc.add_paragraph().paragraph_format.space_after = Pt(4)

# Meta
meta_tbl = doc.add_table(rows=1, cols=3)
meta_tbl.style = "Table Grid"
no_border(meta_tbl)
meta_data = [
    ("📅 Data", today),
    ("👤 Para", "Nicolas"),
    ("✍️ Preparado por", "Equipe Técnica"),
]
for i, (lbl, val) in enumerate(meta_data):
    c = meta_tbl.rows[0].cells[i]
    cell_bg(c, AZUL_CLARO_BG)
    p = c.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    r1 = p.add_run(lbl + "\n")
    set_font(r1, size=8, color=CINZA)
    r2 = p.add_run(val)
    set_font(r2, size=11, bold=True, color=AZUL)

doc.add_paragraph()
add_divider(doc, "1F497D")

# ── SUMÁRIO EXECUTIVO ─────────────────────────────────────────────────────────
add_heading_custom(doc, "📋 Sumário Executivo", size=13, color=AZUL)
add_para(doc,
    "Foram identificados 6 bugs nos agentes de Renovação de Receitas e Solicitação de "
    "Exames da REMMED, observados em conversas reais com pacientes (Samuel e Silvio). "
    "Os problemas afetam diretamente a conversão de pagamento e a experiência do paciente. "
    "Este relatório apresenta cada bug com o trecho real da conversa, causa técnica e fix exato.",
    size=10.5, after=6)

# Tabela resumo
add_para(doc, "Visão geral:", bold=True, size=10, after=3)
resumo_tbl = doc.add_table(rows=7, cols=4)
resumo_tbl.style = "Table Grid"

headers = ["#", "Severidade", "Bug", "Onde"]
row0 = resumo_tbl.rows[0]
for i, h in enumerate(headers):
    cell_bg(row0.cells[i], "1F497D")
    p = row0.cells[i].paragraphs[0]
    r = p.add_run(h)
    set_font(r, size=9, bold=True, color=BRANCO)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

resumo_data = [
    ("1", "🔴 CRÍTICO",  "Link de pagamento gerado mas NÃO enviado",          "3 setores de pagamento"),
    ("2", "🟡 MÉDIO",    "Endereço em múltiplas mensagens → avança cedo",      "4 setores de endereço"),
    ("3", "🟡 MÉDIO",    "Ordem errada: output antes da tool",                 "ETAPA 2E opção 3"),
    ("4", "🟡 MÉDIO",    "Duas tools sem await entre elas",                    "ENDERECO → PAGAMENTO"),
    ("5", "🟡 MÉDIO",    "Mensagem repetida 3x (loop)",                        "N8N concorrência"),
    ("6", "🟢 BAIXO",    "Link enviado mas paciente não conseguiu pagar",       "Asaas / expiração"),
]
row_bgs = [VERMELHO_BG, LARANJA_BG, AMARELO_BG, AMARELO_BG, AMARELO_BG, VERDE_BG]
for idx, (num, sev, bug, onde) in enumerate(resumo_data):
    row = resumo_tbl.rows[idx+1]
    data = [num, sev, bug, onde]
    for j, val in enumerate(data):
        cell_bg(row.cells[j], row_bgs[idx])
        p = row.cells[j].paragraphs[0]
        r = p.add_run(val)
        set_font(r, size=9)
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)

doc.add_paragraph()
add_divider(doc)

# ════════════════════════════════════════════════════════════════════════════
# CONVERSA SAMUEL
# ════════════════════════════════════════════════════════════════════════════
add_heading_custom(doc, "🗣️ Conversa 1 — Samuel", size=13, color=AZUL)
add_para(doc,
    "Três bugs em sequência na mesma conversa, impedindo o paciente de finalizar o pagamento.",
    size=10, italic=True, color=CINZA, after=8)

# ── BUG 1 ─────────────────────────────────────────────────────────────────────
severity_badge(doc, "MÉDIO", "Bug 1 — Pergunta de pagamento repetida (endereço em partes)")

colored_box(doc,
    ["📌 O que aconteceu:",
     "Samuel enviou o endereço em 4 mensagens separadas. Cada mensagem disparou o agente.",
     "Na última mensagem ('Df'), o agente avançou o setor e perguntou a forma de pagamento.",
     "Quando Samuel respondeu '1', o agente não reconheceu e repetiu a pergunta."],
    AZUL_CLARO_BG, text_color=AZUL, border_color="1F497D")

add_para(doc, "Conversa real (reconstituída):", bold=True, size=9.5, after=3)
chat_table(doc, [
    ("agente",   "Agora preciso do seu endereço para finalizar seu agendamento 😊\n📍 CEP\n🏠 Endereço completo e cidade", False),
    ("paciente", "01310-000",        False),
    ("paciente", "Rua das Flores",   False),
    ("paciente", "100",              False),
    ("paciente", "Df",               False),
    ("agente",   "Como você prefere pagar?\n1️⃣ PIX\n2️⃣ Cartão de crédito\nDigite 1 ou 2.", False),
    ("paciente", "1",                False),
    ("agente",   "Como você prefere pagar?\n1️⃣ PIX\n2️⃣ Cartão de crédito\nDigite 1 ou 2.", True),  # BUG
])

colored_box(doc,
    ["🔧 Causa técnica:",
     "O prompt avança o setor para PAGAMENTO imediatamente após qualquer resposta no setor de endereço,",
     "sem verificar se CEP e cidade foram recebidos. Com 4 mensagens separadas, cada uma dispara",
     "o agente. Na última mensagem, o agente avança o setor, mas o '1' da próxima mensagem chega",
     "no setor de pagamento sem contexto de que era a resposta ao menu."],
    VERMELHO_BG, text_color=VERMELHO, border_color="C00000")

colored_box(doc,
    ["✅ Fix no prompt (em todos os 4 setores de endereço):",
     "🔴 Verificar se a mensagem contém CEP (números com hífen) E cidade.",
     "🔴 Se CEP ou cidade ausentes → NÃO avançar setor. Solicitar endereço completo:",
     '     "Preciso do endereço completo numa única mensagem 😊',
     "      Exemplo: Rua das Flores, 100, Centro, São Paulo/SP, CEP 01310-000\"",
     "🔴 Somente quando CEP e cidade presentes → salvar e avançar setor."],
    VERDE_BG, text_color=(30, 80, 30), border_color="388E3C")

doc.add_paragraph()

# ── BUG 2 ─────────────────────────────────────────────────────────────────────
severity_badge(doc, "CRÍTICO", "Bug 2 — Link de pagamento gerado mas não enviado")

colored_box(doc,
    ["📌 O que aconteceu:",
     "Após Samuel enviar '1' pela segunda vez, o agente disse:",
     "     'Seu link de pagamento já foi gerado!'",
     "Mas não enviou a URL. A tool gerar_cobranca_direta foi chamada e executou com sucesso,",
     "porém o link retornado não foi incluído na mensagem enviada ao paciente."],
    AZUL_CLARO_BG, text_color=AZUL, border_color="1F497D")

add_para(doc, "Conversa real (reconstituída):", bold=True, size=9.5, after=3)
chat_table(doc, [
    ("paciente", "1",                False),
    ("agente",   "Pagamento gerado! Assim que confirmado, o médico irá realizar a renovação.\nVocê receberá sua nova receita por aqui em breve. 🧡", True),  # BUG: sem link
    ("paciente", "Mas e o link?",    False),
    ("paciente", "Cadê o link pra pagar?", False),
])

colored_box(doc,
    ["🔧 Causa técnica:",
     "O prompt instrui o agente a AGUARDAR o retorno de gerar_cobranca_direta,",
     "mas NÃO instrui a extrair e incluir o campo URL/link do retorno no output.",
     "O agente recebe o link internamente mas simplesmente não o envia."],
    VERMELHO_BG, text_color=VERMELHO, border_color="C00000")

colored_box(doc,
    ["✅ Fix no prompt (3 lugares: R4_PAGAMENTO, RECEITA_PAGAMENTO, EXAME_PAGAMENTO):",
     "— Adicionar após aguardar retorno de gerar_cobranca_direta:",
     "     🔴 Extrair o campo URL do retorno → salvar como LINK_PAGAMENTO.",
     "— Substituir o output por:",
     '     "Pagamento gerado! 😊',
     "      🔗 [LINK_PAGAMENTO]",
     "      Assim que confirmado, o médico irá realizar a renovação. 🧡\"",
     "",
     "⚠️ Ação necessária: confirmar com Nicolas o nome exato do campo URL retornado",
     "     pela tool gerar_cobranca_direta (ex: link, url, payment_url, invoiceUrl)."],
    VERDE_BG, text_color=(30, 80, 30), border_color="388E3C")

doc.add_paragraph()

# ── BUG 3 ─────────────────────────────────────────────────────────────────────
severity_badge(doc, "MÉDIO", "Bug 3 — Mesma mensagem repetida 3 vezes (loop)")

colored_box(doc,
    ["📌 O que aconteceu:",
     "Sem receber o link, Samuel enviou '?' sem saber o que fazer.",
     "O agente repetiu a última mensagem 3 vezes seguidas."],
    AZUL_CLARO_BG, text_color=AZUL, border_color="1F497D")

add_para(doc, "Conversa real (reconstituída):", bold=True, size=9.5, after=3)
chat_table(doc, [
    ("paciente", "?",    False),
    ("agente",   "Pagamento gerado! Assim que confirmado, o médico irá realizar a renovação.\nVocê receberá sua nova receita por aqui em breve. 🧡", True),
    ("agente",   "Pagamento gerado! Assim que confirmado, o médico irá realizar a renovação.\nVocê receberá sua nova receita por aqui em breve. 🧡", True),
    ("agente",   "Pagamento gerado! Assim que confirmado, o médico irá realizar a renovação.\nVocê receberá sua nova receita por aqui em breve. 🧡", True),
])

colored_box(doc,
    ["🔧 Causa técnica:",
     "Dois fatores combinados:",
     "1. O prompt não trata símbolos isolados ('?', '.') — o agente não sabe o que fazer.",
     "2. N8N não tem controle de concorrência: se o paciente envia várias mensagens rápidas,",
     "   múltiplas execuções do agente disparam simultaneamente e todas produzem o mesmo output."],
    VERMELHO_BG, text_color=VERMELHO, border_color="C00000")

colored_box(doc,
    ["✅ Fix no prompt (setor de pagamento):",
     "🔴 Se resposta inválida for apenas símbolo ('?', '.', '!') → contar como tentativa inválida.",
     "🔴 NÃO repetir a pergunta mais de uma vez por turno.",
     "🔴 Na 2ª tentativa inválida → escalar_humano.",
     "",
     "✅ Fix definitivo (N8N — para o Nicolas):",
     "Implementar lock/mutex por número de telefone para evitar execuções paralelas do mesmo",
     "paciente. Esta é uma configuração de infraestrutura que precisa ser feita no N8N."],
    VERDE_BG, text_color=(30, 80, 30), border_color="388E3C")

add_divider(doc)

# ════════════════════════════════════════════════════════════════════════════
# CONVERSA SILVIO
# ════════════════════════════════════════════════════════════════════════════
add_heading_custom(doc, "🗣️ Conversa 2 — Silvio", size=13, color=AZUL)
add_para(doc,
    "O agente funcionou corretamente — o bug está na plataforma de pagamento.",
    size=10, italic=True, color=CINZA, after=8)

severity_badge(doc, "BAIXO", "Bug 4 — Link enviado mas paciente não conseguiu pagar")

colored_box(doc,
    ["📌 O que aconteceu:",
     "O link foi gerado e enviado corretamente para Silvio:",
     "     https://www.asaas.com/i/f5tkup3eeamnz4dp",
     "O paciente tentou pagar mas não conseguiu."],
    AZUL_CLARO_BG, text_color=AZUL, border_color="1F497D")

add_para(doc, "Conversa real (reconstituída):", bold=True, size=9.5, after=3)
chat_table(doc, [
    ("agente",   "Pagamento gerado! 😊\n\n🔗 https://www.asaas.com/i/f5tkup3eeamnz4dp\n\nAssim que confirmado, o médico irá realizar a renovação. 🧡", False),
    ("paciente", "Não estou conseguindo pagar", False),
    ("paciente", "O link não funciona",         False),
])

colored_box(doc,
    ["🔧 Possíveis causas (externos ao agente):",
     "1. Expiração do link: cobranças Asaas expiram em 10 minutos — se o paciente demorou para clicar.",
     "2. Recusa bancária: cartão ou chave Pix do paciente pode ter sido recusado pelo banco.",
     "3. Falha temporária na plataforma Asaas no momento do pagamento.",
     "4. Cobrança já foi cancelada/expirada antes de o paciente conseguir abrir."],
    AMARELO_BG, text_color=LARANJA, border_color="FFA000")

colored_box(doc,
    ["✅ Ações recomendadas (Nicolas):",
     "1. Verificar no painel Asaas o status da cobrança gerada para Silvio.",
     "2. Confirmar se o tempo de expiração pode ser aumentado (padrão Asaas: 10 min).",
     "3. Considerar enviar instrução ao paciente após o link: 'Pague em até X minutos'.",
     "4. Considerar reenvio automático do link se detectar que o paciente não pagou."],
    VERDE_BG, text_color=(30, 80, 30), border_color="388E3C")

add_divider(doc)

# ════════════════════════════════════════════════════════════════════════════
# BUGS TÉCNICOS ADICIONAIS (revisão do prompt)
# ════════════════════════════════════════════════════════════════════════════
add_heading_custom(doc, "🔧 Bugs Adicionais — Revisão Técnica do Prompt", size=13, color=AZUL)
add_para(doc,
    "Identificados na revisão completa do prompt de Renovação, além dos bugs das conversas.",
    size=10, italic=True, color=CINZA, after=8)

# Bug técnico 1
severity_badge(doc, "MÉDIO", "Bug 5 — Ordem errada: output enviado antes da tool ser chamada")
colored_box(doc,
    ["📌 Onde: ETAPA 2E → OPÇÃO 3 (reemitir pedido antigo)",
     "O prompt envia a mensagem ao paciente ANTES de chamar atualizar_setor.",
     "Se a tool falhar, o output já foi enviado com o setor em estado errado.",
     "",
     "❌ Errado (atual):",
     "   Output: 'Seu pedido foi emitido nos últimos 6 meses?'",
     "   ⚡ Chame atualizar_setor com setor = RENOVACAO_EXAME_PRAZO",
     "",
     "✅ Correto:",
     "   ⚡ Chame atualizar_setor com setor = RENOVACAO_EXAME_PRAZO",
     "   Após tool retornar → output final: 'Seu pedido foi emitido nos últimos 6 meses?'"],
    AMARELO_BG, text_color=LARANJA, border_color="FFA000")

doc.add_paragraph()

# Bug técnico 2
severity_badge(doc, "MÉDIO", "Bug 6 — Duas tools chamadas sem sequenciamento (geo + setor)")
colored_box(doc,
    ["📌 Onde: RENOVACAO_RECEITA_ENDERECO e RENOVACAO_EXAME_ENDERECO (após receber endereço)",
     "O agente chama supabase_update_geolocalizacao e atualizar_setor simultaneamente.",
     "Se o salvamento do endereço falhar, o setor pode avançar com dados incompletos.",
     "",
     "❌ Errado (atual):",
     "   ⚡ Chame supabase_update_geolocalizacao",
     "   ⚡ Chame atualizar_setor com setor = RENOVACAO_RECEITA_PAGAMENTO",
     "",
     "✅ Correto:",
     "   ⚡ Chame supabase_update_geolocalizacao",
     "   🔴 Aguardar retorno com sucesso ANTES de continuar.",
     "   ⚡ Chame atualizar_setor com setor = RENOVACAO_RECEITA_PAGAMENTO"],
    AMARELO_BG, text_color=LARANJA, border_color="FFA000")

add_divider(doc)

# ════════════════════════════════════════════════════════════════════════════
# PLANO DE AÇÃO
# ════════════════════════════════════════════════════════════════════════════
add_heading_custom(doc, "📋 Plano de Ação", size=13, color=AZUL)

acoes_tbl = doc.add_table(rows=1, cols=5)
acoes_tbl.style = "Table Grid"
h_row = acoes_tbl.rows[0]
for i, h in enumerate(["#", "Ação", "Tipo", "Prioridade", "Responsável"]):
    cell_bg(h_row.cells[i], "1F497D")
    p = h_row.cells[i].paragraphs[0]
    r = p.add_run(h)
    set_font(r, size=9, bold=True, color=BRANCO)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

acoes = [
    ("1", "Confirmar nome do campo URL de gerar_cobranca_direta",      "Dev",    "🔴 Urgente", "Nicolas"),
    ("2", "Incluir [LINK_PAGAMENTO] nos 3 outputs de pagamento",        "Prompt", "🔴 Urgente", "Eq. Prompt"),
    ("3", "Validar CEP+cidade antes de avançar (4 setores de endereço)","Prompt", "🟡 Alta",    "Eq. Prompt"),
    ("4", "Tratar símbolo '?' como inválido nos setores de pagamento",  "Prompt", "🟡 Alta",    "Eq. Prompt"),
    ("5", "Implementar lock/mutex por telefone no N8N",                 "N8N",    "🟡 Alta",    "Nicolas"),
    ("6", "Corrigir ordem: tool → output na ETAPA 2E opção 3",          "Prompt", "🟡 Alta",    "Eq. Prompt"),
    ("7", "Sequenciar geo_save antes de atualizar_setor no endereço",   "Prompt", "🟡 Alta",    "Eq. Prompt"),
    ("8", "Verificar tempo de expiração dos links Asaas",               "Asaas",  "🟢 Normal",  "Nicolas"),
    ("9", "Testar fluxo completo com endereço em 1 mensagem (QA)",      "Teste",  "🟢 Normal",  "Eq. Teste"),
]
acao_bgs = [
    VERMELHO_BG, VERMELHO_BG,
    LARANJA_BG, LARANJA_BG, LARANJA_BG, LARANJA_BG, LARANJA_BG,
    VERDE_BG, VERDE_BG,
]
for idx, (num, acao, tipo, prio, resp) in enumerate(acoes):
    row = acoes_tbl.add_row()
    for j, val in enumerate([num, acao, tipo, prio, resp]):
        cell_bg(row.cells[j], acao_bgs[idx])
        p = row.cells[j].paragraphs[0]
        r = p.add_run(val)
        set_font(r, size=9)
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after  = Pt(2)

doc.add_paragraph()

# ── Rodapé ──────────────────────────────────────────────────────────────────
add_divider(doc, "1F497D")
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(f"REMMED Telemedicina  —  Documento Confidencial  —  {today}")
set_font(r, size=8, color=CINZA, italic=True)

# ── Salvar ───────────────────────────────────────────────────────────────────
path = "/home/user/clara-/Bugs_Pagamento_Nicolas_v2.docx"
doc.save(path)
print(f"Salvo: {path}")
