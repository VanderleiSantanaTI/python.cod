from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

pais = "Brasil"
nome = "Juliano"
texto = "vai ficando com raiva de mim que não estou nem aí para as coisas do mundo. " * 100

def generate_pdf(file_name):
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()

    content = []
    style = styles["Normal"]
    style.alignment = 0  # 0 para Esquerda, 1 para Centralizado, 2 para Direita, 3 para Justificado
    text = f'''Olá tudo bem com você {nome}. Estamos todos presentes aqui esperando 
    por uma posição emergencial de acordo com a justiça brasileira. 
    Assim todos nós vamos para o país {pais} satisfeitos. E muitos {texto}'''

    # Adiciona o texto ao conteúdo
    content.append(Paragraph(text, style))

    doc.build(content)

generate_pdf("exemplo.pdf")
