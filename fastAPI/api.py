"""
Para ativar no VSCODE basta digitar no terminal python api.py (nome do arquivo)
e desconectar (CTRL + C)
Para entrar da DOCS pasta http://localhost:8000/docs#/
"""

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

vendas = [{"id": 1, "nome": 'valdir', "email": 'valdir@gmail.com'},
          {"id": 2, "nome": 'garofalo', "email": 'garofalo@gmail.com'},
          {"id": 3, "nome": 'Maldonato', "email": 'Maldonato@gmail.com'}]


# Configurar o middleware CORS para permitir todas as origens
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou especifique os domínios permitidos
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # ou especifique os métodos permitidos
    allow_headers=["*"],  # ou especifique os headers permitidos
)


# para fazer o input dos POSTs
class Inputs(BaseModel):
    id: int
    nome: str
    email: str


# criar o caminho da página para GET
@app.get("/exemplo")
def exemplo():
    return "Olá Mundo!"


# criar o caminho da página para GET todos os IDs disponíveis
@app.get("/ids_disponiveis")
async def ids_disponiveis():
    return [item["id"] for item in vendas]


# criar o caminho da página para GET
@app.get("/exemplo_get")
async def exemplo():

    # criar uma lista de dicionário
    lista_de_dicionarios = [{"id": item["id"], "nome": item["nome"], "email":item["email"]} for item in vendas]
    return lista_de_dicionarios


# criar o caminho da página para GET
@app.get("/exemplo_get/{id_venda}")
async def exemplo(id_venda: int):

    if id_venda < 0 or id_venda >= len(vendas):
        return "Índice fora do intervalo"
    return vendas[id_venda-1]  # Para excluir a posição zero


# criar o caminho da página para POST
@app.post("/exemplo_post")
async def exemplo_2(inputs: Inputs):
    vendas.append(dict(id=inputs.id, nome=inputs.nome, email=inputs.email))
    return inputs.id, inputs.nome, inputs.email


@app.delete("/exemplo_del/{id_venda}")
async def delete_value(id_venda: int):
    try:
        vendas.pop(id_venda-1)  # Para excluir o zero
        return {"message": "Valor excluído com sucesso"}
    except IndexError:
        return {"error": "ID de venda não encontrado"}


# inicia se for pela principal
if __name__ == "__main__":
    uvicorn.run(app, port=8000)
