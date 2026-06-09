"""Shared helpers for PDF generation."""
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

W, H = A4
LM = RM = 20 * mm
TM = 20 * mm
BM = 22 * mm
BW = W - LM - RM  # ~481.89 pt

NAVY   = colors.HexColor('#1B3A6B')
DK_GRN = colors.HexColor('#1B5E20')
DK_RED = colors.HexColor('#8B1A1A')
AMBER  = colors.HexColor('#E65100')
RED    = colors.HexColor('#B71C1C')
PURPLE = colors.HexColor('#4A148C')
LT_BLUE= colors.HexColor('#EEF4FF')
LT_GRN = colors.HexColor('#E8F5E9')
LT_PINK= colors.HexColor('#FFEBEE')
LT_AMB = colors.HexColor('#FFF8E1')
LT_GRAY= colors.HexColor('#F5F5F5')
LT_PRP = colors.HexColor('#F3E5F5')
MID_GRY= colors.HexColor('#BDBDBD')
WHITE  = colors.white
BLACK  = colors.black

def S(name, **kw):
    return ParagraphStyle(name, **kw)

_S = S  # alias

TH  = S('th',  fontName='Helvetica-Bold',        fontSize=8,   leading=10, textColor=WHITE)
TD  = S('td',  fontName='Helvetica',              fontSize=8,   leading=10, textColor=BLACK)
TDB = S('tdb', fontName='Helvetica-Bold',         fontSize=8,   leading=10, textColor=BLACK)
BOX = S('box', fontName='Helvetica',              fontSize=8,   leading=11, textColor=BLACK)
BODY= S('bod', fontName='Helvetica',              fontSize=8.5, leading=12, textColor=BLACK, alignment=TA_JUSTIFY)
BODL= S('bdl', fontName='Helvetica',              fontSize=8.5, leading=12, textColor=BLACK)
H2S = S('h2s', fontName='Helvetica-Bold',         fontSize=10,  leading=13, textColor=NAVY)
H3S = S('h3s', fontName='Helvetica-Bold',         fontSize=9,   leading=12, textColor=NAVY)
FOOT= S('ft',  fontName='Helvetica',              fontSize=7,   leading=9,  textColor=colors.HexColor('#444444'))

def sp(h=3):  return Spacer(1, h * mm)
def hr():     return HRFlowable(width=BW, thickness=0.5, color=MID_GRY)
def p(t):     return Paragraph(t, BODL)
def pj(t):    return Paragraph(t, BODY)
def h2(t):    return Paragraph(t, H2S)
def h3(t):    return Paragraph(t, H3S)
def bul(t, i=12): return Paragraph(f'• {t}', S('bl', fontName='Helvetica', fontSize=8.5, leading=12, leftIndent=i))
def arr(t, i=15): return Paragraph(f'→ {t}', S('ar', fontName='Helvetica', fontSize=8.5, leading=12, leftIndent=i))

def _hex(c):
    return f'{int(c.red*255):02X}{int(c.green*255):02X}{int(c.blue*255):02X}'

def sec_hdr(title, bg=NAVY):
    pp = Paragraph(title, S('sh', fontName='Helvetica-Bold', fontSize=11, leading=15, textColor=WHITE))
    t = Table([[pp]], colWidths=[BW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),
        ('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),8),
    ]))
    return t

def mk_tbl(hdrs, rows, cws, hbg=NAVY):
    data = [[Paragraph(h, TH) for h in hdrs]]
    for row in rows:
        data.append([Paragraph(str(c), TD) for c in row])
    t = Table(data, colWidths=cws, repeatRows=1)
    sty = [
        ('BACKGROUND',(0,0),(-1,0),hbg),
        ('GRID',(0,0),(-1,-1),0.4,MID_GRY),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
    ]
    for i in range(1,len(data)):
        if i%2==0: sty.append(('BACKGROUND',(0,i),(-1,i),LT_GRAY))
    t.setStyle(TableStyle(sty))
    return t

def info_box(title, lines, bc=NAVY, bg=LT_BLUE, tc=None, italic_title=True):
    if tc is None: tc = bc
    hx = _hex(tc)
    fmt = 'i' if italic_title else 'b'
    items = [Paragraph(f'<font color="#{hx}">■ </font><%s>%s</%s>' % (fmt,title,fmt),
                       S('it', fontName='Helvetica-BoldOblique', fontSize=8.5, leading=12, textColor=tc))]
    for ln in lines:
        items.append(Paragraph(ln, BOX))
    t = Table([[items]], colWidths=[BW-2])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('BOX',(0,0),(-1,-1),1.5,bc),
        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
    ]))
    return t

def mac(title, lines):  return info_box(title, lines, bc=NAVY, bg=LT_BLUE, tc=NAVY)
def peg(title, lines):  return info_box(title, lines, bc=RED,  bg=LT_PINK, tc=RED)
def atc(title, lines):  return info_box(title, lines, bc=AMBER,bg=LT_AMB,  tc=AMBER)
def prp(title, lines):  return info_box(title, lines, bc=PURPLE,bg=LT_PRP, tc=PURPLE)
def gab(ltr, lines):    return info_box(f'Gabarito: Alternativa {ltr}', lines, bc=DK_GRN, bg=LT_GRN, tc=DK_GRN)

def checklist(title, items_list):
    hx = _hex(DK_GRN)
    rows = [Paragraph(f'<font color="#{hx}">■ </font><b>{title}</b>',
                      S('cbt', fontName='Helvetica-Bold', fontSize=8.5, leading=12, textColor=DK_GRN))]
    for it in items_list:
        rows.append(Paragraph(f'■ {it}', BOX))
    t = Table([[rows]], colWidths=[BW-2])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),LT_GRN),
        ('BOX',(0,0),(-1,-1),1.5,DK_GRN),
        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
    ]))
    return t

def make_footer(txt):
    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 7)
        canvas.setFillColor(colors.HexColor('#444444'))
        y = BM - 8*mm
        canvas.drawString(LM, y, txt)
        canvas.drawRightString(W-RM, y, f'Pág. {doc.page}')
        canvas.restoreState()
    return footer

def q_block(label, qtext, opts, gab_ltr, comment):
    out = []
    out.append(Paragraph(f'<b>{label}: {qtext}</b>',
                         S('qt', fontName='Helvetica-Bold', fontSize=8.5, leading=12)))
    out.append(sp(1))
    for o in opts:
        out.append(Paragraph(o, S('qo', fontName='Helvetica', fontSize=8.5, leading=12, leftIndent=10)))
    out.append(sp(1))
    out.append(gab(gab_ltr, [comment]))
    out.append(sp(3))
    return out

def ni(num, bold, expl, i=15):
    return [
        Paragraph(f'<b>{num}. {bold}</b>', S('ni', fontName='Helvetica-Bold', fontSize=8.5, leading=12)),
        Paragraph(f'→ {expl}', S('ne', fontName='Helvetica', fontSize=8.5, leading=12, leftIndent=i)),
    ]
