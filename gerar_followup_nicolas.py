from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

for section in doc.sections:
    section.top_margin    = Cm(2)
    section.bottom_margin = Cm(2)
    section.left_margin   = Cm(2.5)
    section.right_margin  = Cm(2.5)

# ── cores ─────────────────────────────────────────────────────────────────────
REMMED_BLUE  = RGBColor(0x1A, 0x73, 0xE8)
DARK_BG      = RGBColor(0x1E, 0x2A, 0x3A)
WHITE        = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_BLUE   = RGBColor(0xE8, 0xF0, 0xFE)
LIGHT_GREEN  = RGBColor(0xE6, 0xF4, 0xEA)
LIGHT_ORANGE = RGBColor(0xFE, 0xF3, 0xE2)
LIGHT_RED    = RGBColor(0xFD, 0xED, 0xED)
LIGHT_PURPLE = RGBColor(0xF3, 0xE8, 0xFD)
LIGHT_TEAL   = RGBColor(0xE0, 0xF5, 0xF1)
LIGHT_PINK   = RGBColor(0xFC, 0xE4, 0xEC)
LIGHT_YELLOW = RGBColor(0xFF, 0xF9, 0xE6)
LIGHT_GRAY   = RGBColor(0xF8, 0xF9, 0xFA)
MID_GRAY     = RGBColor(0xE8, 0xEA, 0xED)
DARK_TEXT    = RGBColor(0x1E, 0x2A, 0x3A)
GREEN_TEXT   = RGBColor(0x18, 0x80, 0x38)
ORANGE_TEXT  = RGBColor(0xB3, 0x6B, 0x00)
RED_TEXT     = RGBColor(0xC5, 0x22, 0x1F)
PURPLE_TEXT  = RGBColor(0x6A, 0x1B, 0x9A)
BLUE_TEXT    = RGBColor(0x1A, 0x73, 0xE8)
TEAL_TEXT    = RGBColor(0x00, 0x7B, 0x6E)
PINK_TEXT    = RGBColor(0xAD, 0x14, 0x57)
YELLOW_TEXT  = RGBColor(0x7A, 0x5C, 0x00)

# ── helpers ───────────────────────────────────────────────────────────────────
def set_cell_bg(cell, rgb):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd  = OxmlElement('w:shd')
    shd.set(qn('w:val'),   'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'),  f"{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}")
    tcPr.append(shd)

def set_left_border(cell, color):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcB  = OxmlElement('w:tcBorders')
    for side in ['top','bottom','right']:
        el = OxmlElement(f'w:{side}')
        el.set(qn('w:val'), 'single'); el.set(qn('w:sz'), '4')
        el.set(qn('w:space'), '0');    el.set(qn('w:color'), 'DADCE0')
        tcB.append(el)
    left = OxmlElement('w:left')
    left.set(qn('w:val'), 'single'); left.set(qn('w:sz'), '14')
    left.set(qn('w:space'), '0');    left.set(qn('w:color'), color)
    tcB.append(left)
    tcPr.append(tcB)

def ps(para, b=0, a=0):
    para.paragraph_format.space_before = Pt(b)
    para.paragraph_format.space_after  = Pt(a)

def run(para, text, bold=False, italic=False, size=10, color=None, mono=False):
    r = para.add_run(text)
    r.bold = bold; r.italic = italic
    r.font.name = 'Courier New' if mono else 'Calibri'
    r.font.size = Pt(size)
    if color: r.font.color.rgb = color
    return r

def spacer(doc, h=6):
    p = doc.add_paragraph()
    ps(p); p.paragraph_format.line_spacing = Pt(h)

def heading(doc, text, size=12, bg=REMMED_BLUE):
    t = doc.add_table(rows=1, cols=1); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.cell(0,0); set_cell_bg(c, bg)
    p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER; ps(p,5,5)
    run(p, text, bold=True, size=size, color=WHITE)
    spacer(doc, 4)

def block_title(doc, emoji, title, bg, tc, size=11):
    t = doc.add_table(rows=1, cols=1); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.cell(0,0); set_cell_bg(c, bg)
    p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.LEFT; ps(p,5,5)
    run(p, f"  {emoji}  {title}", bold=True, size=size, color=tc)

def bubble(doc, label, lc, msg, bg=LIGHT_GRAY):
    hex_lc = f"{lc[0]:02X}{lc[1]:02X}{lc[2]:02X}"
    t = doc.add_table(rows=1, cols=1); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    c = t.cell(0,0); set_cell_bg(c, bg); set_left_border(c, hex_lc)
    p1 = c.paragraphs[0]; ps(p1,4,2)
    run(p1, f"  {label}", bold=True, size=8, color=lc)
    p2 = c.add_paragraph(); ps(p2,2,6)
    run(p2, f"  {msg}", size=9.5, color=DARK_TEXT)

def resp(doc, cond, act, cbg=LIGHT_GREEN, abg=LIGHT_BLUE):
    t = doc.add_table(rows=1, cols=2); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.columns[0].width = Cm(7); t.columns[1].width = Cm(10)
    c0,c1 = t.cell(0,0), t.cell(0,1)
    set_cell_bg(c0,cbg); set_cell_bg(c1,abg)
    for c,txt in [(c0,cond),(c1,act)]:
        p = c.paragraphs[0]; ps(p,4,4)
        run(p, f"  {txt}", size=9, color=DARK_TEXT)

def trig(doc, tid, query, alt=False):
    bg1 = RGBColor(0x17,0x5D,0xBE) if alt else REMMED_BLUE
    bg2 = MID_GRAY if alt else LIGHT_GRAY
    t = doc.add_table(rows=1, cols=2); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.columns[0].width = Cm(4); t.columns[1].width = Cm(13)
    c0,c1 = t.cell(0,0), t.cell(0,1)
    set_cell_bg(c0,bg1); set_cell_bg(c1,bg2)
    p0,p1 = c0.paragraphs[0], c1.paragraphs[0]
    ps(p0,4,4); ps(p1,4,4)
    run(p0, f"  {tid}", bold=True, size=9, color=WHITE)
    run(p1, f"  {query}", size=8, color=DARK_TEXT, mono=True)

def db_row(doc, field, tipo, desc, header=False):
    bg = DARK_BG if header else LIGHT_GRAY
    tc_color = WHITE if header else DARK_TEXT
    t = doc.add_table(rows=1, cols=3); t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.columns[0].width = Cm(5.5); t.columns[1].width = Cm(3); t.columns[2].width = Cm(8.5)
    for i,(txt,w) in enumerate([(field,5.5),(tipo,3),(desc,8.5)]):
        c = t.cell(0,i); set_cell_bg(c, bg)
        p = c.paragraphs[0]; ps(p,4,4)
        run(p, f"  {txt}", bold=header, size=9, color=tc_color,
            mono=(i==0 and not header))

def gatilho_line(doc, text, color):
    p = doc.add_paragraph(); ps(p,2,4)
    run(p, "  ⚡  Gatilho:  ", bold=True, size=9, color=color)
    run(p, text, size=8.5, color=DARK_TEXT, mono=True)

# ══════════════════════════════════════════════════════════════════════════════
# CABEÇALHO
# ══════════════════════════════════════════════════════════════════════════════
heading(doc, "🤖  CLARA — SISTEMA DE FOLLOW-UP  |  REMMED TELEMEDICINA", size=15, bg=DARK_BG)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; ps(p,0,8)
run(p, "Documento técnico para Nicolas  •  Estrutura completa de disparos automáticos",
    italic=True, size=10, color=RGBColor(0x5F,0x6B,0x7C))

t = doc.add_table(rows=1, cols=4); t.alignment = WD_TABLE_ALIGNMENT.CENTER
for i,(lbl,val,bg) in enumerate([
    ("Versão","2.0",LIGHT_BLUE),("Data","Maio / 2026",WHITE),
    ("Responsável","REMMED",LIGHT_BLUE),("Status","🟡 Em revisão",WHITE)]):
    c = t.cell(0,i); set_cell_bg(c,bg)
    p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER; ps(p,5,5)
    run(p, lbl+"\n", bold=True, size=8, color=BLUE_TEXT)
    run(p, val, size=9, color=DARK_TEXT)

spacer(doc,12)

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 1 — VISÃO GERAL
# ══════════════════════════════════════════════════════════════════════════════
heading(doc, "📋  VISÃO GERAL — O QUE SERÁ CONSTRUÍDO")

overview = [
    ("Bloco 1","Pós-consulta geral",                "D+7  •  D+30  •  D+60",         "✅ Existe — mensagens ajustadas", LIGHT_GREEN,  GREEN_TEXT),
    ("Bloco 2","Carrinho abandonado",                "30min  •  D+1",                  "✅ Existe — OK",                  LIGHT_GREEN,  GREEN_TEXT),
    ("Bloco 3","Renovação de receita — 30 dias",     "D-7  •  D-3  •  D+3",           "🔴 Criar do zero",                LIGHT_RED,    RED_TEXT),
    ("Bloco 4","Renovação de receita — 60 dias",     "D-10  •  D-5  •  D+5",          "🔴 Criar do zero",                LIGHT_RED,    RED_TEXT),
    ("Bloco 5","Reativação — pacientes dormentes",   "D+90  •  D+120",                 "🔴 Criar do zero",                LIGHT_RED,    RED_TEXT),
    ("Bloco 6","Cuidado permanente (pós D+120)",     "A cada 60 dias — indefinido",    "🔴 Criar do zero",                LIGHT_RED,    RED_TEXT),
    ("Bloco 7","Sazonais — calendário fixo",         "Jun  •  Nov  •  Jan  •  7 Abr", "🔴 Criar do zero",                LIGHT_RED,    RED_TEXT),
    ("Bloco 8","Datas especiais do paciente",        "Aniversário  •  1 ano REMMED",   "🔴 Criar do zero",                LIGHT_RED,    RED_TEXT),
    ("Global", "Opt-out (LGPD)",                     "Sempre ativo",                   "🔴 Criar do zero — obrigatório",  LIGHT_ORANGE, ORANGE_TEXT),
]

t = doc.add_table(rows=1, cols=4); t.alignment = WD_TABLE_ALIGNMENT.CENTER
t.columns[0].width = Cm(2); t.columns[1].width = Cm(5.5)
t.columns[2].width = Cm(4.5); t.columns[3].width = Cm(6)
for i,h in enumerate(["Bloco","Descrição","Dias de disparo","Status"]):
    c = t.cell(0,i); set_cell_bg(c,DARK_BG)
    p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER; ps(p,5,5)
    run(p, h, bold=True, size=9, color=WHITE)

for bloco,desc,dias,status,bg,tc in overview:
    row = t.add_row()
    for i,txt in enumerate([bloco,desc,dias,status]):
        c = row.cells[i]; set_cell_bg(c, bg if i==3 else LIGHT_GRAY)
        p = c.paragraphs[0]; ps(p,4,4)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in (0,2) else WD_ALIGN_PARAGRAPH.LEFT
        run(p, txt if i==0 else f"  {txt}", bold=(i==0), size=9,
            color=tc if i==3 else DARK_TEXT)

spacer(doc,14)

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2 — CALENDÁRIO COMPLETO
# ══════════════════════════════════════════════════════════════════════════════
heading(doc, "📅  CALENDÁRIO COMPLETO DE DISPAROS")

cal = [
    ("D+0 (30min)",    "Lembrete pagamento pendente",          "Bloco 2", "30 min após agendamento sem pagamento confirmado"),
    ("D+1",            "2º lembrete pagamento pendente",        "Bloco 2", "Apenas se sem resposta no D+0"),
    ("D+7",            "Follow-up pós-consulta",                "Bloco 1", "Verificar evolução — abrir porta para reagendamento"),
    ("D+30",           "Check-in 1 mês",                        "Bloco 1", "Oferecer renovação ou nova consulta"),
    ("D+60",           "Manutenção de relacionamento",           "Bloco 1", "Só disparar se sem contato nos 30 dias anteriores"),
    ("D+90",           "Reativação — paciente dormente",         "Bloco 5", "Paciente sem nenhum contato por 90 dias"),
    ("D+120",          "Última tentativa de reativação",         "Bloco 5", "Só se não respondeu D+90 → marcar inativo se sem resposta"),
    ("A cada 60 dias", "Cuidado permanente (pós D+120)",         "Bloco 6", "Ciclo contínuo enquanto opt_out = false e status = ativo"),
    ("Renovação -10",  "Aviso renovação antecipado (60 dias)",   "Bloco 4", "Apenas pacientes com ciclo_renovacao = 60"),
    ("Renovação -7",   "Aviso renovação (30 dias)",              "Bloco 3", "Apenas pacientes com ciclo_renovacao = 30"),
    ("Renovação -5",   "2º aviso renovação (60 dias)",           "Bloco 4", "Se sem resposta ao D-10"),
    ("Renovação -3",   "2º aviso renovação (30 dias)",           "Bloco 3", "Se sem resposta ao D-7"),
    ("Renovação +3",   "Recuperação pós-vencimento (30 dias)",   "Bloco 3", "Receita venceu — oferecer renovação"),
    ("Renovação +5",   "Recuperação pós-vencimento (60 dias)",   "Bloco 4", "Receita venceu — oferecer renovação"),
    ("1º Jun",         "Sazonal — Inverno / gripes",             "Bloco 7", "Todos os pacientes ativos com opt_out = false"),
    ("1º Nov",         "Sazonal — Dengue / prevenção",           "Bloco 7", "Todos os pacientes ativos com opt_out = false"),
    ("1º Jan",         "Sazonal — Novo ano / check-up",          "Bloco 7", "Todos os pacientes ativos com opt_out = false"),
    ("7 Abr",          "Dia Mundial da Saúde",                   "Bloco 7", "Mensagem de valor puro — sem oferta comercial"),
    ("Aniversário",    "Mensagem de aniversário do paciente",    "Bloco 8", "Gatilho: data_nascimento = DIA+MÊS de hoje"),
    ("1 ano REMMED",   "Marco: 1 ano como paciente",             "Bloco 8", "Gatilho: data_cadastro = hoje - 365 dias"),
]

t = doc.add_table(rows=1, cols=4); t.alignment = WD_TABLE_ALIGNMENT.CENTER
t.columns[0].width = Cm(2.8); t.columns[1].width = Cm(5.7)
t.columns[2].width = Cm(2.5); t.columns[3].width = Cm(7)
for i,h in enumerate(["Dia/Momento","Evento","Bloco","Observação"]):
    c = t.cell(0,i); set_cell_bg(c,DARK_BG)
    p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER; ps(p,5,5)
    run(p, h, bold=True, size=9, color=WHITE)

alt = False
for dia,evento,bloco,obs in cal:
    row = t.add_row(); bg = MID_GRAY if alt else LIGHT_GRAY
    for i,txt in enumerate([dia,evento,bloco,obs]):
        c = row.cells[i]; set_cell_bg(c, bg)
        p = c.paragraphs[0]; ps(p,4,4)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in (0,2) else WD_ALIGN_PARAGRAPH.LEFT
        run(p, txt, bold=(i==0), size=8.5,
            color=BLUE_TEXT if i==2 else DARK_TEXT)
    alt = not alt

spacer(doc,14)

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 3 — MENSAGENS
# ══════════════════════════════════════════════════════════════════════════════
heading(doc, "💬  MENSAGENS — BLOCO A BLOCO")

# ── BLOCO 1 ──────────────────────────────────────────────────────────────────
block_title(doc,"🔵","BLOCO 1 — Pós-consulta geral",LIGHT_BLUE,BLUE_TEXT)
spacer(doc,6)

bubble(doc,"📅  D+7  —  Primeira mensagem após consulta", BLUE_TEXT,
    "Olá, [NOME]! 🧡 Como você está se sentindo desde a sua consulta?\n\n"
    "  Se melhorou → ótimo! Qualquer dúvida, estou aqui.\n"
    "  Se ainda não melhorou → posso te ajudar a agendar uma nova consulta, estou aqui para te ajudar.")
spacer(doc,3)
p = doc.add_paragraph(); ps(p,2,2)
run(p,"  Respostas automáticas:",bold=True,size=9,color=DARK_TEXT)
resp(doc,"👉  Paciente diz: melhorei",
         "✅  \"Que bom saber disso! Cuide-se, estou aqui sempre que precisar. 🌿\"",
     LIGHT_GREEN,LIGHT_GRAY)
spacer(doc,3)
resp(doc,"👉  Paciente menciona sintomas",
         "📅  \"Posso te ajudar a agendar uma nova consulta? O médico pode te auxiliar.\"  →  fluxo de agendamento",
     LIGHT_ORANGE,LIGHT_BLUE)
spacer(doc,8)

bubble(doc,"📅  D+30  —  Check-in 1 mês",BLUE_TEXT,
    "Oi, [NOME]! 🧡 Passando pra lembrar que faz 1 mês desde a sua consulta.\n\n"
    "  Como está sua saúde? Se quiser renovar receita, fazer check-up ou um novo atendimento,\n"
    "  posso organizar rapidinho pra você 😊")
spacer(doc,3)
resp(doc,"👉  Paciente responde SIM","📅  Direcionar para fluxo de agendamento",LIGHT_GREEN,LIGHT_BLUE)
spacer(doc,3)
resp(doc,"👉  Paciente diz não / tudo bem",
         "✅  \"Fico feliz que esteja bem! Estarei por aqui quando precisar. 🌿\"",
     LIGHT_GRAY,LIGHT_GRAY)
spacer(doc,8)

bubble(doc,"📅  D+60  —  Manutenção de relacionamento",BLUE_TEXT,
    "Olá, [NOME]! 🌿 Passando rapidinho pra saber como você está.\n\n"
    "  Se precisar de renovação de receita, acompanhamento ou quiser agendar uma consulta,\n"
    "  estou aqui pra te ajudar! 😊\n\n"
    "  ⚠️  Só disparar se sem contato nos últimos 30 dias.")
spacer(doc,10)

# ── BLOCO 2 ──────────────────────────────────────────────────────────────────
block_title(doc,"🔴","BLOCO 2 — Carrinho abandonado (agendou mas não pagou)",LIGHT_RED,RED_TEXT)
spacer(doc,6)

bubble(doc,"📅  D+0  (30 min após agendamento sem pagamento)",RED_TEXT,
    "Oi! 😊 Vi que você iniciou seu agendamento mas ainda não finalizou.\n\n"
    "  Você ainda gostaria de realizar sua consulta?\n"
    "  Posso te ajudar a concluir agora 😊",bg=LIGHT_RED)
spacer(doc,4)
bubble(doc,"📅  D+1  (manhã seguinte — sem resposta)",RED_TEXT,
    "Oi, [NOME]! Passando pra saber se você ainda quer realizar sua consulta. 🧡\n\n"
    "  Se precisar, posso te ajudar a organizar rapidinho.",bg=LIGHT_RED)
spacer(doc,3)
resp(doc,"👉  Paciente responde SIM","📅  Direcionar para fluxo de agendamento/pagamento",LIGHT_GREEN,LIGHT_BLUE)
spacer(doc,3)
resp(doc,"👉  Paciente responde NÃO","✅  \"Sem problema! Estaremos à disposição sempre que precisar. 🧡\"",LIGHT_GRAY,LIGHT_GRAY)
spacer(doc,10)

# ── BLOCO 3 ──────────────────────────────────────────────────────────────────
block_title(doc,"🟢","BLOCO 3 — Renovação de receita  |  Ciclo 30 dias",LIGHT_GREEN,GREEN_TEXT)
spacer(doc,4)
gatilho_line(doc,"proxima_renovacao = HOJE + 7  AND  ciclo_renovacao = 30  AND  opt_out = false",GREEN_TEXT)

bubble(doc,"📅  D-7  (7 dias antes do vencimento)",GREEN_TEXT,
    "Olá, [NOME]! 💊 Sua receita de [MEDICAMENTO] vence em 7 dias.\n\n"
    "  Quer renovar agora? Leva menos de 5 minutos e você já recebe a receita digital 😊\n\n"
    "  👉  Responda SIM que eu organizo tudo!",bg=LIGHT_GREEN)
spacer(doc,4)
bubble(doc,"📅  D-3  (3 dias antes — sem resposta ao D-7)",GREEN_TEXT,
    "Oi, [NOME]! 🧡 Só lembrando: sua receita vence em 3 dias.\n\n"
    "  Posso renovar agora, demora menos de 5 minutos!",bg=LIGHT_GREEN)
spacer(doc,4)
bubble(doc,"📅  D+3  (receita já vencida — recuperação)",GREEN_TEXT,
    "Oi, [NOME]! Percebi que sua receita de [MEDICAMENTO] pode ter vencido. 🧡\n\n"
    "  Sem problema — consigo renovar mesmo assim.\n"
    "  Quer que eu agende agora?",bg=LIGHT_GREEN)
spacer(doc,3)
resp(doc,"👉  SIM em qualquer mensagem","📅  Direcionar para fluxo de Renovação de Receita",LIGHT_GREEN,LIGHT_BLUE)
spacer(doc,10)

# ── BLOCO 4 ──────────────────────────────────────────────────────────────────
block_title(doc,"🟣","BLOCO 4 — Renovação de receita  |  Ciclo 60 dias",LIGHT_PURPLE,PURPLE_TEXT)
spacer(doc,4)
gatilho_line(doc,"proxima_renovacao = HOJE + 10  AND  ciclo_renovacao = 60  AND  opt_out = false",PURPLE_TEXT)

bubble(doc,"📅  D-10  (10 dias antes do vencimento)",PURPLE_TEXT,
    "Olá, [NOME]! 💊 Sua receita vence em 10 dias.\n\n"
    "  Quando quiser renovar, estou aqui — é rápido e você recebe tudo pelo celular 😊\n\n"
    "  👉  Responda SIM que eu organizo!",bg=LIGHT_PURPLE)
spacer(doc,4)
bubble(doc,"📅  D-5  (5 dias antes — sem resposta ao D-10)",PURPLE_TEXT,
    "Oi, [NOME]! 🧡 Sua receita vence em 5 dias.\n\n"
    "  Posso renovar agora, é bem rápido!",bg=LIGHT_PURPLE)
spacer(doc,4)
bubble(doc,"📅  D+5  (receita já vencida — recuperação)",PURPLE_TEXT,
    "Oi, [NOME]! Sua receita pode ter vencido esta semana. 🧡\n\n"
    "  Consigo renovar agora mesmo se quiser.\n"
    "  Só me responder que eu organizo!",bg=LIGHT_PURPLE)
spacer(doc,3)
resp(doc,"👉  SIM em qualquer mensagem","📅  Direcionar para fluxo de Renovação de Receita",LIGHT_GREEN,LIGHT_BLUE)
spacer(doc,10)

# ── BLOCO 5 ──────────────────────────────────────────────────────────────────
block_title(doc,"🟠","BLOCO 5 — Reativação de pacientes dormentes",LIGHT_ORANGE,ORANGE_TEXT)
spacer(doc,4)
gatilho_line(doc,"data_ultima_consulta = HOJE - 90  AND  opt_out = false  AND  ultimo_followup < HOJE - 30",ORANGE_TEXT)

bubble(doc,"📅  D+90  (90 dias sem contato)",ORANGE_TEXT,
    "Oi, [NOME]! 🧡 Faz um tempo que não nos falamos.\n\n"
    "  Como está sua saúde? Se precisar de qualquer coisa — consulta, renovação ou só\n"
    "  tirar uma dúvida — estamos aqui pra te ajudar 😊",bg=LIGHT_ORANGE)
spacer(doc,4)
bubble(doc,"📅  D+120  (última tentativa — sem resposta ao D+90)",ORANGE_TEXT,
    "Oi, [NOME]! Notamos que faz um tempo desde sua última consulta. 🧡\n\n"
    "  Quando quiser retomar seu acompanhamento, estamos aqui pra te atender\n"
    "  da melhor forma 😊",bg=LIGHT_ORANGE)
spacer(doc,3)
resp(doc,"👉  Sem resposta após D+120",
         "⚠️  Setar status_paciente = 'inativo' — parar envios do Bloco 5\n  ✅  Bloco 6 (Cuidado Permanente) continua ativo",
     LIGHT_RED,LIGHT_ORANGE)
spacer(doc,10)

# ── BLOCO 6 ──────────────────────────────────────────────────────────────────
block_title(doc,"💙","BLOCO 6 — Cuidado Permanente (a cada 60 dias — sem fim)",LIGHT_TEAL,TEAL_TEXT)
spacer(doc,4)

p = doc.add_paragraph(); ps(p,0,6)
run(p,"  💡  Filosofia: ", bold=True, size=9, color=TEAL_TEXT)
run(p,"70% valor para o paciente  +  30% oferta suave. Nunca começa com \"quer marcar consulta?\"",
    size=9, color=DARK_TEXT)

gatilho_line(doc,"ultimo_followup <= HOJE - 60  AND  opt_out = false  (sem limite de data)",TEAL_TEXT)

bubble(doc,"🔄  Mensagem padrão — Cuidado 60 dias",TEAL_TEXT,
    "Oi, [NOME]! 🧡 Passando pra saber como você está.\n\n"
    "  Se precisar de qualquer coisa — uma dúvida, renovação de receita ou nova consulta —\n"
    "  estou aqui. É sempre rápido por aqui! 😊",bg=LIGHT_TEAL)
spacer(doc,4)

bubble(doc,"🔄  Mensagem alternada — 120 dias (variação para não repetir)",TEAL_TEXT,
    "Oi, [NOME]! 🌿 Só passando pra lembrar que estamos aqui sempre que precisar.\n\n"
    "  Consulta, renovação de receita, dúvida rápida — tudo pelo celular, sem sair de casa 😊",bg=LIGHT_TEAL)
spacer(doc,4)

p = doc.add_paragraph(); ps(p,2,2)
run(p,"  ⚠️  Regra anti-spam: ", bold=True, size=9, color=TEAL_TEXT)
run(p,"Nunca disparar se já houve contato (qualquer tipo) nos últimos 30 dias. "
       "Verificar campo ultimo_followup antes de cada envio.", size=9, color=DARK_TEXT)
spacer(doc,10)

# ── BLOCO 7 ──────────────────────────────────────────────────────────────────
block_title(doc,"🌦️","BLOCO 7 — Sazonais (calendário fixo — todos os anos)",LIGHT_YELLOW,YELLOW_TEXT)
spacer(doc,4)

p = doc.add_paragraph(); ps(p,0,6)
run(p,"  💡  Esses disparos não dependem da data da consulta — rodam em datas fixas do calendário\n"
       "  para TODOS os pacientes ativos (opt_out = false). Máximo 1 disparo por campanha por paciente.",
    size=9, color=DARK_TEXT, italic=True)

bubble(doc,"❄️  1º de Junho — Inverno / gripes e resfriados",YELLOW_TEXT,
    "Oi, [NOME]! ❄️ O inverno chegou e com ele as gripes e resfriados aparecem mais.\n\n"
    "  Hidrate-se bem, mantenha a vitamina D em dia e, se aparecer qualquer sintoma,\n"
    "  não deixa pra depois — posso te ajudar a agendar em minutos! 🧡",bg=LIGHT_YELLOW)
spacer(doc,4)

bubble(doc,"🦟  1º de Novembro — Dengue / prevenção",YELLOW_TEXT,
    "Oi, [NOME]! 🦟 O verão está chegando e com ele o risco de dengue aumenta.\n\n"
    "  Elimine água parada em casa, use repelente e fique atento a: febre alta, dor atrás\n"
    "  dos olhos, manchas vermelhas.\n\n"
    "  Se precisar de atendimento rápido, estou aqui! 🧡",bg=LIGHT_YELLOW)
spacer(doc,4)

bubble(doc,"🎊  1º de Janeiro — Novo ano / check-up",YELLOW_TEXT,
    "Oi, [NOME]! 🎊 Feliz Ano Novo!\n\n"
    "  Que tal começar 2026 cuidando da saúde? Um check-up no início do ano ajuda a\n"
    "  identificar o que precisa de atenção antes de virar problema.\n\n"
    "  Se quiser agendar, estou aqui! 😊🧡",bg=LIGHT_YELLOW)
spacer(doc,4)

bubble(doc,"🌍  7 de Abril — Dia Mundial da Saúde",YELLOW_TEXT,
    "Oi, [NOME]! 🌍 Hoje é o Dia Mundial da Saúde.\n\n"
    "  Um lembrete singelo: cuidar da saúde não é só ir ao médico quando algo dói —\n"
    "  é também prevenir, descansar bem e ouvir o próprio corpo 🧡\n\n"
    "  Sempre que precisar, estamos aqui!",bg=LIGHT_YELLOW)
spacer(doc,10)

# ── BLOCO 8 ──────────────────────────────────────────────────────────────────
block_title(doc,"🎂","BLOCO 8 — Datas especiais do paciente",LIGHT_PINK,PINK_TEXT)
spacer(doc,4)

bubble(doc,"🎂  Aniversário do paciente",PINK_TEXT,
    "Feliz aniversário, [NOME]! 🎂🧡\n\n"
    "  Que este novo ano de vida traga muita saúde, leveza e realizações!\n\n"
    "  Quando precisar de qualquer coisa, estamos aqui pra cuidar de você 😊",bg=LIGHT_PINK)
spacer(doc,4)

p = doc.add_paragraph(); ps(p,2,4)
run(p,"  ⚡  Gatilho:  ", bold=True, size=9, color=PINK_TEXT)
run(p,"EXTRACT(MONTH FROM data_nascimento) = EXTRACT(MONTH FROM CURRENT_DATE)\n"
       "  AND EXTRACT(DAY FROM data_nascimento) = EXTRACT(DAY FROM CURRENT_DATE)\n"
       "  AND opt_out = false",
    size=8, color=DARK_TEXT, mono=True)
spacer(doc,6)

bubble(doc,"🏥  1 ano como paciente REMMED",PINK_TEXT,
    "Oi, [NOME]! 🧡 Faz exatamente 1 ano que você é paciente da REMMED!\n\n"
    "  Obrigada pela confiança — é muito bom poder fazer parte do cuidado da sua saúde 😊\n\n"
    "  Se precisar de qualquer coisa, estamos aqui!",bg=LIGHT_PINK)
spacer(doc,4)

p = doc.add_paragraph(); ps(p,2,4)
run(p,"  ⚡  Gatilho:  ", bold=True, size=9, color=PINK_TEXT)
run(p,"data_cadastro = CURRENT_DATE - INTERVAL '1 year'  AND  opt_out = false",
    size=8, color=DARK_TEXT, mono=True)
spacer(doc,10)

# ── OPT-OUT ───────────────────────────────────────────────────────────────────
block_title(doc,"⛔","REGRA GLOBAL — Opt-out (LGPD obrigatório)",LIGHT_RED,RED_TEXT)
spacer(doc,6)

p = doc.add_paragraph(); ps(p,2,4)
run(p,"  Palavras que ativam opt-out: ", bold=True, size=9, color=RED_TEXT)
run(p,'"pare"  "stop"  "não quero mais"  "remover"  "cancelar"  "para de me mandar"  "sair da lista"',
    size=8.5, color=DARK_TEXT, mono=True)

resp(doc,
    "Paciente envia qualquer palavra de opt-out",
    "1. Setar opt_out = true no Supabase\n"
    "  2. Parar TODOS os envios futuros (todos os blocos)\n"
    "  3. Responder: \"Entendido! Não enviarei mais mensagens. Se precisar, pode me chamar. 🧡\"",
    LIGHT_RED, LIGHT_GRAY)
spacer(doc,10)

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 4 — BANCO DE DADOS
# ══════════════════════════════════════════════════════════════════════════════
heading(doc, "🗄️  BANCO DE DADOS — CAMPOS NECESSÁRIOS NO SUPABASE")

p = doc.add_paragraph(); ps(p,0,6)
run(p,"  Tabela: clientes  |  Adicionar todos os campos abaixo que ainda não existem.",
    size=9, color=DARK_TEXT, italic=True)

db_row(doc,"Campo","Tipo","Descrição",header=True)
campos = [
    ("data_ultima_consulta",  "date",    "Base para todos os cálculos D+N — atualizar após cada consulta"),
    ("data_cadastro",         "date",    "Data que o paciente se cadastrou — base para '1 ano REMMED' (Bloco 8)"),
    ("data_nascimento",       "date",    "Para disparo do aniversário (Bloco 8) — já pode existir"),
    ("ciclo_renovacao",       "int",     "30 ou 60 — preencher quando paciente fizer renovação de receita"),
    ("proxima_renovacao",     "date",    "Calculado: data_ultima_consulta + ciclo_renovacao — atualizar após renovação"),
    ("medicamento_renovacao", "text",    "Nome do medicamento — personaliza mensagem dos Blocos 3 e 4"),
    ("opt_out",               "boolean", "false por padrão — setar true quando paciente pedir para parar"),
    ("ultimo_followup",       "date",    "Atualizar após CADA disparo — evita duplicidade e spam"),
    ("status_paciente",       "text",    "'ativo' por padrão — setar 'inativo' após D+120 sem resposta (Bloco 5)"),
]
for f,t,d in campos:
    db_row(doc, f, t, d)

spacer(doc,14)

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 5 — TRIGGERS N8N
# ══════════════════════════════════════════════════════════════════════════════
heading(doc, "⚡  N8N — TODOS OS TRIGGERS  (Schedule diário — 09h00)")

p = doc.add_paragraph(); ps(p,0,8)
run(p,"  Cada trigger = 1 nó Schedule no N8N. Roda 1x por dia.\n"
       "  Para cada linha retornada → enviar mensagem WhatsApp via Evolution API → atualizar ultimo_followup.",
    size=9, color=DARK_TEXT, italic=True)

triggers = [
    ("T1 — Bloco 1  D+7",
     "SELECT * FROM clientes WHERE data_ultima_consulta = CURRENT_DATE - 7 AND opt_out = false"),
    ("T2 — Bloco 1  D+30",
     "SELECT * FROM clientes WHERE data_ultima_consulta = CURRENT_DATE - 30 AND opt_out = false"),
    ("T3 — Bloco 1  D+60",
     "SELECT * FROM clientes WHERE data_ultima_consulta = CURRENT_DATE - 60 AND opt_out = false AND ultimo_followup < CURRENT_DATE - 30"),
    ("T4 — Bloco 2  30min",
     "SELECT * FROM agendamentos WHERE criado_em <= NOW() - INTERVAL '30 min' AND pagamento_confirmado = false AND opt_out = false"),
    ("T5 — Bloco 3  D-7",
     "SELECT * FROM clientes WHERE proxima_renovacao = CURRENT_DATE + 7 AND ciclo_renovacao = 30 AND opt_out = false"),
    ("T6 — Bloco 3  D-3",
     "SELECT * FROM clientes WHERE proxima_renovacao = CURRENT_DATE + 3 AND ciclo_renovacao = 30 AND opt_out = false"),
    ("T7 — Bloco 3  D+3",
     "SELECT * FROM clientes WHERE proxima_renovacao = CURRENT_DATE - 3 AND ciclo_renovacao = 30 AND opt_out = false"),
    ("T8 — Bloco 4  D-10",
     "SELECT * FROM clientes WHERE proxima_renovacao = CURRENT_DATE + 10 AND ciclo_renovacao = 60 AND opt_out = false"),
    ("T9 — Bloco 4  D-5",
     "SELECT * FROM clientes WHERE proxima_renovacao = CURRENT_DATE + 5 AND ciclo_renovacao = 60 AND opt_out = false"),
    ("T10 — Bloco 4  D+5",
     "SELECT * FROM clientes WHERE proxima_renovacao = CURRENT_DATE - 5 AND ciclo_renovacao = 60 AND opt_out = false"),
    ("T11 — Bloco 5  D+90",
     "SELECT * FROM clientes WHERE data_ultima_consulta = CURRENT_DATE - 90 AND opt_out = false AND status_paciente = 'ativo'"),
    ("T12 — Bloco 5  D+120",
     "SELECT * FROM clientes WHERE data_ultima_consulta = CURRENT_DATE - 120 AND opt_out = false AND status_paciente = 'ativo'"),
    ("T13 — Bloco 6  Cuidado 60d",
     "SELECT * FROM clientes WHERE ultimo_followup <= CURRENT_DATE - 60 AND opt_out = false AND status_paciente != 'removido'"),
    ("T14 — Bloco 7  Inverno",
     "SELECT * FROM clientes WHERE opt_out = false  -- Rodar manualmente em 01/06 todo ano"),
    ("T15 — Bloco 7  Dengue",
     "SELECT * FROM clientes WHERE opt_out = false  -- Rodar manualmente em 01/11 todo ano"),
    ("T16 — Bloco 7  Ano Novo",
     "SELECT * FROM clientes WHERE opt_out = false  -- Rodar manualmente em 01/01 todo ano"),
    ("T17 — Bloco 7  Dia Saúde",
     "SELECT * FROM clientes WHERE opt_out = false  -- Rodar manualmente em 07/04 todo ano"),
    ("T18 — Bloco 8  Aniversário",
     "SELECT * FROM clientes WHERE EXTRACT(MONTH FROM data_nascimento) = EXTRACT(MONTH FROM CURRENT_DATE) AND EXTRACT(DAY FROM data_nascimento) = EXTRACT(DAY FROM CURRENT_DATE) AND opt_out = false"),
    ("T19 — Bloco 8  1 ano REMMED",
     "SELECT * FROM clientes WHERE data_cadastro = CURRENT_DATE - INTERVAL '1 year' AND opt_out = false"),
]

for i,(tid,query) in enumerate(triggers):
    trig(doc, tid, query, alt=(i%2==1))
    spacer(doc,2)

spacer(doc,14)

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 6 — PRIORIDADES
# ══════════════════════════════════════════════════════════════════════════════
heading(doc, "🎯  PRIORIDADE DE IMPLEMENTAÇÃO")

prios = [
    ("1ª","Alta",   "Opt-out global (LGPD)",           "Obrigatório antes de qualquer disparo em produção"),
    ("2ª","Alta",   "Bloco 2 — Carrinho abandonado",    "ROI imediato — recupera pacientes que não pagaram"),
    ("3ª","Alta",   "Bloco 3 — Renovação 30 dias",      "Maior volume — receita recorrente garantida"),
    ("4ª","Alta",   "Bloco 8 — Aniversário",            "Mais fácil de implementar — impacto emocional enorme"),
    ("5ª","Média",  "Bloco 1 — Pós-consulta (ajustar)", "Melhorar mensagens existentes"),
    ("6ª","Média",  "Bloco 4 — Renovação 60 dias",      "Mesma lógica do Bloco 3, ciclo diferente"),
    ("7ª","Média",  "Bloco 6 — Cuidado Permanente",     "Retenção de longo prazo — diferencial REMMED"),
    ("8ª","Média",  "Bloco 7 — Sazonais",               "Fácil de implementar — alto engajamento"),
    ("9ª","Baixa",  "Bloco 5 — Reativação dormentes",   "Impacto de longo prazo"),
    ("10ª","Baixa", "Bloco 8 — 1 ano REMMED",           "Marco de relacionamento — implementar por último"),
]

t = doc.add_table(rows=1, cols=4); t.alignment = WD_TABLE_ALIGNMENT.CENTER
t.columns[0].width = Cm(1.5); t.columns[1].width = Cm(2)
t.columns[2].width = Cm(6); t.columns[3].width = Cm(8.5)
for i,h in enumerate(["Ordem","Prioridade","O que implementar","Motivo"]):
    c = t.cell(0,i); set_cell_bg(c,DARK_BG)
    p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER; ps(p,5,5)
    run(p, h, bold=True, size=9, color=WHITE)

pc = {"Alta":(LIGHT_RED,RED_TEXT),"Média":(LIGHT_ORANGE,ORANGE_TEXT),"Baixa":(LIGHT_GREEN,GREEN_TEXT)}
for i,(ordem,prio,o_que,motivo) in enumerate(prios):
    row = t.add_row(); bg = LIGHT_GRAY if i%2==0 else MID_GRAY
    pbg,ptc = pc[prio]
    for j,txt in enumerate([ordem,prio,o_que,motivo]):
        c = row.cells[j]; set_cell_bg(c, pbg if j==1 else bg)
        p = c.paragraphs[0]; ps(p,4,4)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j in (0,1) else WD_ALIGN_PARAGRAPH.LEFT
        run(p, txt, bold=(j<2), size=9, color=ptc if j==1 else DARK_TEXT)

spacer(doc,14)

# ── rodapé ────────────────────────────────────────────────────────────────────
t = doc.add_table(rows=1, cols=1); t.alignment = WD_TABLE_ALIGNMENT.CENTER
c = t.cell(0,0); set_cell_bg(c, DARK_BG)
p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER; ps(p,8,8)
run(p, "REMMED Telemedicina  •  Sistema Clara  •  Follow-up Automático v2.0  •  Maio 2026",
    size=8, color=RGBColor(0xA0,0xAE,0xBE))

out = "/home/user/clara-/FollowUp_Nicolas_v2.docx"
doc.save(out)
print(f"Saved: {out}")
