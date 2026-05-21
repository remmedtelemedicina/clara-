from docx import Document
from docx.shared import Pt, RGBColor, Cm, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# ── page margins ──────────────────────────────────────────────────────────────
for section in doc.sections:
    section.top_margin    = Cm(2)
    section.bottom_margin = Cm(2)
    section.left_margin   = Cm(2.5)
    section.right_margin  = Cm(2.5)

# ── colours ───────────────────────────────────────────────────────────────────
REMMED_BLUE   = RGBColor(0x1A, 0x73, 0xE8)
DARK_BG       = RGBColor(0x1E, 0x2A, 0x3A)
WHITE         = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_BLUE    = RGBColor(0xE8, 0xF0, 0xFE)
LIGHT_GREEN   = RGBColor(0xE6, 0xF4, 0xEA)
LIGHT_ORANGE  = RGBColor(0xFE, 0xF3, 0xE2)
LIGHT_RED     = RGBColor(0xFD, 0xED, 0xED)
LIGHT_PURPLE  = RGBColor(0xF3, 0xE8, 0xFD)
LIGHT_GRAY    = RGBColor(0xF8, 0xF9, 0xFA)
MID_GRAY      = RGBColor(0xE8, 0xEA, 0xED)
DARK_TEXT     = RGBColor(0x1E, 0x2A, 0x3A)
GREEN_TEXT    = RGBColor(0x18, 0x80, 0x38)
ORANGE_TEXT   = RGBColor(0xB3, 0x6B, 0x00)
RED_TEXT      = RGBColor(0xC5, 0x22, 0x1F)
PURPLE_TEXT   = RGBColor(0x6A, 0x1B, 0x9A)
BLUE_TEXT     = RGBColor(0x1A, 0x73, 0xE8)

# ── helpers ───────────────────────────────────────────────────────────────────
def set_cell_bg(cell, rgb: RGBColor):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd  = OxmlElement('w:shd')
    hex_color = f"{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"
    shd.set(qn('w:val'),   'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'),  hex_color)
    tcPr.append(shd)

def set_cell_border(cell, top=None, bottom=None, left=None, right=None):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for side, val in [('top',top),('bottom',bottom),('left',left),('right',right)]:
        if val:
            el = OxmlElement(f'w:{side}')
            el.set(qn('w:val'),   val.get('val','single'))
            el.set(qn('w:sz'),    val.get('sz','8'))
            el.set(qn('w:space'),'0')
            el.set(qn('w:color'), val.get('color','auto'))
            tcBorders.append(el)
    tcPr.append(tcBorders)

def para_space(para, before=0, after=0):
    pf = para.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after  = Pt(after)

def add_run(para, text, bold=False, italic=False, size=10,
            color=None, font_name='Calibri'):
    r = para.add_run(text)
    r.bold      = bold
    r.italic    = italic
    r.font.name = font_name
    r.font.size = Pt(size)
    if color:
        r.font.color.rgb = color
    return r

def heading_para(doc, text, size=14, color=WHITE, bg=DARK_BG, bold=True):
    """Full-width coloured heading row via 1-col table."""
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_bg(cell, bg)
    cell.top_margin    = Pt(8)
    cell.bottom_margin = Pt(8)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para_space(p, 4, 4)
    add_run(p, text, bold=bold, size=size, color=color)
    doc.add_paragraph()   # spacer

def section_title(doc, emoji, title, bg, text_color, size=12):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_bg(cell, bg)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    para_space(p, 4, 4)
    add_run(p, f"  {emoji}  {title}", bold=True, size=size, color=text_color)

def msg_bubble(doc, label, label_color, msg_text, bg=LIGHT_GRAY):
    """WhatsApp-style message bubble."""
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_bg(cell, bg)
    set_cell_border(cell,
        top=   {'val':'single','sz':'4','color':'DADCE0'},
        bottom={'val':'single','sz':'4','color':'DADCE0'},
        left=  {'val':'single','sz':'12','color':f"{label_color[0]:02X}{label_color[1]:02X}{label_color[2]:02X}"},
        right= {'val':'single','sz':'4','color':'DADCE0'})
    # label line
    p1 = cell.paragraphs[0]
    para_space(p1, 4, 2)
    add_run(p1, f"  {label}", bold=True, size=8, color=label_color)
    # message
    p2 = cell.add_paragraph()
    para_space(p2, 2, 6)
    add_run(p2, f"  {msg_text}", size=9.5, color=DARK_TEXT)

def response_row(doc, condition, action, cond_bg=LIGHT_GREEN, action_bg=LIGHT_BLUE):
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.columns[0].width = Cm(7)
    tbl.columns[1].width = Cm(10)
    c0, c1 = tbl.cell(0,0), tbl.cell(0,1)
    set_cell_bg(c0, cond_bg)
    set_cell_bg(c1, action_bg)
    p0 = c0.paragraphs[0]
    p1 = c1.paragraphs[0]
    para_space(p0, 4, 4)
    para_space(p1, 4, 4)
    add_run(p0, f"  {condition}", size=9, color=DARK_TEXT)
    add_run(p1, f"  {action}", size=9, color=DARK_TEXT)

def tech_row(doc, field, tipo, desc, header=False):
    tbl = doc.add_table(rows=1, cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.columns[0].width = Cm(5.5)
    tbl.columns[1].width = Cm(3.5)
    tbl.columns[2].width = Cm(8)
    bg = DARK_BG if header else LIGHT_GRAY
    tc = WHITE if header else DARK_TEXT
    for i, txt in enumerate([field, tipo, desc]):
        c = tbl.cell(0, i)
        set_cell_bg(c, bg)
        p = c.paragraphs[0]
        para_space(p, 4, 4)
        add_run(p, f"  {txt}", bold=header, size=9 if not header else 9,
                color=tc)

def spacer(doc, h=4):
    p = doc.add_paragraph()
    para_space(p, 0, 0)
    p.paragraph_format.line_spacing = Pt(h)

def trigger_row(doc, trigger_id, query, bg=LIGHT_GRAY, alt=False):
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.columns[0].width = Cm(4)
    tbl.columns[1].width = Cm(13)
    row_bg = MID_GRAY if alt else LIGHT_GRAY
    c0, c1 = tbl.cell(0,0), tbl.cell(0,1)
    set_cell_bg(c0, REMMED_BLUE if not alt else RGBColor(0x17,0x5D,0xBE))
    set_cell_bg(c1, row_bg)
    p0 = c0.paragraphs[0]
    p1 = c1.paragraphs[0]
    para_space(p0, 4, 4)
    para_space(p1, 4, 4)
    add_run(p0, f"  {trigger_id}", bold=True, size=9, color=WHITE)
    add_run(p1, f"  {query}", size=8.5, color=DARK_TEXT, font_name='Courier New')

# ══════════════════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════════════════
heading_para(doc,
    "🤖  CLARA — SISTEMA DE FOLLOW-UP  |  REMMED TELEMEDICINA",
    size=15, bg=DARK_BG)

# subtitle
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
para_space(p, 0, 8)
add_run(p, "Documento técnico para Nicolas  •  Estrutura completa de disparos automáticos",
        italic=True, size=10, color=RGBColor(0x5F,0x6B,0x7C))

# ── meta table ────────────────────────────────────────────────────────────────
tbl = doc.add_table(rows=1, cols=4)
tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
labels = ["Versão","Data","Responsável","Status"]
values = ["1.0","Maio / 2026","REMMED","🟡 Em revisão"]
for i in range(4):
    c = tbl.cell(0, i)
    set_cell_bg(c, LIGHT_BLUE if i % 2 == 0 else WHITE)
    p = c.paragraphs[0]
    para_space(p, 5, 5)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_run(p, labels[i] + "\n", bold=True, size=8, color=BLUE_TEXT)
    add_run(p, values[i], size=9, color=DARK_TEXT)

spacer(doc, 12)

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 1 — VISÃO GERAL
# ══════════════════════════════════════════════════════════════════════════════
heading_para(doc, "📋  VISÃO GERAL — O QUE SERÁ CONSTRUÍDO", size=12, bg=REMMED_BLUE)

overview = [
    ("Bloco 1", "Pós-consulta geral",             "D+7  •  D+30  •  D+60",  "✅ Existe — melhorar mensagens", LIGHT_GREEN, GREEN_TEXT),
    ("Bloco 2", "Carrinho abandonado",              "30min  •  D+1",           "✅ Existe — OK",                  LIGHT_GREEN, GREEN_TEXT),
    ("Bloco 3", "Renovação de receita — 30 dias",  "D-7  •  D-3  •  D+3",    "🔴 Criar do zero",                LIGHT_RED,   RED_TEXT),
    ("Bloco 4", "Renovação de receita — 60 dias",  "D-10  •  D-5  •  D+5",   "🔴 Criar do zero",                LIGHT_RED,   RED_TEXT),
    ("Bloco 5", "Reativação — pacientes dormentes","D+90  •  D+120",          "🔴 Criar do zero",                LIGHT_RED,   RED_TEXT),
    ("Global",  "Opt-out (LGPD)",                  "Sempre ativo",            "🔴 Criar do zero — obrigatório",  LIGHT_ORANGE,ORANGE_TEXT),
]

# header row
tbl = doc.add_table(rows=1, cols=4)
tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl.columns[0].width = Cm(2)
tbl.columns[1].width = Cm(6)
tbl.columns[2].width = Cm(4)
tbl.columns[3].width = Cm(6)
for i, h in enumerate(["Bloco","Descrição","Dias de disparo","Status"]):
    c = tbl.cell(0, i)
    set_cell_bg(c, DARK_BG)
    p = c.paragraphs[0]
    para_space(p, 5, 5)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_run(p, h, bold=True, size=9, color=WHITE)

for bloco, desc, dias, status, bg, tc in overview:
    row = tbl.add_row()
    for i, txt in enumerate([bloco, desc, dias, status]):
        c = row.cells[i]
        set_cell_bg(c, bg if i == 3 else LIGHT_GRAY)
        p = c.paragraphs[0]
        para_space(p, 4, 4)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in (0,2) else WD_ALIGN_PARAGRAPH.LEFT
        add_run(p, f"  {txt}" if i != 0 else txt,
                bold=(i==0), size=9,
                color=tc if i==3 else DARK_TEXT)

spacer(doc, 14)

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2 — CALENDÁRIO COMPLETO
# ══════════════════════════════════════════════════════════════════════════════
heading_para(doc, "📅  CALENDÁRIO COMPLETO DE DISPAROS", size=12, bg=REMMED_BLUE)

calendar_items = [
    # (dia, evento, bloco, observação)
    ("D+0\n(30 min)", "Lembrete de pagamento pendente",      "Bloco 2", "Disparar 30 min após agendamento sem pagamento confirmado"),
    ("D+1",           "2º lembrete pagamento pendente",      "Bloco 2", "Apenas se não houve resposta no D+0"),
    ("D+7",           "Follow-up pós-consulta",              "Bloco 1", "Verificar evolução e abrir porta para reagendamento"),
    ("D+30",          "Check-in 1 mês",                      "Bloco 1", "Oferecer renovação de receita ou nova consulta"),
    ("D+60",          "Manutenção de relacionamento",         "Bloco 1", "Intervalo mínimo — só disparar se sem contato nos 30 dias anteriores"),
    ("D+90",          "Reativação paciente dormente",         "Bloco 5", "Paciente sem nenhum contato por 90 dias"),
    ("D+120",         "Última tentativa de reativação",       "Bloco 5", "Somente se não respondeu D+90"),
    ("Renovação -10", "Aviso renovação antecipado (60 dias)", "Bloco 4", "Apenas pacientes com ciclo de 60 dias"),
    ("Renovação -7",  "Aviso renovação (30 dias)",            "Bloco 3", "Apenas pacientes com ciclo de 30 dias"),
    ("Renovação -5",  "2º aviso renovação (60 dias)",         "Bloco 4", "Se não respondeu ao D-10"),
    ("Renovação -3",  "2º aviso renovação (30 dias)",         "Bloco 3", "Se não respondeu ao D-7"),
    ("Renovação +3",  "Recuperação pós-vencimento (30 dias)","Bloco 3", "Receita já venceu — oferecer renovação"),
    ("Renovação +5",  "Recuperação pós-vencimento (60 dias)","Bloco 4", "Receita já venceu — oferecer renovação"),
]

tbl = doc.add_table(rows=1, cols=4)
tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl.columns[0].width = Cm(2.5)
tbl.columns[1].width = Cm(6)
tbl.columns[2].width = Cm(2.5)
tbl.columns[3].width = Cm(7)
for i, h in enumerate(["Dia","Evento","Bloco","Observação"]):
    c = tbl.cell(0, i)
    set_cell_bg(c, DARK_BG)
    p = c.paragraphs[0]
    para_space(p, 5, 5)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_run(p, h, bold=True, size=9, color=WHITE)

alt = False
for dia, evento, bloco, obs in calendar_items:
    row = tbl.add_row()
    row_bg = MID_GRAY if alt else LIGHT_GRAY
    for i, txt in enumerate([dia, evento, bloco, obs]):
        c = row.cells[i]
        set_cell_bg(c, row_bg)
        p = c.paragraphs[0]
        para_space(p, 4, 4)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in (0,2) else WD_ALIGN_PARAGRAPH.LEFT
        color = BLUE_TEXT if i == 2 else DARK_TEXT
        add_run(p, txt, bold=(i==0), size=8.5, color=color)
    alt = not alt

spacer(doc, 14)

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 3 — MENSAGENS POR BLOCO
# ══════════════════════════════════════════════════════════════════════════════
heading_para(doc, "💬  MENSAGENS — BLOCO A BLOCO", size=12, bg=REMMED_BLUE)

# ── BLOCO 1 ──────────────────────────────────────────────────────────────────
section_title(doc, "🔵", "BLOCO 1 — Pós-consulta geral", LIGHT_BLUE, BLUE_TEXT)
spacer(doc, 6)

msg_bubble(doc, "📅  D+7  —  Primeira mensagem após consulta", BLUE_TEXT,
    "Olá, [NOME]! 🧡 Como você está se sentindo desde a sua consulta?\n\n"
    "  Se melhorou → ótimo! Qualquer dúvida, estou aqui.\n"
    "  Se ainda não melhorou → posso te ajudar a agendar uma reavaliação — o médico pode ajustar o tratamento.")
spacer(doc, 4)

p = doc.add_paragraph()
para_space(p, 2, 2)
add_run(p, "  Respostas automáticas:", bold=True, size=9, color=DARK_TEXT)
response_row(doc, "👉  Paciente diz: melhorei",
                  "✅  \"Que bom saber disso! Cuide-se, estou aqui sempre que precisar. 🌿\"",
             LIGHT_GREEN, LIGHT_GRAY)
spacer(doc, 3)
response_row(doc, "👉  Paciente menciona sintomas",
                  "📅  \"Posso te ajudar a agendar uma reavaliação? O médico pode ajustar o tratamento.\"  →  fluxo de agendamento",
             LIGHT_ORANGE, LIGHT_BLUE)
spacer(doc, 8)

msg_bubble(doc, "📅  D+30  —  Check-in 1 mês", BLUE_TEXT,
    "Oi, [NOME]! 🧡 Passando pra lembrar que faz 1 mês desde a sua consulta.\n\n"
    "  Como está sua saúde? Se quiser renovar receita, fazer check-up ou um novo atendimento,\n"
    "  posso organizar rapidinho pra você 😊")
spacer(doc, 4)

response_row(doc, "👉  Paciente responde SIM",
                  "📅  Direcionar para fluxo de agendamento",
             LIGHT_GREEN, LIGHT_BLUE)
spacer(doc, 3)
response_row(doc, "👉  Paciente diz não / tudo bem",
                  "✅  \"Fico feliz que esteja bem! Estarei por aqui quando precisar. 🌿\"",
             LIGHT_GRAY, LIGHT_GRAY)
spacer(doc, 8)

msg_bubble(doc, "📅  D+60  —  Manutenção de relacionamento", BLUE_TEXT,
    "Olá, [NOME]! 🌿 Passando rapidinho pra saber como você está.\n\n"
    "  Se precisar de renovação de receita, acompanhamento ou quiser agendar uma consulta,\n"
    "  estou aqui pra te ajudar! 😊\n\n"
    "  ⚠️  Só disparar se não houve nenhum contato nos últimos 30 dias.")
spacer(doc, 10)

# ── BLOCO 2 ──────────────────────────────────────────────────────────────────
section_title(doc, "🔴", "BLOCO 2 — Carrinho abandonado (agendou mas não pagou)", LIGHT_RED, RED_TEXT)
spacer(doc, 6)

msg_bubble(doc, "📅  D+0  (30 min após agendamento sem pagamento)", RED_TEXT,
    "Oi! 😊 Vi que você iniciou seu agendamento mas ainda não finalizou o pagamento.\n\n"
    "  Seu horário está reservado por um tempo limitado.\n"
    "  Quer concluir agora? É rápido, te ajudo!",
    bg=LIGHT_RED)
spacer(doc, 4)

msg_bubble(doc, "📅  D+1  (manhã seguinte — sem resposta)", RED_TEXT,
    "Oi, [NOME]! Passando pra saber se você ainda quer realizar sua consulta. 🧡\n\n"
    "  Se precisar, posso te ajudar a organizar rapidinho.",
    bg=LIGHT_RED)
spacer(doc, 4)

response_row(doc, "👉  Paciente responde SIM",
                  "📅  Direcionar para fluxo de agendamento/pagamento",
             LIGHT_GREEN, LIGHT_BLUE)
spacer(doc, 3)
response_row(doc, "👉  Paciente responde NÃO",
                  "✅  \"Sem problema! Estaremos à disposição sempre que precisar. 🧡\"",
             LIGHT_GRAY, LIGHT_GRAY)
spacer(doc, 10)

# ── BLOCO 3 ──────────────────────────────────────────────────────────────────
section_title(doc, "🟢", "BLOCO 3 — Renovação de receita  |  Ciclo 30 dias", LIGHT_GREEN, GREEN_TEXT)
spacer(doc, 4)

p = doc.add_paragraph()
para_space(p, 2, 4)
add_run(p, "  ⚡  Gatilho:  ", bold=True, size=9, color=GREEN_TEXT)
add_run(p, "proxima_renovacao = HOJE + 7  AND  ciclo_renovacao = 30  AND  opt_out = false", size=9, color=DARK_TEXT, font_name='Courier New')

msg_bubble(doc, "📅  D-7  (7 dias antes do vencimento)", GREEN_TEXT,
    "Olá, [NOME]! 💊 Sua receita de [MEDICAMENTO] vence em 7 dias.\n\n"
    "  Quer renovar agora? Leva menos de 5 minutos e você já recebe a receita digital 😊\n\n"
    "  👉  Responda SIM que eu organizo tudo!",
    bg=LIGHT_GREEN)
spacer(doc, 4)

msg_bubble(doc, "📅  D-3  (3 dias antes — sem resposta ao D-7)", GREEN_TEXT,
    "Oi, [NOME]! 🧡 Só lembrando: sua receita vence em 3 dias.\n\n"
    "  Posso renovar agora, demora menos de 5 minutos!",
    bg=LIGHT_GREEN)
spacer(doc, 4)

msg_bubble(doc, "📅  D+3  (receita já vencida — recuperação)", GREEN_TEXT,
    "Oi, [NOME]! Percebi que sua receita de [MEDICAMENTO] pode ter vencido. 🧡\n\n"
    "  Sem problema — consigo renovar mesmo assim.\n"
    "  Quer que eu agende agora?",
    bg=LIGHT_GREEN)
spacer(doc, 4)

response_row(doc, "👉  SIM em qualquer mensagem",
                  "📅  Direcionar para fluxo de Renovação de Receita",
             LIGHT_GREEN, LIGHT_BLUE)
spacer(doc, 10)

# ── BLOCO 4 ──────────────────────────────────────────────────────────────────
section_title(doc, "🟣", "BLOCO 4 — Renovação de receita  |  Ciclo 60 dias", LIGHT_PURPLE, PURPLE_TEXT)
spacer(doc, 4)

p = doc.add_paragraph()
para_space(p, 2, 4)
add_run(p, "  ⚡  Gatilho:  ", bold=True, size=9, color=PURPLE_TEXT)
add_run(p, "proxima_renovacao = HOJE + 10  AND  ciclo_renovacao = 60  AND  opt_out = false", size=9, color=DARK_TEXT, font_name='Courier New')

msg_bubble(doc, "📅  D-10  (10 dias antes do vencimento)", PURPLE_TEXT,
    "Olá, [NOME]! 💊 Sua receita vence em 10 dias.\n\n"
    "  Quando quiser renovar, estou aqui — é rápido e você recebe tudo pelo celular 😊\n\n"
    "  👉  Responda SIM que eu organizo!",
    bg=LIGHT_PURPLE)
spacer(doc, 4)

msg_bubble(doc, "📅  D-5  (5 dias antes — sem resposta ao D-10)", PURPLE_TEXT,
    "Oi, [NOME]! 🧡 Sua receita vence em 5 dias.\n\n"
    "  Posso renovar agora, é bem rápido!",
    bg=LIGHT_PURPLE)
spacer(doc, 4)

msg_bubble(doc, "📅  D+5  (receita já vencida — recuperação)", PURPLE_TEXT,
    "Oi, [NOME]! Sua receita pode ter vencido esta semana. 🧡\n\n"
    "  Consigo renovar agora mesmo se quiser.\n"
    "  Só me responder que eu organizo!",
    bg=LIGHT_PURPLE)
spacer(doc, 4)

response_row(doc, "👉  SIM em qualquer mensagem",
                  "📅  Direcionar para fluxo de Renovação de Receita",
             LIGHT_GREEN, LIGHT_BLUE)
spacer(doc, 10)

# ── BLOCO 5 ──────────────────────────────────────────────────────────────────
section_title(doc, "🟠", "BLOCO 5 — Reativação de pacientes dormentes", LIGHT_ORANGE, ORANGE_TEXT)
spacer(doc, 4)

p = doc.add_paragraph()
para_space(p, 2, 4)
add_run(p, "  ⚡  Gatilho:  ", bold=True, size=9, color=ORANGE_TEXT)
add_run(p, "data_ultima_consulta = HOJE - 90  AND  opt_out = false  AND  sem contato há 30+ dias", size=9, color=DARK_TEXT, font_name='Courier New')

msg_bubble(doc, "📅  D+90  (90 dias sem nenhum contato)", ORANGE_TEXT,
    "Oi, [NOME]! 🧡 Faz um tempo que não nos falamos.\n\n"
    "  Como está sua saúde? Se precisar de qualquer coisa — consulta, renovação ou só\n"
    "  tirar uma dúvida — estamos aqui pra te ajudar 😊",
    bg=LIGHT_ORANGE)
spacer(doc, 4)

msg_bubble(doc, "📅  D+120  (última tentativa — sem resposta ao D+90)", ORANGE_TEXT,
    "Oi, [NOME]! Notamos que faz um tempo desde sua última consulta. 🧡\n\n"
    "  Quando quiser retomar seu acompanhamento, estamos aqui com toda a estrutura\n"
    "  pra te atender da melhor forma 😊",
    bg=LIGHT_ORANGE)
spacer(doc, 4)

response_row(doc, "👉  Sem resposta após D+120",
                  "⚠️  Marcar paciente como 'inativo' no banco — parar envios",
             LIGHT_RED, LIGHT_ORANGE)
spacer(doc, 10)

# ── OPT-OUT ───────────────────────────────────────────────────────────────────
section_title(doc, "⛔", "REGRA GLOBAL — Opt-out (LGPD obrigatório)", LIGHT_RED, RED_TEXT)
spacer(doc, 6)

p = doc.add_paragraph()
para_space(p, 2, 4)
add_run(p, "  Palavras que ativam opt-out: ", bold=True, size=9, color=RED_TEXT)
add_run(p, '"pare"  "stop"  "não quero mais"  "remover"  "cancelar mensagens"  "para de me mandar"', size=9, color=DARK_TEXT, font_name='Courier New')

response_row(doc,
    "Paciente envia qualquer palavra de opt-out",
    "1. Setar opt_out = true no Supabase\n  2. Parar TODOS os envios futuros\n  3. Responder: \"Entendido! Não enviarei mais mensagens. Se precisar, pode me chamar. 🧡\"",
    LIGHT_RED, LIGHT_GRAY)
spacer(doc, 10)

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 4 — BANCO DE DADOS
# ══════════════════════════════════════════════════════════════════════════════
heading_para(doc, "🗄️  BANCO DE DADOS — NOVOS CAMPOS NECESSÁRIOS", size=12, bg=REMMED_BLUE)

tech_row(doc, "Campo", "Tipo", "Descrição", header=True)
campos = [
    ("data_ultima_consulta",  "date",      "Data da última consulta realizada — base para D+7, D+30, D+60, D+90"),
    ("ciclo_renovacao",       "int",       "30 ou 60 — preencher na renovação de receita"),
    ("proxima_renovacao",     "date",      "Calculado: data_ultima_consulta + ciclo_renovacao"),
    ("medicamento_renovacao", "text",      "Nome do medicamento para personalizar mensagem do Bloco 3/4"),
    ("opt_out",               "boolean",   "false por padrão — setar true quando paciente pedir para parar"),
    ("ultimo_followup",       "date",      "Data do último disparo — evitar duplicidade"),
    ("status_paciente",       "text",      "'ativo' / 'inativo' — setar 'inativo' após D+120 sem resposta"),
]
for i, (f, t, d) in enumerate(campos):
    tech_row(doc, f, t, d)

spacer(doc, 14)

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 5 — TRIGGERS N8N
# ══════════════════════════════════════════════════════════════════════════════
heading_para(doc, "⚡  N8N — TRIGGERS (Schedule diário — roda toda manhã)", size=12, bg=REMMED_BLUE)

p = doc.add_paragraph()
para_space(p, 0, 6)
add_run(p, "  Cada trigger abaixo é um nó Schedule no N8N. Executa 1x por dia (ex: 09h00).\n"
           "  Para cada registro retornado → disparar mensagem WhatsApp via Evolution API.",
        size=9, color=DARK_TEXT, italic=True)

triggers = [
    ("T1 — Bloco 1 D+7",    "SELECT * FROM clientes WHERE data_ultima_consulta = CURRENT_DATE - 7 AND opt_out = false"),
    ("T2 — Bloco 1 D+30",   "SELECT * FROM clientes WHERE data_ultima_consulta = CURRENT_DATE - 30 AND opt_out = false"),
    ("T3 — Bloco 1 D+60",   "SELECT * FROM clientes WHERE data_ultima_consulta = CURRENT_DATE - 60 AND opt_out = false AND ultimo_followup < CURRENT_DATE - 30"),
    ("T4 — Bloco 2 30min",  "SELECT * FROM agendamentos WHERE criado_em <= NOW() - INTERVAL '30 min' AND pagamento_confirmado = false AND opt_out = false"),
    ("T5 — Bloco 3 D-7",    "SELECT * FROM clientes WHERE proxima_renovacao = CURRENT_DATE + 7 AND ciclo_renovacao = 30 AND opt_out = false"),
    ("T6 — Bloco 3 D-3",    "SELECT * FROM clientes WHERE proxima_renovacao = CURRENT_DATE + 3 AND ciclo_renovacao = 30 AND opt_out = false"),
    ("T7 — Bloco 3 D+3",    "SELECT * FROM clientes WHERE proxima_renovacao = CURRENT_DATE - 3 AND ciclo_renovacao = 30 AND opt_out = false"),
    ("T8 — Bloco 4 D-10",   "SELECT * FROM clientes WHERE proxima_renovacao = CURRENT_DATE + 10 AND ciclo_renovacao = 60 AND opt_out = false"),
    ("T9 — Bloco 4 D-5",    "SELECT * FROM clientes WHERE proxima_renovacao = CURRENT_DATE + 5 AND ciclo_renovacao = 60 AND opt_out = false"),
    ("T10 — Bloco 4 D+5",   "SELECT * FROM clientes WHERE proxima_renovacao = CURRENT_DATE - 5 AND ciclo_renovacao = 60 AND opt_out = false"),
    ("T11 — Bloco 5 D+90",  "SELECT * FROM clientes WHERE data_ultima_consulta = CURRENT_DATE - 90 AND opt_out = false AND status_paciente = 'ativo'"),
    ("T12 — Bloco 5 D+120", "SELECT * FROM clientes WHERE data_ultima_consulta = CURRENT_DATE - 120 AND opt_out = false AND status_paciente = 'ativo'"),
]

for i, (tid, query) in enumerate(triggers):
    trigger_row(doc, tid, query, alt=(i%2==1))
    spacer(doc, 2)

spacer(doc, 10)

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 6 — PRIORIDADES
# ══════════════════════════════════════════════════════════════════════════════
heading_para(doc, "🎯  PRIORIDADE DE IMPLEMENTAÇÃO", size=12, bg=REMMED_BLUE)

prios = [
    ("1ª",  "Alta",   "Opt-out global",                  "Obrigatório LGPD antes de qualquer disparo em produção"),
    ("2ª",  "Alta",   "Bloco 2 — Carrinho abandonado",    "Recuperação imediata de receita — ROI direto"),
    ("3ª",  "Alta",   "Bloco 3 — Renovação 30 dias",      "Maior volume de pacientes — receita recorrente"),
    ("4ª",  "Média",  "Bloco 1 — Pós-consulta (melhorar)","Refinar mensagens e segmentar por tipo de consulta"),
    ("5ª",  "Média",  "Bloco 4 — Renovação 60 dias",      "Mesma lógica do Bloco 3 — ciclo diferente"),
    ("6ª",  "Baixa",  "Bloco 5 — Reativação",             "Impacto de longo prazo — implementar por último"),
]

tbl = doc.add_table(rows=1, cols=4)
tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl.columns[0].width = Cm(1.5)
tbl.columns[1].width = Cm(2)
tbl.columns[2].width = Cm(6)
tbl.columns[3].width = Cm(8.5)
for i, h in enumerate(["Ordem","Prioridade","O que implementar","Motivo"]):
    c = tbl.cell(0, i)
    set_cell_bg(c, DARK_BG)
    p = c.paragraphs[0]
    para_space(p, 5, 5)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_run(p, h, bold=True, size=9, color=WHITE)

prio_colors = {
    "Alta":  (LIGHT_RED,    RED_TEXT),
    "Média": (LIGHT_ORANGE, ORANGE_TEXT),
    "Baixa": (LIGHT_GREEN,  GREEN_TEXT),
}
for i, (ordem, prio, o_que, motivo) in enumerate(prios):
    row = tbl.add_row()
    bg = LIGHT_GRAY if i % 2 == 0 else MID_GRAY
    pbg, ptc = prio_colors[prio]
    for j, txt in enumerate([ordem, prio, o_que, motivo]):
        c = row.cells[j]
        set_cell_bg(c, pbg if j == 1 else bg)
        p = c.paragraphs[0]
        para_space(p, 4, 4)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j in (0,1) else WD_ALIGN_PARAGRAPH.LEFT
        add_run(p, txt, bold=(j<2), size=9,
                color=ptc if j==1 else DARK_TEXT)

spacer(doc, 14)

# ── footer ────────────────────────────────────────────────────────────────────
tbl = doc.add_table(rows=1, cols=1)
tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
cell = tbl.cell(0, 0)
set_cell_bg(cell, DARK_BG)
p = cell.paragraphs[0]
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
para_space(p, 8, 8)
add_run(p, "REMMED Telemedicina  •  Sistema Clara  •  Follow-up Automático v1.0  •  Maio 2026",
        size=8, color=RGBColor(0xA0, 0xAE, 0xBE))

# ── save ──────────────────────────────────────────────────────────────────────
out = "/home/user/clara-/FollowUp_Nicolas_v1.docx"
doc.save(out)
print(f"Saved: {out}")
