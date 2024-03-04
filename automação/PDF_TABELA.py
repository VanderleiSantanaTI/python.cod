from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors

viatura = "caminha"
placa = "bgf51232"
hodometro = 17232
num_patrim = "12562325"
su = "bc320"
tip_manut = "CORRETIVA"
sisAfetado = "FREIO"
pecas = [
    (5, "Filtro de óleo"),
    (8, "Pastilha de freio"),
    (3, "Vela de ignição"),
    (4, "Amortecedor dianteiro"),
    (2, "Bateria"),
    (6, "Pneu dianteiro"),
    (10, "Óleo do motor"),
    (7, "Correia dentada"),
    (3, "Lâmpada do farol"),
    (5, "Sensor de temperatura"),
    (4, "Palheta do limpador"),
    (6, "Disco de freio"),
    (2, "Filtro de ar"),
    (8, "Rolamento da roda"),
    (3, "Terminal da direção"),
    (7, "Bomba de combustível"),
    (5, "Sensor de oxigênio"),
    (4, "Junta do cabeçote"),
    (6, "Pistão"),
    (8, "Virabrequim"),
    (3, "Sensor de velocidade"),
    (5, "Radiador"),
    (4, "Coxim do motor"),
    (6, "Válvula termostática"),
    (2, "Sonda lambda"),
    (8, "Catalisador"),
    (3, "Filtro de combustível"),
    (6, "Bomba de água"),
    (5, "Reservatório de expansão"),
    (4, "Coletor de admissão"),
    (7, "Bomba de óleo"),
    (5, "Interruptor de pressão"),
    (3, "Tampa do radiador"),
    (6, "Jogo de juntas"),
    (8, "Compressor do ar-condicionado"),
    (4, "Cilindro mestre"),
    (6, "Sensor de freio ABS"),
    (2, "Interruptor de luz de freio"),
    (7, "Sensor de posição do virabrequim"),
    (5, "Atuador da marcha lenta"),
    (5, "Amortecedor traseiro"),
    (8, "Pastilha de freio traseira"),
    (3, "Sensor de estacionamento"),
    (4, "Disco de freio traseiro"),
    (2, "Sensor de ABS"),
    (6, "Mangueira do radiador"),
    (10, "Bomba d'água"),
    (7, "Alternador"),
    (3, "Compressor do ar-condicionado"),
    (5, "Coxim do câmbio"),
    (4, "Kit de embreagem"),
    (6, "Correia do alternador"),
    (2, "Tensor da correia"),
    (8, "Junta homocinética"),
    (3, "Kit de reparo da suspensão"),
    (7, "Bomba de direção hidráulica"),
]
totp = len(pecas)
somap = sum(qty for qty, _ in pecas)
servicos = [
    "Troca da pastilha de freio",
    "Troca de óleo do motor",
    "Alinhamento e balanceamento",
    "Substituição da correia dentada",
    "Troca das velas de ignição",
    "Reparo no sistema de suspensão",
    "Revisão do sistema de arrefecimento",
    "Manutenção do sistema de injeção eletrônica",
    "Troca do filtro de ar-condicionado",
    "Verificação do sistema de freios",
    "Substituição das lâmpadas dos faróis",
    "Alinhamento da direção",
    "Balanceamento das rodas",
    "Troca do filtro de combustível",
    "Inspeção dos pneus",
    "Troca do líquido de arrefecimento",
    "Reparo no sistema de escapamento",
    "Revisão da suspensão dianteira",
    "Troca do fluido de transmissão",
    "Manutenção do sistema de ignição",
    "Verificação da correia do alternador",
    "Ajuste do sistema de freio ABS",
    "Reparo no sistema de embreagem",
    "Troca dos amortecedores",
    "Substituição do filtro de cabine",
    "Revisão do sistema de direção assistida",
    "Limpeza do sistema de alimentação de combustível",
    "Troca da junta do cabeçote",
    "Inspeção do sistema de escapamento",
    "Reparo do sistema de ar-condicionado",
    "Verificação do sistema de transmissão",
    "Substituição da bomba de combustível",
    "Troca da válvula termostática",
    "Reparo no sistema elétrico",
    "Manutenção do sistema de refrigeração",
    "Troca dos discos de freio",
    "Verificação da folga das válvulas",
    "Revisão do sistema de partida",
    "Troca da correia do alternador",
    "Ajuste do freio de mão",
]
tots = len(servicos)


def generate_pdf(file_name):
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()
    # Criar um estilo baseado no estilo "Normal" com alinhamento justificado
    style = styles["Normal"]
    style.alignment = 0  # 0 para Esquerda, 1 para Centralizado, 2 para Direita, 3 para Justificado

    data = [
        ['Ordem de serviço N°                   Data:  '],
        ['VIATURA', 'EB/PLACA', 'HODÔMETRO', 'N° DE PATRIMÔNIO', 'SU'],
        [viatura, placa, hodometro, num_patrim, su],
        [f'MANUTENÇÃO: {tip_manut}'],
        [f'Sistema(s) afetado(s):  {sisAfetado}'],
        [Paragraph(f'Qtd e Peça(s) utilizada(s) na manutenção.<br/>'
                   f' total: {totp} e QT.total depeças: {somap}'),
         'null', f'Serviço(s) realizado(s). Total: {tots}', 'null'],
        [Paragraph('<br/>'.join([f'{qty} - {name}' for qty, name in pecas]), styles['Normal']), 'null',
         Paragraph('<br/>'.join(servicos), styles['Normal']), 'null']
    ]

    # Crie um estilo para a tabela
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 20),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 2, colors.green)])

    # Crie a tabela com os dados e o estilo
    table = Table(data)
    table.setStyle(style)

    # # Mesclar células
    table_style = TableStyle([('SPAN', (0, 0), (-1, 0)),
                              ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                              ('SPAN', (0, 3), (-1, 3)),  # forma de manutenção:
                              ('ALIGN', (0, 3), (-1, 3), 'LEFT'),
                              ('SPAN', (0, 4), (-1, 4)),  # Sistema(s) afetado(s):
                              ('SPAN', (0, 5), (1, 5)),  # cabeçalho peças e serviços
                              ('SPAN', (2, 5), (4, 5)),
                              ('SPAN', (0, 6), (1, 6)),  # peças e serviços
                              ('SPAN', (2, 6), (4, 6)),
                              ('VALIGN', (0, 6), (3, 6), 'TOP')  # alinhar em cima
                              ])  # (col, row)
    table.setStyle(table_style)

    # Crie o documento

    # Adicione a tabela ao conteúdo do documento
    content = [table]

    # Adicione o número da página no rodapé de cada página
    doc.build(content, onFirstPage=add_page_number, onLaterPages=add_page_number)


# Função para adicionar o número da página no rodapé
def add_page_number(canvas, doc):
    # Obtenha o número da página atual
    page_num = canvas.getPageNumber()
    # Obtenha o tamanho da página
    width, height = A4

    # Defina a fonte e o tamanho do número da página
    canvas.setFont("Helvetica", 9)
    # Posicione o número da página no rodapé (a 15 pontos do lado esquerdo e inferior da página)
    canvas.drawString(15, 20, f"Página {page_num}")


generate_pdf("tabela.pdf")
