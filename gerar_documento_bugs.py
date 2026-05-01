from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# ── Estilos globais ──────────────────────────────────────────────────────────
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)

def set_cell_bg(cell, hex_color):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def heading1(text, color_hex='1F3864'):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(16)
    r, g, b = bytes.fromhex(color_hex)
    run.font.color.rgb = RGBColor(r, g, b)
    return p

def heading2(text, color_hex='2E74B5'):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(13)
    r, g, b = bytes.fromhex(color_hex)
    run.font.color.rgb = RGBColor(r, g, b)
    return p

def heading3(text, color_hex='404040'):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(11)
    r, g, b = bytes.fromhex(color_hex)
    run.font.color.rgb = RGBColor(r, g, b)
    return p

def body(text, indent=0):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(indent * 0.3)
    p.add_run(text)
    return p

def label_block(label, content, label_color='C00000'):
    p = doc.add_paragraph()
    r_label = p.add_run(f'{label}: ')
    r_label.bold = True
    r, g, b = bytes.fromhex(label_color)
    r_label.font.color.rgb = RGBColor(r, g, b)
    r_content = p.add_run(content)
    r_content.font.name = 'Courier New'
    r_content.font.size = Pt(9)
    p.paragraph_format.left_indent = Inches(0.3)
    return p

def code_block(text, bg='F2F2F2'):
    # Use a table with 1 cell to simulate a code block
    table = doc.add_table(rows=1, cols=1)
    table.style = 'Table Grid'
    cell = table.rows[0].cells[0]
    set_cell_bg(cell, bg)
    cell.paragraphs[0].clear()
    for i, line in enumerate(text.strip().split('\n')):
        if i == 0:
            p = cell.paragraphs[0]
        else:
            p = cell.add_paragraph()
        run = p.add_run(line)
        run.font.name = 'Courier New'
        run.font.size = Pt(9)
    doc.add_paragraph()  # spacing after
    return table

def divider():
    p = doc.add_paragraph('─' * 80)
    p.runs[0].font.size = Pt(8)
    p.runs[0].font.color.rgb = RGBColor(0xCC, 0xCC, 0xCC)

def priority_badge(text, p=None):
    if p is None:
        p = doc.add_paragraph()
    run = p.add_run(f'  [{text}]  ')
    run.bold = True
    run.font.size = Pt(9)
    return p

# ════════════════════════════════════════════════════════════════════════════
# CAPA
# ════════════════════════════════════════════════════════════════════════════
doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('REMMED TELEMEDICINA')
run.bold = True
run.font.size = Pt(20)
run.font.color.rgb = RGBColor(0x1F, 0x38, 0x64)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('Correções de Bugs — Prompts do Sistema Clara')
run.font.size = Pt(14)
run.font.color.rgb = RGBColor(0x2E, 0x74, 0xB5)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('Documento técnico para Nicolas • Maio 2025')
run.font.size = Pt(11)
run.font.color.rgb = RGBColor(0x60, 0x60, 0x60)

doc.add_paragraph()

# Tabela resumo
heading2('Resumo Geral')
table = doc.add_table(rows=4, cols=3)
table.style = 'Table Grid'
headers = ['Prompt', 'Qtd. Bugs', 'Prioridade']
data = [
    ('TRIAGEM_MEDICA', '5', 'ALTA'),
    ('RENOVAR_EXAME', '8', 'ALTA'),
    ('CLARA', '7', 'MÉDIA'),
]
hdr_cells = table.rows[0].cells
for i, h in enumerate(headers):
    hdr_cells[i].text = h
    hdr_cells[i].paragraphs[0].runs[0].bold = True
    set_cell_bg(hdr_cells[i], '1F3864')
    hdr_cells[i].paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

colors = ['D6E4F0', 'FDEBD0', 'D5E8D4']
for i, (nome, qtd, prio) in enumerate(data):
    row = table.rows[i+1].cells
    row[0].text = nome
    row[1].text = qtd
    row[2].text = prio
    for c in row:
        set_cell_bg(c, colors[i])

doc.add_paragraph()
doc.add_page_break()

# ════════════════════════════════════════════════════════════════════════════
# SEÇÃO 1 — TRIAGEM_MEDICA
# ════════════════════════════════════════════════════════════════════════════
heading1('1. TRIAGEM_MEDICA — 5 Bugs')

# Bug T1
heading2('BUG T1 — MOMENTO 2 REPROVADO: setor errado')
body('Setor salvo como "HUMANO" mas deveria ser "ENCERRADO" para fechar o atendimento.')

heading3('SUBSTITUIR:')
code_block('⚠️ Se REPROVADO:\n  → atualizar_setor com setor = "HUMANO"', 'FFE0E0')

heading3('POR:')
code_block('⚠️ Se REPROVADO:\n  → atualizar_setor com setor = "ENCERRADO"', 'E0FFE0')

doc.add_paragraph()

# Bug T2
heading2('BUG T2 — ETAPA 3: loop infinito SIM/NÃO')
body('A resposta SIM e NÃO no loop de confirmação de dados ficam dentro do mesmo ETAPA 3, criando loop infinito. A branch NÃO precisa sair da etapa com um setor específico.')

heading3('SUBSTITUIR:')
code_block('ETAPA 3 — Confirmação\nSe NÃO → "Pode corrigir os dados"\n[aguarda nova resposta → volta ETAPA 3]', 'FFE0E0')

heading3('POR:')
code_block('ETAPA 3 — Confirmação\nSe NÃO → atualizar_setor com setor = "TRIAGEM_CORRECAO"\n         → "Por favor, informe o dado que deseja corrigir"\n         → ENCERRAR execução\n[próxima mensagem do paciente chega no setor TRIAGEM_CORRECAO → corrige e volta ao fluxo]', 'E0FFE0')

doc.add_paragraph()

# Bug T3
heading2('BUG T3 — VERIFICAÇÃO 14: path NÃO em loop')
body('Quando paciente não concorda com encaminhamento, o fluxo tenta reapresentar opções mas não atualiza o setor, causando loop.')

heading3('SUBSTITUIR (path NÃO):')
code_block('Se NÃO → "Entendo. Posso tentar outra abordagem..."\n[aguarda resposta]', 'FFE0E0')

heading3('POR:')
code_block('Se NÃO → atualizar_setor com setor = "TRIAGEM_OPCOES"\n         → "Entendo. Gostaria de discutir outras opções? (SIM/NÃO)"\n         → ENCERRAR execução', 'E0FFE0')

doc.add_paragraph()

# Bug T4
heading2('BUG T4 — VERIFICAÇÃO 5 / PASSO 2: redundância de coleta')
body('VERIFICAÇÃO 5 coleta celular e PASSO 2 coleta celular novamente. Remover a coleta duplicada.')

heading3('SUBSTITUIR (em PASSO 2):')
code_block('Passo 2: Coletar celular do paciente\n→ "Qual é o seu número de celular com DDD?"', 'FFE0E0')

heading3('POR:')
code_block('Passo 2: [REMOVIDO — celular já coletado em VERIFICAÇÃO 5]\n→ usar o celular já registrado no contexto', 'E0FFE0')

doc.add_paragraph()

# Bug T5
heading2('BUG T5 — VERIFICAÇÃO 0: "falta de ar" muito ampla')
body('"Falta de ar" sem qualificador encaminha para SAMU casos leves (ex: ansiedade, esforço físico). Adicionar qualificador de gravidade.')

heading3('SUBSTITUIR:')
code_block('- Falta de ar → ENCERRADO (orientar SAMU/UPA)', 'FFE0E0')

heading3('POR:')
code_block('- Falta de ar em repouso ou dificuldade para falar frases completas → ENCERRADO (orientar SAMU/UPA)', 'E0FFE0')

doc.add_page_break()

# ════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2 — RENOVAR_EXAME
# ════════════════════════════════════════════════════════════════════════════
heading1('2. RENOVAR_EXAME — 8 Bugs')

# Bug R1
heading2('BUG R1 — Triple "Se SIM" com setor errado no meio')
body('No fluxo de endereço há três blocos "Se SIM" consecutivos. O bloco do meio usa setor "RENOVACAO_EXAME_ENDERECO" que não existe — deveria ser "RENOVACAO_RECEITA_ENDERECO" (ou o setor correto da receita).')

heading3('SUBSTITUIR (bloco do meio):')
code_block('Se SIM → atualizar_setor com setor = "RENOVACAO_EXAME_ENDERECO"\n         → confirmar endereço com paciente', 'FFE0E0')

heading3('POR:')
code_block('Se SIM → atualizar_setor com setor = "RENOVACAO_RECEITA_ENDERECO"\n         → confirmar endereço com paciente', 'E0FFE0')

doc.add_paragraph()

# Bug R2
heading2('BUG R2 — Setores de endereço sem "aguardar retorno"')
body('Nos setores RENOVACAO_RECEITA_ENDERECO e RENOVACAO_EXAME_ENDERECO o fluxo não encerra a execução aguardando resposta do paciente — continua processando sem input.')

heading3('SUBSTITUIR (em cada setor de endereço):')
code_block('→ "Qual é o seu endereço completo?"\n[sem ENCERRAR]', 'FFE0E0')

heading3('POR:')
code_block('→ "Qual é o seu endereço completo (rua, número, bairro, cidade)?"\n→ ENCERRAR execução e aguardar retorno do paciente', 'E0FFE0')

doc.add_paragraph()

# Bug R3
heading2('BUG R3 — Sub-etapa R2 inline sem setor')
body('A Sub-etapa R2 está embutida dentro de outro bloco sem atualizar o setor, impossibilitando retomar o fluxo se a execução for interrompida.')

heading3('SUBSTITUIR:')
code_block('[Sub-etapa R2 inline dentro do bloco anterior]\n→ processar dados\n→ continuar fluxo', 'FFE0E0')

heading3('POR:')
code_block('→ atualizar_setor com setor = "RENOVACAO_SUB_R2"\n→ ENCERRAR execução\n\n[Quando paciente responder, setor = RENOVACAO_SUB_R2]\n→ processar dados\n→ continuar fluxo', 'E0FFE0')

doc.add_paragraph()

# Bug R4
heading2('BUG R4 — RENOVACAO_RECEITA_PAGAMENTO sem retry')
body('Se o pagamento falhar, o fluxo não prevê tentativa de reenvio do link ou fallback — o paciente fica sem resposta.')

heading3('SUBSTITUIR:')
code_block('→ gerar_cobranca_direta\n→ "Seu link de pagamento: {link}"', 'FFE0E0')

heading3('POR:')
code_block('→ gerar_cobranca_direta\nSe SUCESSO:\n  → "Seu link de pagamento: {link}. Válido por 30 minutos."\n  → atualizar_setor com setor = "RENOVACAO_AGUARDANDO_PAGAMENTO"\n  → ENCERRAR execução\nSe ERRO:\n  → "Tive um problema ao gerar seu link. Tente novamente em instantes ou entre em contato conosco."\n  → atualizar_setor com setor = "HUMANO"\n  → ENCERRAR execução', 'E0FFE0')

doc.add_paragraph()

# Bug R5
heading2('BUG R5 — Sem confirmação antes do pagamento')
body('O sistema gera cobrança sem confirmar com o paciente o valor e o método. Risco de cobrar sem consentimento explícito.')

heading3('INSERIR antes de gerar_cobranca_direta:')
code_block('→ atualizar_setor com setor = "RENOVACAO_CONFIRMA_PAGAMENTO"\n→ "O valor da renovação é R$ {valor}. Deseja pagar via PIX ou cartão de crédito?"\n→ ENCERRAR execução\n\n[Quando paciente responder]\n→ processar escolha\n→ gerar_cobranca_direta com método escolhido', 'E0FFE0')

doc.add_paragraph()

# Bug R6
heading2('BUG R6 — "escalar_humano" tool não existe')
body('O prompt chama uma tool chamada "escalar_humano" que não está cadastrada no N8N. Substituir pela sequência correta.')

heading3('SUBSTITUIR (todas as ocorrências):')
code_block('→ escalar_humano', 'FFE0E0')

heading3('POR:')
code_block('→ atualizar_setor com setor = "HUMANO"\n→ "Vou transferir você para um atendente. Aguarde um momento."\n→ ENCERRAR execução', 'E0FFE0')

doc.add_paragraph()

# Bug R7
heading2('BUG R7 — Comparação de nome antes da coleta de dados (RENOVACAO_RECEITA_PDF)')
body('O fluxo compara o nome do PDF com dados do paciente antes de ter coletado esses dados. Para pacientes novos isso causa erro. A coleta deve acontecer primeiro.')

heading3('SUBSTITUIR (ordem atual):')
code_block('1. Analisar PDF\n2. Comparar nome do PDF com nome do paciente\n3. Coletar dados do paciente', 'FFE0E0')

heading3('POR:')
code_block('1. Analisar PDF\n2. Coletar dados do paciente (se ainda não coletados)\n3. Comparar nome do PDF com nome do paciente cadastrado', 'E0FFE0')

doc.add_paragraph()

# Bug R8
heading2('BUG R8 — "Enviar em mensagem SEPARADA" não funciona no N8N')
body('A instrução "Enviar em mensagem separada" não é suportada pela arquitetura de saída única do N8N/Evolution API. Cada execução gera apenas uma mensagem de saída.')

heading3('SUBSTITUIR (todas as ocorrências de "mensagem separada"):')
code_block('→ "Enviar em mensagem SEPARADA: {conteúdo}"', 'FFE0E0')

heading3('POR:')
code_block('→ Incluir o conteúdo na mesma mensagem, separado por linha em branco:\n   "[texto anterior]\n   \n   {conteúdo que seria separado}"', 'E0FFE0')

doc.add_page_break()

# ════════════════════════════════════════════════════════════════════════════
# SEÇÃO 3 — CLARA
# ════════════════════════════════════════════════════════════════════════════
heading1('3. CLARA — 7 Bugs')

# Bug C1
heading2('BUG C1 — FILTRO 1: idade inconsistente')
body('A condição do FILTRO 1 diz "< 4 anos" mas a mensagem enviada ao paciente diz "< 5 anos". Alinhar para 5 anos (padrão pediátrico).')

heading3('SUBSTITUIR (condição do filtro):')
code_block('Se idade < 4 anos → redirecionar para pediatra', 'FFE0E0')

heading3('POR:')
code_block('Se idade < 5 anos → redirecionar para pediatra', 'E0FFE0')

doc.add_paragraph()

# Bug C2
heading2('BUG C2 — FILTRO 3: "febre há 3 dias" listada como SAMU')
body('"Febre há mais de 3 dias" não é emergência SAMU — é urgência de UPA ou consulta. Mover para o fluxo de triagem normal.')

heading3('SUBSTITUIR (em FILTRO 3):')
code_block('Emergências SAMU:\n- Febre há mais de 3 dias\n- Dor no peito\n- Convulsão\n...', 'FFE0E0')

heading3('POR:')
code_block('Emergências SAMU:\n- Dor no peito\n- Convulsão\n- [demais emergências reais]\n\nUrgências (encaminhar para UPA ou triagem):\n- Febre há mais de 3 dias sem melhora', 'E0FFE0')

doc.add_paragraph()

# Bug C3
heading2('BUG C3 — FILTRO 4: validação de dados biológicos não pertence à Clara')
body('FILTRO 4 valida dados biológicos (peso, altura, etc.). Essa responsabilidade é da TRIAGEM_MEDICA. Na Clara isso cria redundância e possível conflito de fluxo.')

heading3('AÇÃO:')
body('Remover FILTRO 4 completamente do prompt da CLARA.', 1)
body('Garantir que TRIAGEM_MEDICA realiza essa validação (já consta no prompt da Triagem).', 1)

doc.add_paragraph()

# Bug C4
heading2('BUG C4 — FILTRO 5: rótulo "PRIORIDADE MÁXIMA" em posição errada')
body('FILTRO 5 está rotulado como "PRIORIDADE MÁXIMA" mas é o 5º na ordem de execução. Se é máxima prioridade, deve ser FILTRO 1 ou o rótulo deve ser corrigido.')

heading3('SUBSTITUIR:')
code_block('FILTRO 5 — PRIORIDADE MÁXIMA\n...', 'FFE0E0')

heading3('POR (opção A — mover para topo):')
code_block('FILTRO 1 — PRIORIDADE MÁXIMA\n[conteúdo atual do FILTRO 5]\n\nFILTRO 2 — [conteúdo atual do FILTRO 1]\n...', 'E0FFE0')

heading3('POR (opção B — corrigir rótulo):')
code_block('FILTRO 5 — Verificação de contexto\n[manter posição, remover "PRIORIDADE MÁXIMA"]', 'E0FFE0')

doc.add_paragraph()

# Bug C5
heading2('BUG C5 — FILTRO 2 (atestado): código morto')
body('FILTRO 2 verifica insistência sobre atestado mas esse caminho nunca é atingido no fluxo atual. É código morto.')

heading3('AÇÃO:')
body('Remover FILTRO 2 completamente, ou mover a lógica para o agente correto que trata atestados.', 1)

doc.add_paragraph()

# Bug C6
heading2('BUG C6 — Opção "6" (aguardar 1 turno): impossível no N8N')
body('A opção "6" no menu promete "aguardar 1 turno" mas não existe mecanismo de fila/turno na arquitetura atual do N8N. Cada execução é independente.')

heading3('SUBSTITUIR:')
code_block('Opção 6: Aguardar 1 turno para ser atendido', 'FFE0E0')

heading3('POR:')
code_block('Opção 6: Falar com um atendente humano\n→ atualizar_setor com setor = "HUMANO"\n→ "Transferindo para atendimento humano. Aguarde."', 'E0FFE0')

doc.add_paragraph()

# Bug C7
heading2('BUG C7 — Regra ansiedade/depressão na FAQ: código morto')
body('A regra de ansiedade/depressão está na seção FAQ mas nunca é acessada pelo fluxo de roteamento. Mover para TRIAGEM_MEDICA ou remover.')

heading3('AÇÃO:')
body('Remover a regra de ansiedade/depressão da seção FAQ da CLARA.', 1)
body('Se necessário tratar esses casos, adicionar como condição dentro do prompt TRIAGEM_MEDICA.', 1)

doc.add_page_break()

# ════════════════════════════════════════════════════════════════════════════
# TABELA DE PRIORIDADE PARA NICOLAS
# ════════════════════════════════════════════════════════════════════════════
heading1('4. Ordem de Implementação para Nicolas')

doc.add_paragraph('Implementar nesta ordem para evitar dependências entre correções:')

table = doc.add_table(rows=21, cols=4)
table.style = 'Table Grid'

headers_row = ['Ordem', 'Bug ID', 'Prompt', 'Descrição']
hdr = table.rows[0].cells
for i, h in enumerate(headers_row):
    hdr[i].text = h
    hdr[i].paragraphs[0].runs[0].bold = True
    set_cell_bg(hdr[i], '1F3864')
    hdr[i].paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

bugs = [
    ('1', 'T6 (escalar_humano)', 'RENOVAR_EXAME', 'Tool inexistente → atualizar_setor HUMANO'),
    ('2', 'T1', 'TRIAGEM_MEDICA', 'MOMENTO 2 REPROVADO → setor ENCERRADO'),
    ('3', 'R4', 'RENOVAR_EXAME', 'Pagamento sem retry nem fallback'),
    ('4', 'R5', 'RENOVAR_EXAME', 'Cobrança sem confirmação prévia do paciente'),
    ('5', 'R1', 'RENOVAR_EXAME', 'Triple SIM com setor errado no meio'),
    ('6', 'R2', 'RENOVAR_EXAME', 'Setores de endereço sem ENCERRAR execução'),
    ('7', 'R3', 'RENOVAR_EXAME', 'Sub-etapa R2 inline sem setor'),
    ('8', 'R7', 'RENOVAR_EXAME', 'Comparação de nome antes de coletar dados'),
    ('9', 'R8', 'RENOVAR_EXAME', '"Mensagem separada" não funciona no N8N'),
    ('10', 'T2', 'TRIAGEM_MEDICA', 'ETAPA 3 loop SIM/NÃO'),
    ('11', 'T3', 'TRIAGEM_MEDICA', 'VERIFICAÇÃO 14 path NÃO em loop'),
    ('12', 'T4', 'TRIAGEM_MEDICA', 'Coleta de celular duplicada'),
    ('13', 'T5', 'TRIAGEM_MEDICA', '"Falta de ar" muito ampla → qualificar'),
    ('14', 'C3', 'CLARA', 'Remover FILTRO 4 (dados biológicos)'),
    ('15', 'C5', 'CLARA', 'Remover FILTRO 2 (código morto)'),
    ('16', 'C7', 'CLARA', 'Remover regra ansiedade/depressão da FAQ'),
    ('17', 'C1', 'CLARA', 'FILTRO 1: corrigir idade de 4 para 5 anos'),
    ('18', 'C2', 'CLARA', 'FILTRO 3: mover febre para urgência'),
    ('19', 'C4', 'CLARA', 'FILTRO 5: corrigir rótulo PRIORIDADE MÁXIMA'),
    ('20', 'C6', 'CLARA', 'Opção 6: substituir "aguardar turno" por HUMANO'),
]

row_colors = ['FFFFFF', 'F5F5F5']
for i, (ordem, bug_id, prompt, desc) in enumerate(bugs):
    row = table.rows[i+1].cells
    row[0].text = ordem
    row[1].text = bug_id
    row[2].text = prompt
    row[3].text = desc
    for c in row:
        set_cell_bg(c, row_colors[i % 2])

doc.add_paragraph()
doc.add_paragraph()

# Nota final
p = doc.add_paragraph()
run = p.add_run('Observação: ')
run.bold = True
run.font.color.rgb = RGBColor(0xC0, 0x00, 0x00)
p.add_run('Os bugs de maior risco (T6, T1, R4, R5) devem ser corrigidos antes de qualquer teste em produção. Os demais podem ser implementados em paralelo após esses.')

doc.add_paragraph()
p = doc.add_paragraph()
run = p.add_run('Documento gerado automaticamente por análise de IA — REMMED Telemedicina — Maio 2025')
run.font.size = Pt(9)
run.font.color.rgb = RGBColor(0x90, 0x90, 0x90)
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Salvar
doc.save('/home/user/clara-/Bugs_Correccoes_Nicolas.docx')
print('Documento criado com sucesso!')
