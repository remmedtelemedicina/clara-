import sys
sys.path.insert(0, '/home/user/clara-')

from pdf_helpers import A4, LM, RM, TM, BM, make_footer
from gerar_sus_p1 import pages_1_to_24
from gerar_sus_p2 import pages_20_to_48
from reportlab.platypus import SimpleDocTemplate

OUT = '/home/user/clara-/MODULO1_SUS_VERSAO_FINAL_CORRIGIDO.pdf'

def main():
    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=LM, rightMargin=RM,
        topMargin=TM, bottomMargin=BM,
    )
    story = pages_1_to_24() + pages_20_to_48()
    footer = make_footer('Módulo 1 SUS — Praia Grande 001/2026 | IBAM | Atualizado mai/2026')
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f'Generated: {OUT}')

if __name__ == '__main__':
    main()
