import streamlit as st
import datetime
from fpdf import FPDF
import re

# Função para gerar o PDF
def gerar_pdf(nome, cpf, data_termino):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    
    pdf.cell(200, 10, "DECLARAÇÃO DE CONCLUSÃO DE CURSO", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    texto = f"""Eu, {nome}, portador(a) do CPF {formatar_cpf(cpf)}, declaro para os devidos fins que concluí 
    o curso conforme as normas da instituição.

    Assinatura: ___________________________
    Data: {data_termino.strftime('%d/%m/%Y')}
    """
    pdf.multi_cell(0, 10, texto)

    # Salvar o PDF
    caminho_pdf = "declaracao.pdf"
    pdf.output(caminho_pdf)
    return caminho_pdf

# Função para formatar o CPF
def formatar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)  # Remove tudo que não for número
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf  # Retorna sem alteração se não tiver 11 dígitos


# Função principal
def main():
    # Configuração da página
    st.set_page_config(page_title="Declaração de Conclusão de Curso", page_icon="🎓", layout="centered")
    
    # Estilização personalizada
    st.markdown(
        """
        <style>
        .stApp {
            background: #000000;
            color: #FFFFFF;
            font-family: 'Arial', sans-serif;
            display: flex;
            justify-content: center;
        }
        .container {
            max-width: 900px;
            padding: 20px;
            background: #111111;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.2);
        }
        .stTextInput>div>div>input {
            background-color: #222222;
            color: #FFFFFF;
            border: 1px solid #3A8DFF;
        }
        .stButton>button {
            background-color: #3A8DFF;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #1C6DFF;
        }
        .report-box {
            background: #1A1A1A;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
        }
        .print-button {
            background-color: #008CBA;
            color: white;
            padding: 8px 15px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
        }
        .print-button:hover {
            background-color: #005F73;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Container principal
    st.markdown('<div class="container">', unsafe_allow_html=True)
    
    # Título da página
    st.title('🎓 Declaração de Conclusão de Curso')

    # Formulário para inserir os dados
    st.header("📌 Preencha os dados para a declaração:")

    # Campos de entrada
    nome = st.text_input("Nome Completo:").upper()
    cpf = st.text_input("CPF (Somente números):", max_chars=14).replace(".", "").replace("-", "").strip()
    data_termino = st.date_input("Data de término do curso", max_value=datetime.date.today())

    # Botão para gerar a declaração
    if st.button("Gerar Declaração"):
        cpf_formatado = formatar_cpf(cpf)
        
        if nome and cpf_formatado and data_termino:
            caminho_pdf = gerar_pdf(nome, cpf, data_termino)
            
            st.subheader("📄 Declaração Gerada")
            st.write(f"**Nome:** {nome}")
            st.write(f"**CPF:** {cpf_formatado}")
            st.write(f"**Data de Conclusão:** {data_termino.strftime('%d/%m/%Y')}")

            # Botão para download do PDF
            with open(caminho_pdf, "rb") as file:
                st.download_button(
                    label="🖨️ Baixar Declaração",
                    data=file,
                    file_name="declaracao_conclusao.pdf",
                    mime="application/pdf",
                )
        else:
            st.error("⚠️ Por favor, preencha todos os campos!")

    st.markdown('</div>', unsafe_allow_html=True)  # Fecha o container

if __name__ == '__main__':
    main()
