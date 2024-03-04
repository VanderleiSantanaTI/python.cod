from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

placa = "BRE0852"
nome_viatura = "Juliano"
texto = "vai ficando com raiva de mim que não " \
        "estou nem aí para as coisas do mundo. " * 300


def generate_pdf(file_name):
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()

    content = []

    # Criar um estilo baseado no estilo "Normal" com alinhamento justificado
    style = styles["Normal"]
    style.alignment = 0  # 0 para Esquerda, 1 para Centralizado, 2 para Direita, 3 para Justificado

    # Adiciona o texto ao conteúdo usando o novo estilo  +'&nbsp'*30 +  dá espaçamento
    content.append(Paragraph(f'PLACA : {placa},'+'&nbsp'*30 + ';VIATURA: {nome_viatura}.', style))
    content.append(Paragraph('<font color="blue"><a href="https://www.google.com/">Texto em negrito'
                             '</a></font>', style))
    content.append(Spacer(1, 12))  # 12 é a altura do espaço em branco em pontos
    content.append(Paragraph('<br/>Todos presentes aqui esperando.', style))
    content.append(Paragraph('Assim todos nós vamos para o país satisfeitos.', style))
    content.append(Paragraph(f'E muitos {texto}', style))
    content.append(Paragraph('<font size="15">vamos</font>', style))

    doc.build(content)


generate_pdf("exemplo.pdf")
