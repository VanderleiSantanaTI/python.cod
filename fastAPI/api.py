'''
Para ativar no VSCODE basta digitar no terminal python api.py (nome do arquivo)
e desconectar (CTRL + C)
Para entrar da DOCS pasta http://localhost:8000/docs#/
'''
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

vendas = []

# Adicione o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou especifique os domínios permitidos  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Ou especifique os métodos permitidos
    allow_headers=["*"],  # Ou especifique os headers permitidos
)


# para fazer o input dos POSTs
class Inputs(BaseModel):
    inp: int
    inp2: str
    email: str



# criar o caminho da página para GET
@app.get("/exemplo")
def exemplo():
    return "Olá Mundo!"


# criar o caminho da página para GET todos os IDs disponíveis
@app.get("/ids_disponiveis")
def ids_disponiveis():
    return [item[0] for item in vendas]





# criar o caminho da página para GET
@app.get("/exemplo_get")
def exemplo():
    # criar uma lista de dicionário
    lista_de_dicionarios = [{"id": item[0], "nome": item[1], "email":item[2]} for item in vendas]
    return lista_de_dicionarios

# criar o caminho da página para GET
@app.get("/exemplo_get/{id_venda}")
def exemplo(id_venda:int):
    return vendas[id_venda]


# criar o caminho da página para POST
@app.post("/exemplo_post")
def exemplo_2(inputs: Inputs):
    # ...
    print(inputs.inp2)
    vendas.append((inputs.inp, inputs.inp2, inputs.email))
    #vendas.append(inputs.inp)
    if (inputs.inp2).lower() == "vanderlei":
        print("concedido")
    else:
        print("Não concedido")    
    return inputs.inp, inputs.inp2, inputs.email


@app.delete("/exemplo_get/{id_venda}")
def delete_value(id_venda: int):
    try:
        vendas.pop(id_venda)
        return {"message": "Valor excluído com sucesso"}
    except IndexError:
        return {"error": "ID de venda não encontrado"}

# inicia se for pela principal
if __name__ == "__main__":
    uvicorn.run(app, port=8000)
