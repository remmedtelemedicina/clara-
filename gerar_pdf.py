from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── página ────────────────────────────────────────────────────────────────────
W, H = A4
M = 2*cm
doc = SimpleDocTemplate(
    "/home/user/clara-/FollowUp_Nicolas_v3.pdf",
    pagesize=A4,
    leftMargin=M, rightMargin=M,
    topMargin=M, bottomMargin=M,
)

# ── cores ─────────────────────────────────────────────────────────────────────
DARK_BG      = colors.HexColor("#1E2A3A")
REMMED_BLUE  = colors.HexColor("#1A73E8")
BLUE2        = colors.HexColor("#175DBE")
WHITE        = colors.white
LIGHT_BLUE   = colors.HexColor("#E8F0FE")
LIGHT_GREEN  = colors.HexColor("#E6F4EA")
LIGHT_ORANGE = colors.HexColor("#FEF3E2")
LIGHT_RED    = colors.HexColor("#FDEDED")
LIGHT_PURPLE = colors.HexColor("#F3E8FD")
LIGHT_TEAL   = colors.HexColor("#E0F5F1")
LIGHT_PINK   = colors.HexColor("#FCE4EC")
LIGHT_YELLOW = colors.HexColor("#FFF9E6")
LIGHT_GRAY   = colors.HexColor("#F8F9FA")
MID_GRAY     = colors.HexColor("#E8EAED")
DARK_TEXT    = colors.HexColor("#1E2A3A")
GREEN_TEXT   = colors.HexColor("#188038")
ORANGE_TEXT  = colors.HexColor("#B36B00")
RED_TEXT     = colors.HexColor("#C5221F")
PURPLE_TEXT  = colors.HexColor("#6A1B9A")
BLUE_TEXT    = colors.HexColor("#1A73E8")
TEAL_TEXT    = colors.HexColor("#007B6E")
PINK_TEXT    = colors.HexColor("#AD1457")
YELLOW_TEXT  = colors.HexColor("#7A5C00")
CODE_GREEN   = colors.HexColor("#A8D8A8")
CRON_BG      = colors.HexColor("#37475A")

# ── estilos ───────────────────────────────────────────────────────────────────
def sty(name, parent=None, **kw):
    base = ParagraphStyle(name)
    kw.setdefault('fontName', 'Helvetica')
    kw.setdefault('fontSize', 9)
    kw.setdefault('leading', 13)
    kw.setdefault('textColor', DARK_TEXT)
    kw.setdefault('spaceAfter', 2)
    for k,v in kw.items():
        setattr(base, k, v)
    return base

S_TITLE    = sty('title',   fontName='Helvetica-Bold', fontSize=15, textColor=WHITE,
                 alignment=TA_CENTER, leading=20)
S_META     = sty('meta',    fontSize=9, textColor=colors.HexColor("#5F6B7C"),
                 alignment=TA_CENTER, leading=12)
S_HEAD     = sty('head',    fontName='Helvetica-Bold', fontSize=11, textColor=WHITE,
                 alignment=TA_CENTER, leading=15)
S_BLK      = sty('blk',     fontName='Helvetica-Bold', fontSize=10.5, leading=14)
S_BODY     = sty('body',    fontSize=8.5, leading=12)
S_SMALL    = sty('small',   fontSize=7.5, leading=11)
S_CODE     = sty('code',    fontName='Courier', fontSize=7.5, leading=11, textColor=DARK_TEXT)
S_CODE_W   = sty('codew',   fontName='Courier', fontSize=7.5, leading=11, textColor=CODE_GREEN)
S_LABEL    = sty('label',   fontName='Helvetica-Bold', fontSize=8, leading=11)
S_CENTER   = sty('center',  fontSize=9, alignment=TA_CENTER, leading=13)
S_ITALIC   = sty('italic',  fontSize=8.5, leading=12, fontName='Helvetica-Oblique',
                 textColor=DARK_TEXT)

# ── helpers ───────────────────────────────────────────────────────────────────
TW = W - 2*M  # usable width

def sp(h=6): return Spacer(1, h)

def heading(text):
    t = Table([[Paragraph(text, S_HEAD)]], colWidths=[TW])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), REMMED_BLUE),
        ('TOPPADDING',    (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING',   (0,0), (-1,-1), 8),
        ('RIGHTPADDING',  (0,0), (-1,-1), 8),
    ]))
    return [t, sp(6)]

def dark_heading(text):
    t = Table([[Paragraph(text, S_TITLE)]], colWidths=[TW])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), DARK_BG),
        ('TOPPADDING',    (0,0), (-1,-1), 9),
        ('BOTTOMPADDING', (0,0), (-1,-1), 9),
    ]))
    return [t, sp(6)]

def block_title(text, bg, tc):
    s = sty(f'bt_{text[:6]}', fontName='Helvetica-Bold', fontSize=10.5, textColor=tc, leading=14)
    t = Table([[Paragraph(f"  {text}", s)]], colWidths=[TW])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('TOPPADDING',    (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    return [t, sp(5)]

def bubble(label, lc, msg, bg=LIGHT_GRAY):
    ls = sty(f'lb_{label[:4]}', fontName='Helvetica-Bold', fontSize=7.5, textColor=lc, leading=10)
    ms = sty(f'mb_{label[:4]}', fontSize=9, leading=13, textColor=DARK_TEXT)
    inner = Table([
        [Paragraph(label, ls)],
        [Paragraph(msg.replace("\n","<br/>"), ms)],
    ], colWidths=[TW - 0.5*cm])
    inner.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('TOPPADDING',    (0,0), (0,0), 5),
        ('BOTTOMPADDING', (0,1), (0,1), 7),
        ('LEFTPADDING',   (0,0), (-1,-1), 10),
        ('RIGHTPADDING',  (0,0), (-1,-1), 8),
        ('LINEWIDTH',  (0,0), (0,0), 0),
        ('LINEBEFORE', (0,0), (-1,-1), 3, lc),
    ]))
    return [inner, sp(4)]

def resp_row(cond, act, cbg=LIGHT_GREEN, abg=LIGHT_BLUE):
    cs = sty('rc', fontSize=8.5, leading=12, textColor=DARK_TEXT)
    as_ = sty('ra', fontSize=8.5, leading=12, textColor=DARK_TEXT)
    t = Table(
        [[Paragraph(f"  {cond}", cs), Paragraph(f"  {act}", as_)]],
        colWidths=[TW*0.40, TW*0.60]
    )
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), cbg),
        ('BACKGROUND', (1,0), (1,0), abg),
        ('TOPPADDING',    (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING',   (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    return [t, sp(4)]

def info_box(text, bg=LIGHT_ORANGE, tc=ORANGE_TEXT):
    s = sty(f'ib_{text[:4]}', fontSize=8, leading=12, textColor=tc,
            fontName='Helvetica-Oblique')
    t = Table([[Paragraph(text.replace("\n","<br/>"), s)]], colWidths=[TW])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('TOPPADDING',    (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING',   (0,0), (-1,-1), 10),
        ('RIGHTPADDING',  (0,0), (-1,-1), 10),
    ]))
    return [t, sp(5)]

def trig_row(tid, sql, cron, note="", alt=False):
    bg_id  = BLUE2 if alt else REMMED_BLUE
    bg_row = MID_GRAY if alt else LIGHT_GRAY
    id_s   = sty(f'tr_{tid[:3]}', fontName='Helvetica-Bold', fontSize=8, textColor=WHITE, leading=11)
    note_s = sty(f'tn_{tid[:3]}', fontSize=7, textColor=colors.HexColor("#FFD054"),
                 fontName='Helvetica-Oblique', leading=10)
    sql_s  = sty(f'ts_{tid[:3]}', fontName='Courier', fontSize=7, leading=10, textColor=DARK_TEXT)
    cr_s   = sty(f'tc_{tid[:3]}', fontName='Courier-Bold', fontSize=7.5, textColor=WHITE,
                 alignment=TA_CENTER, leading=11)
    id_cell = [Paragraph(f"  {tid}", id_s)]
    if note:
        id_cell.append(Paragraph(f"  ⚠ {note}", note_s))
    t = Table(
        [[id_cell, Paragraph(f"  {sql.replace(chr(10), '<br/>  ')}", sql_s),
          Paragraph(cron, cr_s)]],
        colWidths=[TW*0.235, TW*0.615, TW*0.15]
    )
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), bg_id),
        ('BACKGROUND', (1,0), (1,0), bg_row),
        ('BACKGROUND', (2,0), (2,0), DARK_BG),
        ('TOPPADDING',    (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING',   (0,0), (-1,-1), 5),
        ('RIGHTPADDING',  (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    return [t, sp(2)]

def db_field(field, tipo, desc, note="", header=False):
    if header:
        fs = sty('dbh', fontName='Helvetica-Bold', fontSize=8.5, textColor=WHITE,
                 alignment=TA_CENTER, leading=12)
        t = Table(
            [[Paragraph(field, fs), Paragraph(tipo, fs), Paragraph(desc, fs)]],
            colWidths=[TW*0.32, TW*0.14, TW*0.54]
        )
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), DARK_BG),
            ('TOPPADDING',    (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING',   (0,0), (-1,-1), 6),
        ]))
        return [t]
    f_s = sty('dbf', fontName='Courier', fontSize=8, leading=11, textColor=DARK_TEXT)
    t_s = sty('dbt', fontSize=8, leading=11, textColor=DARK_TEXT)
    d_s = sty('dbd', fontSize=8, leading=11, textColor=DARK_TEXT)
    n_s = sty('dbn', fontSize=7, leading=10, textColor=ORANGE_TEXT,
              fontName='Helvetica-Oblique')
    desc_cell = [Paragraph(f"  {desc}", d_s)]
    if note:
        desc_cell.append(Paragraph(f"  → {note}", n_s))
    t = Table(
        [[Paragraph(f"  {field}", f_s), Paragraph(f"  {tipo}", t_s), desc_cell]],
        colWidths=[TW*0.32, TW*0.14, TW*0.54]
    )
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_GRAY),
        ('TOPPADDING',    (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING',   (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, MID_GRAY),
    ]))
    return [t]

# ══════════════════════════════════════════════════════════════════════════════
story = []

# ── CABEÇALHO ─────────────────────────────────────────────────────────────────
story += dark_heading("🤖  CLARA — SISTEMA DE FOLLOW-UP  |  REMMED TELEMEDICINA")
story.append(Paragraph("Documento técnico para Nicolas  •  Estrutura completa de disparos automáticos",
    S_META))
story.append(sp(6))

meta = Table(
    [["Versão\n3.0", "Data\nMaio / 2026", "Responsável\nREMMED", "Status\n🟢 Pronto para implementar"]],
    colWidths=[TW/4]*4
)
meta.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,0), LIGHT_BLUE),
    ('BACKGROUND', (1,0), (1,0), LIGHT_GRAY),
    ('BACKGROUND', (2,0), (2,0), LIGHT_BLUE),
    ('BACKGROUND', (3,0), (3,0), LIGHT_GREEN),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING',    (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('FONTSIZE', (0,0), (-1,-1), 8.5),
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
    ('TEXTCOLOR', (0,0), (-1,-1), DARK_TEXT),
]))
story.append(meta)
story.append(sp(14))

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 1 — VISÃO GERAL
# ══════════════════════════════════════════════════════════════════════════════
story += heading("📋  VISÃO GERAL — O QUE SERÁ CONSTRUÍDO")

overview_data = [
    ["Bloco","Descrição","Dias de disparo","Status"],
    ["Bloco 1","Pós-consulta geral","D+7  •  D+30  •  D+60","✅ Existe — ajustar mensagens"],
    ["Bloco 2","Carrinho abandonado","30min  •  D+1","✅ Existe — OK"],
    ["Bloco 3","Renovação receita — 30d","D-7  •  D-3  •  D+3","🔴 Criar do zero"],
    ["Bloco 4","Renovação receita — 60d","D-10  •  D-5  •  D+5","🔴 Criar do zero"],
    ["Bloco 5","Reativação dormentes","D+90  •  D+120","🔴 Criar do zero"],
    ["Bloco 6","Cuidado permanente","A cada 60 dias — sem fim","🔴 Criar do zero"],
    ["Bloco 7","Sazonais — calendário fixo","Jun • Nov • Jan • 7Abr","🔴 Criar do zero"],
    ["Bloco 8","Datas especiais","Aniversário  •  1 ano REMMED","🔴 Criar do zero"],
    ["Global","Opt-out (LGPD)","Sempre ativo","🔴 Obrigatório"],
]
ov_styles = [
    TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BG),
        ('TEXTCOLOR',  (0,0), (-1,0), WHITE),
        ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',   (0,0), (-1,-1), 8.5),
        ('ALIGN',      (0,0), (0,-1), 'CENTER'),
        ('ALIGN',      (2,0), (2,-1), 'CENTER'),
        ('ALIGN',      (3,0), (3,-1), 'CENTER'),
        ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING',    (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING',   (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [LIGHT_GRAY, MID_GRAY]),
        ('BACKGROUND', (3,1), (3,2), LIGHT_GREEN),
        ('BACKGROUND', (3,3), (3,-2), LIGHT_RED),
        ('BACKGROUND', (3,-1), (3,-1), LIGHT_ORANGE),
        ('TEXTCOLOR',  (3,1), (3,2), GREEN_TEXT),
        ('TEXTCOLOR',  (3,3), (3,-2), RED_TEXT),
        ('TEXTCOLOR',  (3,-1), (3,-1), ORANGE_TEXT),
        ('FONTNAME',   (0,1), (0,-1), 'Helvetica-Bold'),
    ])
]
ov = Table(overview_data, colWidths=[TW*0.11, TW*0.30, TW*0.27, TW*0.32])
for s in ov_styles: ov.setStyle(s)
story.append(ov)
story.append(sp(14))

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2 — CALENDÁRIO
# ══════════════════════════════════════════════════════════════════════════════
story += heading("📅  CALENDÁRIO COMPLETO DE DISPAROS")

cal_data = [["Dia/Momento","Evento","Bloco","Observação"]]
cal_rows = [
    ("D+0 (30min)",    "Lembrete pagamento pendente",         "Bloco 2", "30min após agendamento sem pagamento"),
    ("D+1",            "2º lembrete pagamento pendente",       "Bloco 2", "Apenas se sem resposta no D+0"),
    ("D+7",            "Follow-up pós-consulta",               "Bloco 1", "Verificar evolução"),
    ("D+30",           "Check-in 1 mês",                       "Bloco 1", "Oferecer renovação ou nova consulta"),
    ("D+60",           "Manutenção de relacionamento",          "Bloco 1", "Só se sem contato nos 30 dias anteriores"),
    ("D+90",           "Reativação — paciente dormente",        "Bloco 5", "Sem contato por 90 dias"),
    ("D+120",          "Última tentativa reativação",           "Bloco 5", "Só se não respondeu D+90"),
    ("A cada 60d",     "Cuidado permanente",                    "Bloco 6", "Ciclo contínuo enquanto opt_out = false"),
    ("Renov. -10",     "Aviso renovação antecipado (60d)",      "Bloco 4", "ciclo_renovacao = 60"),
    ("Renov. -7",      "Aviso renovação (30d)",                 "Bloco 3", "ciclo_renovacao = 30"),
    ("Renov. -5",      "2º aviso renovação (60d)",              "Bloco 4", "Se sem resposta ao D-10"),
    ("Renov. -3",      "2º aviso renovação (30d)",              "Bloco 3", "Se sem resposta ao D-7"),
    ("Renov. +3",      "Recuperação pós-vencimento (30d)",      "Bloco 3", "Receita venceu"),
    ("Renov. +5",      "Recuperação pós-vencimento (60d)",      "Bloco 4", "Receita venceu"),
    ("1º Jun",         "Sazonal — Inverno / gripes",            "Bloco 7", "Cron: 0 9 1 6 *"),
    ("1º Nov",         "Sazonal — Dengue / prevenção",          "Bloco 7", "Cron: 0 9 1 11 *"),
    ("1º Jan",         "Sazonal — Novo ano / check-up",         "Bloco 7", "Cron: 0 9 1 1 *"),
    ("7 Abr",          "Dia Mundial da Saúde",                  "Bloco 7", "Cron: 0 9 7 4 *"),
    ("Aniversário",    "Mensagem de aniversário",               "Bloco 8", "data_nascimento = DIA+MÊS hoje"),
    ("1 ano REMMED",   "Marco: 1 ano como paciente",            "Bloco 8", "data_cadastro = hoje - 1 year"),
]
for row in cal_rows:
    cal_data.append(list(row))

cal = Table(cal_data, colWidths=[TW*0.15, TW*0.31, TW*0.13, TW*0.41])
cal.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), DARK_BG),
    ('TEXTCOLOR',  (0,0), (-1,0), WHITE),
    ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0), (-1,-1), 8),
    ('ALIGN',      (0,0), (0,-1), 'CENTER'),
    ('ALIGN',      (2,0), (2,-1), 'CENTER'),
    ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING',    (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('LEFTPADDING',   (0,0), (-1,-1), 5),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [LIGHT_GRAY, MID_GRAY]),
    ('FONTNAME',   (0,1), (0,-1), 'Helvetica-Bold'),
    ('TEXTCOLOR',  (2,1), (2,-1), BLUE_TEXT),
]))
story.append(cal)
story.append(sp(14))

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 3 — MENSAGENS
# ══════════════════════════════════════════════════════════════════════════════
story += heading("💬  MENSAGENS — BLOCO A BLOCO")

# BLOCO 1
story += block_title("🔵  BLOCO 1 — Pós-consulta geral", LIGHT_BLUE, BLUE_TEXT)
story += bubble("📅  D+7 — Primeira mensagem após consulta", BLUE_TEXT,
    "Olá, [NOME]! 🧡 Como você está se sentindo desde a sua consulta?\n\n"
    "Se melhorou → ótimo! Qualquer dúvida, estou aqui.\n"
    "Se ainda não melhorou → posso te ajudar a agendar uma nova consulta.", LIGHT_BLUE)
story += resp_row("👉 Paciente diz: melhorei",
    "✅ \"Que bom! Cuide-se, estou aqui sempre que precisar. 🌿\"", LIGHT_GREEN, LIGHT_GRAY)
story += resp_row("👉 Paciente menciona sintomas",
    "📅 \"Posso te ajudar a agendar uma nova consulta?\" → fluxo de agendamento", LIGHT_ORANGE, LIGHT_BLUE)
story += bubble("📅  D+30 — Check-in 1 mês", BLUE_TEXT,
    "Oi, [NOME]! 🧡 Passando pra lembrar que faz 1 mês desde a sua consulta.\n\n"
    "Como está sua saúde? Se quiser renovar receita, fazer check-up ou novo atendimento,\nposso organizar rapidinho 😊")
story += resp_row("👉 Paciente responde SIM", "📅 Direcionar para fluxo de agendamento", LIGHT_GREEN, LIGHT_BLUE)
story += resp_row("👉 Paciente diz não / tudo bem", "✅ \"Fico feliz! Estarei por aqui quando precisar. 🌿\"", LIGHT_GRAY, LIGHT_GRAY)
story += bubble("📅  D+60 — Manutenção de relacionamento", BLUE_TEXT,
    "Olá, [NOME]! 🌿 Passando rapidinho pra saber como você está.\n\n"
    "Se precisar de renovação, acompanhamento ou nova consulta, estou aqui! 😊\n\n"
    "⚠️ Só disparar se sem contato nos últimos 30 dias.")
story.append(sp(8))

# BLOCO 2
story += block_title("🔴  BLOCO 2 — Carrinho abandonado (agendou mas não pagou)", LIGHT_RED, RED_TEXT)
story += info_box(
    "⏱️ T4a (30min): Schedule cada 30min — não diário.  T4b (D+1): Schedule diário 09h.\n"
    "⚠️ Campo lembrete_enviado (boolean) na tabela agendamentos evita duplicatas no T4a.\n"
    "   T4a: AND lembrete_enviado = false → após envio setar lembrete_enviado = true.",
    LIGHT_ORANGE, ORANGE_TEXT)
story += bubble("📅  D+0 (30 min após agendamento sem pagamento)", RED_TEXT,
    "Oi! 😊 Vi que você iniciou seu agendamento mas ainda não finalizou.\n\n"
    "Você ainda gostaria de realizar sua consulta? Posso te ajudar a concluir agora 😊", LIGHT_RED)
story += bubble("📅  D+1 (manhã seguinte — sem resposta)", RED_TEXT,
    "Oi, [NOME]! Passando pra saber se você ainda quer realizar sua consulta. 🧡\n\n"
    "Se precisar, posso te ajudar a organizar rapidinho.", LIGHT_RED)
story += resp_row("👉 Paciente responde SIM", "📅 Direcionar para fluxo de agendamento/pagamento", LIGHT_GREEN, LIGHT_BLUE)
story += resp_row("👉 Paciente responde NÃO", "✅ \"Sem problema! Estaremos à disposição sempre que precisar. 🧡\"", LIGHT_GRAY, LIGHT_GRAY)
story.append(sp(8))

# BLOCO 3
story += block_title("🟢  BLOCO 3 — Renovação de receita  |  Ciclo 30 dias", LIGHT_GREEN, GREEN_TEXT)
story += info_box(
    "📋 Pré-requisito: medicamento_renovacao e ciclo_renovacao preenchidos.\n"
    "   Quem preenche: agente Clara (Renovação) via supabase_update_cliente após confirmar renovação.",
    LIGHT_GREEN, GREEN_TEXT)
story += bubble("📅  D-7 (7 dias antes do vencimento)", GREEN_TEXT,
    "Olá, [NOME]! 💊 Sua receita de [MEDICAMENTO] vence em 7 dias.\n\n"
    "Quer renovar agora? Leva menos de 5 minutos e você já recebe a receita digital 😊\n\n"
    "👉 Responda SIM que eu organizo tudo!", LIGHT_GREEN)
story += bubble("📅  D-3 (3 dias antes — sem resposta)", GREEN_TEXT,
    "Oi, [NOME]! 🧡 Só lembrando: sua receita vence em 3 dias. Posso renovar agora!", LIGHT_GREEN)
story += bubble("📅  D+3 (receita vencida — recuperação)", GREEN_TEXT,
    "Oi, [NOME]! Percebi que sua receita de [MEDICAMENTO] pode ter vencido. 🧡\n\n"
    "Sem problema — consigo renovar mesmo assim. Quer que eu agende agora?", LIGHT_GREEN)
story += resp_row("👉 SIM em qualquer mensagem", "📅 Direcionar para fluxo de Renovação de Receita", LIGHT_GREEN, LIGHT_BLUE)
story.append(sp(8))

# BLOCO 4
story += block_title("🟣  BLOCO 4 — Renovação de receita  |  Ciclo 60 dias", LIGHT_PURPLE, PURPLE_TEXT)
story += info_box("📋 Mesma lógica do Bloco 3 — diferença apenas no ciclo (60 dias) e janelas de aviso.",
    LIGHT_PURPLE, PURPLE_TEXT)
story += bubble("📅  D-10 (10 dias antes do vencimento)", PURPLE_TEXT,
    "Olá, [NOME]! 💊 Sua receita vence em 10 dias.\n\n"
    "Quando quiser renovar, estou aqui — é rápido e você recebe tudo pelo celular 😊\n\n"
    "👉 Responda SIM que eu organizo!", LIGHT_PURPLE)
story += bubble("📅  D-5 (5 dias antes — sem resposta)", PURPLE_TEXT,
    "Oi, [NOME]! 🧡 Sua receita vence em 5 dias. Posso renovar agora, é bem rápido!", LIGHT_PURPLE)
story += bubble("📅  D+5 (receita vencida — recuperação)", PURPLE_TEXT,
    "Oi, [NOME]! Sua receita pode ter vencido esta semana. 🧡\n\n"
    "Consigo renovar agora mesmo se quiser. Só me responder que eu organizo!", LIGHT_PURPLE)
story += resp_row("👉 SIM em qualquer mensagem", "📅 Direcionar para fluxo de Renovação de Receita", LIGHT_GREEN, LIGHT_BLUE)
story.append(sp(8))

# BLOCO 5
story += block_title("🟠  BLOCO 5 — Reativação de pacientes dormentes", LIGHT_ORANGE, ORANGE_TEXT)
story += info_box(
    "🔑 Lógica de dois estágios:\n"
    "D+90: disparo inicial → se paciente responde, setar respondeu_reativacao = true\n"
    "D+120: só dispara se respondeu_reativacao = false\n"
    "Após D+120 sem resposta → setar status_paciente = 'inativo'. Bloco 6 continua ativo.",
    LIGHT_ORANGE, ORANGE_TEXT)
story += bubble("📅  D+90 (90 dias sem contato)", ORANGE_TEXT,
    "Oi, [NOME]! 🧡 Faz um tempo que não nos falamos.\n\n"
    "Como está sua saúde? Se precisar de qualquer coisa — consulta, renovação ou dúvida\n— estamos aqui 😊", LIGHT_ORANGE)
story += bubble("📅  D+120 (última tentativa — apenas se não respondeu D+90)", ORANGE_TEXT,
    "Oi, [NOME]! Notamos que faz um tempo desde sua última consulta. 🧡\n\n"
    "Quando quiser retomar seu acompanhamento, estamos aqui 😊", LIGHT_ORANGE)
story += resp_row("👉 Sem resposta após D+120",
    "⚠️ status_paciente = 'inativo' — parar Bloco 5\n✅ Bloco 6 continua ativo indefinidamente",
    LIGHT_RED, LIGHT_ORANGE)
story.append(sp(8))

# BLOCO 6
story += block_title("💙  BLOCO 6 — Cuidado Permanente (a cada 60 dias — sem fim)", LIGHT_TEAL, TEAL_TEXT)
story += info_box(
    "💡 Filosofia: 70% valor para o paciente + 30% oferta suave.\n"
    "🔀 Alternância via campo contagem_bloco6:\n"
    "   contagem_bloco6 ÍMPAR → Mensagem A  |  PAR → Mensagem B\n"
    "   Após envio: incrementar contagem_bloco6 + 1 via supabase_update_cliente.",
    LIGHT_TEAL, TEAL_TEXT)
story += bubble("🔄  Mensagem A (envios 1, 3, 5...)", TEAL_TEXT,
    "Oi, [NOME]! 🧡 Passando pra saber como você está.\n\n"
    "Se precisar de qualquer coisa — dúvida, renovação ou nova consulta — estou aqui! 😊", LIGHT_TEAL)
story += bubble("🔄  Mensagem B (envios 2, 4, 6...)", TEAL_TEXT,
    "Oi, [NOME]! 🌿 Só passando pra lembrar que estamos aqui sempre que precisar.\n\n"
    "Consulta, renovação, dúvida rápida — tudo pelo celular, sem sair de casa 😊", LIGHT_TEAL)
story.append(sp(8))

# BLOCO 7
story += block_title("🌦️  BLOCO 7 — Sazonais (calendário fixo — todos os anos)", LIGHT_YELLOW, YELLOW_TEXT)
story += info_box(
    "⚙️ Criar 4 nós Schedule com Cron Expression no N8N — automático, zero intervenção manual.\n"
    "Inverno (1 Jun): 0 9 1 6 *   |   Dengue (1 Nov): 0 9 1 11 *\n"
    "Ano Novo (1 Jan): 0 9 1 1 *  |   Dia Saúde (7 Abr): 0 9 7 4 *\n"
    "SQL: SELECT * FROM clientes WHERE opt_out = false AND (ultimo_followup IS NULL OR ultimo_followup < CURRENT_DATE - 30)",
    LIGHT_YELLOW, YELLOW_TEXT)
story += bubble("❄️  1º de Junho — Inverno / gripes", YELLOW_TEXT,
    "Oi, [NOME]! ❄️ O inverno chegou e as gripes aparecem mais.\n\n"
    "Hidrate-se, mantenha a vitamina D em dia e se aparecer qualquer sintoma,\nnão deixa pra depois — posso te ajudar a agendar em minutos! 🧡", LIGHT_YELLOW)
story += bubble("🦟  1º de Novembro — Dengue / prevenção", YELLOW_TEXT,
    "Oi, [NOME]! 🦟 O verão está chegando — risco de dengue aumenta.\n\n"
    "Elimine água parada, use repelente e fique atento: febre alta, dor atrás dos olhos,\nmanchas vermelhas. Se precisar de atendimento rápido, estou aqui! 🧡", LIGHT_YELLOW)
story += bubble("🎊  1º de Janeiro — Novo ano / check-up", YELLOW_TEXT,
    "Oi, [NOME]! 🎊 Feliz Ano Novo!\n\n"
    "Que tal começar o ano cuidando da saúde? Um check-up ajuda a identificar o que\nprecisa de atenção antes de virar problema. Se quiser agendar, estou aqui! 😊🧡", LIGHT_YELLOW)
story += bubble("🌍  7 de Abril — Dia Mundial da Saúde", YELLOW_TEXT,
    "Oi, [NOME]! 🌍 Hoje é o Dia Mundial da Saúde.\n\n"
    "Cuidar da saúde não é só ir ao médico quando algo dói — é também prevenir,\ndescansar bem e ouvir o próprio corpo 🧡  Sempre que precisar, estamos aqui!", LIGHT_YELLOW)
story.append(sp(8))

# BLOCO 8
story += block_title("🎂  BLOCO 8 — Datas especiais do paciente", LIGHT_PINK, PINK_TEXT)
story += bubble("🎂  Aniversário do paciente", PINK_TEXT,
    "Feliz aniversário, [NOME]! 🎂🧡\n\n"
    "Que este novo ano de vida traga muita saúde, leveza e realizações!\n\n"
    "Quando precisar de qualquer coisa, estamos aqui pra cuidar de você 😊", LIGHT_PINK)
story += bubble("🏥  1 ano como paciente REMMED", PINK_TEXT,
    "Oi, [NOME]! 🧡 Faz exatamente 1 ano que você é paciente da REMMED!\n\n"
    "Obrigada pela confiança — é muito bom poder fazer parte do cuidado da sua saúde 😊\n\n"
    "Se precisar de qualquer coisa, estamos aqui!", LIGHT_PINK)
story.append(sp(8))

# OPT-OUT
story += block_title("⛔  REGRA GLOBAL — Opt-out (LGPD obrigatório)", LIGHT_RED, RED_TEXT)
story += info_box(
    'Palavras: "pare"  "stop"  "não quero mais"  "remover"  "cancelar"  "para de me mandar"  "sair da lista"',
    LIGHT_RED, RED_TEXT)
story += resp_row(
    "Paciente envia palavra de opt-out",
    "1. opt_out = true no Supabase\n2. Parar TODOS os envios futuros\n"
    "3. \"Entendido! Não enviarei mais mensagens. Se precisar, pode me chamar. 🧡\"",
    LIGHT_RED, LIGHT_GRAY)
story.append(sp(14))

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 4 — BANCO DE DADOS
# ══════════════════════════════════════════════════════════════════════════════
story += heading("🗄️  BANCO DE DADOS — CAMPOS NECESSÁRIOS NO SUPABASE")
story.append(Paragraph("  Tabela: clientes  |  Adicionar todos os campos que ainda não existem.",
    S_ITALIC))
story.append(sp(4))

story += db_field("Campo","Tipo","Descrição",header=True)
campos = [
    ("nome","text","Nome do paciente — personaliza [NOME]. Provavelmente já existe — confirmar.",""),
    ("data_ultima_consulta","date","Base para D+N — atualizar após cada consulta.",""),
    ("data_cadastro","date","Data primeiro cadastro — Bloco 8 '1 ano REMMED'.","DEFAULT NOW()"),
    ("data_nascimento","date","Aniversário — Bloco 8. Nullable.",""),
    ("ciclo_renovacao","int","30 ou 60 — preencher ao renovar receita.","Preenchido pelo agente Clara (Renovação)"),
    ("proxima_renovacao","date","Calculado: data_ultima_consulta + ciclo_renovacao.","Calculado e salvo pelo agente Clara"),
    ("medicamento_renovacao","text","Nome do medicamento — personaliza [MEDICAMENTO].","Preenchido pelo agente Clara (Renovação)"),
    ("opt_out","boolean","false por padrão — true = parar todos os disparos.","DEFAULT false"),
    ("ultimo_followup","date","Atualizar após CADA disparo — controle anti-spam.","Atualizar após todo envio"),
    ("status_paciente","text","Valores: 'ativo', 'inativo', 'removido'","DEFAULT 'ativo'"),
    ("respondeu_reativacao","boolean","true quando paciente responde ao D+90 — impede D+120.","DEFAULT false"),
    ("contagem_bloco6","int","Alternância mensagem A/B no Bloco 6. Ímpar=A, Par=B.","DEFAULT 0"),
]
for f,t,d,n in campos:
    story += db_field(f,t,d,note=n)
story.append(sp(8))

story.append(Paragraph("  Tabela: agendamentos  |  Adicionar campo para controle de duplicatas no Bloco 2.",
    S_ITALIC))
story.append(sp(4))
story += db_field("Campo","Tipo","Descrição",header=True)
story += db_field("lembrete_enviado","boolean",
    "Impede T4a disparar mais de uma vez no mesmo agendamento.",
    note="DEFAULT false  |  Setar true após envio T4a")
story.append(sp(14))

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 5 — TRIGGERS N8N
# ══════════════════════════════════════════════════════════════════════════════
story += heading("⚡  N8N — TODOS OS TRIGGERS")

# Cabeçalho da tabela de triggers
hdr = Table(
    [["Trigger ID", "SQL Query (Supabase)", "Cron N8N"]],
    colWidths=[TW*0.235, TW*0.615, TW*0.15]
)
hdr.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), DARK_BG),
    ('TEXTCOLOR',  (0,0), (-1,-1), WHITE),
    ('FONTNAME',   (0,0), (-1,-1), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0), (-1,-1), 8.5),
    ('ALIGN',      (0,0), (-1,-1), 'CENTER'),
    ('TOPPADDING',    (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(hdr)
story.append(sp(2))

triggers = [
    ("T1 — Bloco 1  D+7",
     "SELECT * FROM clientes\nWHERE data_ultima_consulta = CURRENT_DATE - 7\nAND opt_out = false",
     "0 9 * * *", "", False),
    ("T2 — Bloco 1  D+30",
     "SELECT * FROM clientes\nWHERE data_ultima_consulta = CURRENT_DATE - 30\nAND opt_out = false\nAND (ultimo_followup IS NULL OR ultimo_followup < CURRENT_DATE - 20)",
     "0 9 * * *", "", True),
    ("T3 — Bloco 1  D+60",
     "SELECT * FROM clientes\nWHERE data_ultima_consulta = CURRENT_DATE - 60\nAND opt_out = false\nAND (ultimo_followup IS NULL OR ultimo_followup < CURRENT_DATE - 30)",
     "0 9 * * *", "", False),
    ("T4a — Bloco 2  30min",
     "SELECT a.*, c.nome FROM agendamentos a\nJOIN clientes c ON c.id = a.cliente_id\nWHERE a.criado_em <= NOW() - INTERVAL '30 min'\nAND a.pagamento_confirmado = false\nAND a.lembrete_enviado = false\nAND c.opt_out = false",
     "*/30 * * * *", "Após envio: lembrete_enviado = true", True),
    ("T4b — Bloco 2  D+1",
     "SELECT a.*, c.nome FROM agendamentos a\nJOIN clientes c ON c.id = a.cliente_id\nWHERE DATE(a.criado_em) = CURRENT_DATE - 1\nAND a.pagamento_confirmado = false\nAND c.opt_out = false",
     "0 9 * * *", "", False),
    ("T5 — Bloco 3  D-7",
     "SELECT * FROM clientes\nWHERE proxima_renovacao = CURRENT_DATE + 7\nAND ciclo_renovacao = 30\nAND opt_out = false",
     "0 9 * * *", "", True),
    ("T6 — Bloco 3  D-3",
     "SELECT * FROM clientes\nWHERE proxima_renovacao = CURRENT_DATE + 3\nAND ciclo_renovacao = 30\nAND opt_out = false",
     "0 9 * * *", "", False),
    ("T7 — Bloco 3  D+3",
     "SELECT * FROM clientes\nWHERE proxima_renovacao = CURRENT_DATE - 3\nAND ciclo_renovacao = 30\nAND opt_out = false",
     "0 9 * * *", "", True),
    ("T8 — Bloco 4  D-10",
     "SELECT * FROM clientes\nWHERE proxima_renovacao = CURRENT_DATE + 10\nAND ciclo_renovacao = 60\nAND opt_out = false",
     "0 9 * * *", "", False),
    ("T9 — Bloco 4  D-5",
     "SELECT * FROM clientes\nWHERE proxima_renovacao = CURRENT_DATE + 5\nAND ciclo_renovacao = 60\nAND opt_out = false",
     "0 9 * * *", "", True),
    ("T10 — Bloco 4  D+5",
     "SELECT * FROM clientes\nWHERE proxima_renovacao = CURRENT_DATE - 5\nAND ciclo_renovacao = 60\nAND opt_out = false",
     "0 9 * * *", "", False),
    ("T11 — Bloco 5  D+90",
     "SELECT * FROM clientes\nWHERE data_ultima_consulta = CURRENT_DATE - 90\nAND opt_out = false\nAND status_paciente = 'ativo'\nAND (ultimo_followup IS NULL OR ultimo_followup < CURRENT_DATE - 30)",
     "0 9 * * *", "", True),
    ("T12 — Bloco 5  D+120",
     "SELECT * FROM clientes\nWHERE data_ultima_consulta = CURRENT_DATE - 120\nAND opt_out = false\nAND status_paciente = 'ativo'\nAND respondeu_reativacao = false",
     "0 9 * * *", "Após envio: status_paciente='inativo'", False),
    ("T13 — Bloco 6  60d",
     "SELECT * FROM clientes\nWHERE (ultimo_followup IS NULL OR ultimo_followup <= CURRENT_DATE - 60)\nAND opt_out = false\nAND status_paciente != 'removido'",
     "0 9 * * *", "Após envio: +1 em contagem_bloco6", True),
    ("T14 — Bloco 7  Inverno",
     "SELECT * FROM clientes\nWHERE opt_out = false\nAND (ultimo_followup IS NULL OR ultimo_followup < CURRENT_DATE - 30)",
     "0 9 1 6 *", "1º de Junho — automático", False),
    ("T15 — Bloco 7  Dengue",
     "SELECT * FROM clientes\nWHERE opt_out = false\nAND (ultimo_followup IS NULL OR ultimo_followup < CURRENT_DATE - 30)",
     "0 9 1 11 *", "1º de Novembro — automático", True),
    ("T16 — Bloco 7  Ano Novo",
     "SELECT * FROM clientes\nWHERE opt_out = false\nAND (ultimo_followup IS NULL OR ultimo_followup < CURRENT_DATE - 30)",
     "0 9 1 1 *", "1º de Janeiro — automático", False),
    ("T17 — Bloco 7  Dia Saúde",
     "SELECT * FROM clientes\nWHERE opt_out = false\nAND (ultimo_followup IS NULL OR ultimo_followup < CURRENT_DATE - 30)",
     "0 9 7 4 *", "7 de Abril — automático", True),
    ("T18 — Bloco 8  Aniversário",
     "SELECT * FROM clientes\nWHERE EXTRACT(MONTH FROM data_nascimento) = EXTRACT(MONTH FROM CURRENT_DATE)\nAND EXTRACT(DAY FROM data_nascimento) = EXTRACT(DAY FROM CURRENT_DATE)\nAND data_nascimento IS NOT NULL\nAND opt_out = false",
     "0 9 * * *", "", False),
    ("T19 — Bloco 8  1 ano REMMED",
     "SELECT * FROM clientes\nWHERE EXTRACT(MONTH FROM data_cadastro) = EXTRACT(MONTH FROM CURRENT_DATE)\nAND EXTRACT(DAY FROM data_cadastro) = EXTRACT(DAY FROM CURRENT_DATE)\nAND data_cadastro <= CURRENT_DATE - INTERVAL '1 year'\nAND opt_out = false",
     "0 9 * * *", "Blindado 29/fev bissextos", True),
]

for tid, sql, cron, note, alt in triggers:
    story += trig_row(tid, sql, cron, note=note, alt=alt)

story.append(sp(14))

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 6 — FLUXO N8N PADRÃO
# ══════════════════════════════════════════════════════════════════════════════
story += heading("⚙️  CONFIGURAÇÃO N8N — FLUXO PADRÃO POR TRIGGER")
story += info_box(
    "Cada trigger (T1-T19) segue o mesmo padrão. Criar um subworkflow padrão e reutilizar.",
    LIGHT_BLUE, BLUE_TEXT)
story.append(sp(5))

flow_data = [
    ["#","Nó N8N","O que fazer"],
    ["1","Schedule Trigger",
     "Cron conforme tabela. T4a: cada 30min. Sazonais (T14-T17): cron específico."],
    ["2","Supabase SELECT",
     "Executar SQL do trigger. Se retorno vazio → parar workflow."],
    ["3","Loop / SplitInBatches",
     "Para cada paciente retornado, executar passos 4-6."],
    ["4","Evolution API\n(HTTP Request)",
     "POST enviar WhatsApp. Substituir [NOME] e [MEDICAMENTO] com dados do item.\n"
     "URL: {{$env.EVOLUTION_API_URL}}/message/sendText/{{$env.INSTANCE}}\n"
     "Body: { \"number\": \"{{item.telefone}}\", \"text\": \"{{mensagem}}\" }"],
    ["5","Supabase UPDATE",
     "Atualizar ultimo_followup = CURRENT_DATE.\n"
     "T4a: lembrete_enviado = true\n"
     "T12 sem resposta: status_paciente = 'inativo'\n"
     "T13: contagem_bloco6 = contagem_bloco6 + 1"],
    ["6","Error Handler",
     "Log erros em tabela followup_erros (cliente_id, trigger_id, erro, criado_em)."],
]

flow = Table(flow_data, colWidths=[TW*0.05, TW*0.20, TW*0.75])
flow.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), DARK_BG),
    ('TEXTCOLOR',  (0,0), (-1,0), WHITE),
    ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
    ('BACKGROUND', (0,1), (0,-1), REMMED_BLUE),
    ('TEXTCOLOR',  (0,1), (0,-1), WHITE),
    ('FONTNAME',   (0,1), (0,-1), 'Helvetica-Bold'),
    ('BACKGROUND', (1,1), (1,-1), LIGHT_BLUE),
    ('FONTNAME',   (1,1), (1,-1), 'Helvetica-Bold'),
    ('TEXTCOLOR',  (1,1), (1,-1), BLUE_TEXT),
    ('ROWBACKGROUNDS', (2,1), (2,-1), [LIGHT_GRAY, MID_GRAY]),
    ('FONTSIZE', (0,0), (-1,-1), 8.5),
    ('ALIGN',   (0,0), (0,-1), 'CENTER'),
    ('VALIGN',  (0,0), (-1,-1), 'TOP'),
    ('TOPPADDING',    (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING',   (0,0), (-1,-1), 6),
]))
story.append(flow)
story.append(sp(8))

story += info_box(
    "📖  Referência Cron (formato Unix):  minuto  hora  dia  mês  dia_semana\n"
    "0 9 * * *    = Todo dia às 09h00           */30 * * * * = A cada 30 minutos\n"
    "0 9 1 6 *    = 1º de Junho às 09h          0 9 1 11 *   = 1º de Novembro às 09h\n"
    "0 9 1 1 *    = 1º de Janeiro às 09h        0 9 7 4 *    = 7 de Abril às 09h",
    DARK_BG, colors.HexColor("#A0CCFF"))
story.append(sp(14))

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 7 — SQL MIGRATION
# ══════════════════════════════════════════════════════════════════════════════
story += heading("🛠️  SQL — MIGRATION PARA CRIAR CAMPOS NO SUPABASE")

sql_text = (
    "-- Executar no SQL Editor do Supabase (uma vez)\n\n"
    "ALTER TABLE clientes\n"
    "  ADD COLUMN IF NOT EXISTS data_ultima_consulta   date,\n"
    "  ADD COLUMN IF NOT EXISTS data_cadastro          date DEFAULT CURRENT_DATE,\n"
    "  ADD COLUMN IF NOT EXISTS data_nascimento        date,\n"
    "  ADD COLUMN IF NOT EXISTS ciclo_renovacao        int,\n"
    "  ADD COLUMN IF NOT EXISTS proxima_renovacao      date,\n"
    "  ADD COLUMN IF NOT EXISTS medicamento_renovacao  text,\n"
    "  ADD COLUMN IF NOT EXISTS opt_out               boolean DEFAULT false NOT NULL,\n"
    "  ADD COLUMN IF NOT EXISTS ultimo_followup        date,\n"
    "  ADD COLUMN IF NOT EXISTS status_paciente        text    DEFAULT 'ativo' NOT NULL,\n"
    "  ADD COLUMN IF NOT EXISTS respondeu_reativacao   boolean DEFAULT false NOT NULL,\n"
    "  ADD COLUMN IF NOT EXISTS contagem_bloco6        int     DEFAULT 0 NOT NULL;\n\n"
    "ALTER TABLE agendamentos\n"
    "  ADD COLUMN IF NOT EXISTS lembrete_enviado boolean DEFAULT false NOT NULL;\n\n"
    "-- Índices para performance\n"
    "CREATE INDEX IF NOT EXISTS idx_clientes_ultimo_followup    ON clientes(ultimo_followup);\n"
    "CREATE INDEX IF NOT EXISTS idx_clientes_data_consulta      ON clientes(data_ultima_consulta);\n"
    "CREATE INDEX IF NOT EXISTS idx_clientes_proxima_renovacao  ON clientes(proxima_renovacao);\n"
    "CREATE INDEX IF NOT EXISTS idx_clientes_opt_out            ON clientes(opt_out);\n"
    "CREATE INDEX IF NOT EXISTS idx_clientes_status             ON clientes(status_paciente);\n\n"
    "-- Tabela de log de erros\n"
    "CREATE TABLE IF NOT EXISTS followup_erros (\n"
    "  id          bigserial PRIMARY KEY,\n"
    "  cliente_id  bigint REFERENCES clientes(id),\n"
    "  trigger_id  text,\n"
    "  erro        text,\n"
    "  criado_em   timestamptz DEFAULT NOW()\n"
    ");"
)

sql_table = Table([[Paragraph(sql_text.replace("\n","<br/>"), S_CODE_W)]], colWidths=[TW])
sql_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), DARK_BG),
    ('TOPPADDING',    (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING',   (0,0), (-1,-1), 14),
    ('RIGHTPADDING',  (0,0), (-1,-1), 14),
]))
story.append(sql_table)
story.append(sp(14))

# ══════════════════════════════════════════════════════════════════════════════
# SEÇÃO 8 — PRIORIDADES
# ══════════════════════════════════════════════════════════════════════════════
story += heading("🎯  PRIORIDADE DE IMPLEMENTAÇÃO")

prio_data = [["Ordem","Prioridade","O que implementar","Motivo"]]
prios = [
    ("1ª","Alta",   "Migration SQL (criar campos)",      "Rodar no Supabase antes de qualquer coisa"),
    ("2ª","Alta",   "Opt-out global (LGPD)",              "Obrigatório antes de qualquer disparo em produção"),
    ("3ª","Alta",   "Bloco 2 — Carrinho abandonado",      "ROI imediato — recupera quem não pagou"),
    ("4ª","Alta",   "Bloco 3 — Renovação 30 dias",        "Maior volume — receita recorrente garantida"),
    ("5ª","Alta",   "Bloco 8 — Aniversário",              "Fácil de implementar — impacto emocional enorme"),
    ("6ª","Média",  "Bloco 1 — Pós-consulta",             "Melhorar mensagens existentes"),
    ("7ª","Média",  "Bloco 4 — Renovação 60 dias",        "Mesma lógica Bloco 3, ciclo diferente"),
    ("8ª","Média",  "Bloco 6 — Cuidado Permanente",       "Retenção longo prazo — diferencial REMMED"),
    ("9ª","Média",  "Bloco 7 — Sazonais",                 "Fácil de implementar — alto engajamento"),
    ("10ª","Baixa", "Bloco 5 — Reativação dormentes",     "Impacto de longo prazo"),
    ("11ª","Baixa", "Bloco 8 — 1 ano REMMED",             "Marco de relacionamento"),
]
for row in prios:
    prio_data.append(list(row))

prio_colors = {"Alta": (LIGHT_RED, RED_TEXT), "Média": (LIGHT_ORANGE, ORANGE_TEXT), "Baixa": (LIGHT_GREEN, GREEN_TEXT)}
prio_table = Table(prio_data, colWidths=[TW*0.08, TW*0.11, TW*0.35, TW*0.46])
ts = TableStyle([
    ('BACKGROUND', (0,0), (-1,0), DARK_BG),
    ('TEXTCOLOR',  (0,0), (-1,0), WHITE),
    ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE',   (0,0), (-1,-1), 8.5),
    ('ALIGN',      (0,0), (1,-1), 'CENTER'),
    ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING',    (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('LEFTPADDING',   (0,0), (-1,-1), 5),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [LIGHT_GRAY, MID_GRAY]),
    ('FONTNAME',   (0,1), (1,-1), 'Helvetica-Bold'),
])
prio_table.setStyle(ts)
# color priority cells
for i, (_, prio, _, _) in enumerate(prios, start=1):
    bg, tc = prio_colors[prio]
    prio_table.setStyle(TableStyle([
        ('BACKGROUND', (1,i), (1,i), bg),
        ('TEXTCOLOR',  (1,i), (1,i), tc),
    ]))
story.append(prio_table)
story.append(sp(14))

# ── RODAPÉ ───────────────────────────────────────────────────────────────────
footer_s = sty('footer', fontSize=8, textColor=colors.HexColor("#A0AEBE"),
               alignment=TA_CENTER, leading=11)
footer = Table(
    [[Paragraph("REMMED Telemedicina  •  Sistema Clara  •  Follow-up Automático v3.0  •  Maio 2026",
                footer_s)]],
    colWidths=[TW]
)
footer.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), DARK_BG),
    ('TOPPADDING',    (0,0), (-1,-1), 9),
    ('BOTTOMPADDING', (0,0), (-1,-1), 9),
]))
story.append(footer)

# ── BUILD ─────────────────────────────────────────────────────────────────────
doc.build(story)
print("Saved: /home/user/clara-/FollowUp_Nicolas_v3.pdf")
