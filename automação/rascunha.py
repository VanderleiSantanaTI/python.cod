from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import blue, green

# Definindo o estilo com wordWrap desativado
style = ParagraphStyle(name='CustomStyle', wordWrap='LTR')

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

    # Adiciona o texto ao conteúdo usando o novo estilo
    content.append(Paragraph(f'PLACA : {placa}, VIATURA: {nome_viatura}.', style))
    content.append(Paragraph('<b><a href="https://www.google.com/">Texto em negrito</a></b>', style))
    content.append(Paragraph('&nbsp; '*10 + '<font color="blue">Todos presentes aqui esperando.</font>', style))
    content.append(Paragraph('&nbsp; '*33 + '<font color="green">Assim todos nós vamos para o país satisfeitos.</font>', style))
    content.append(Paragraph('&nbsp; '*50 + f'<font color="red">{texto}</font>', style))
    content.append(Paragraph('&nbsp; '*33 + '<font size="15">vamos</font>', style))

    doc.build(content)


generate_pdf("exemplo.pdf")
