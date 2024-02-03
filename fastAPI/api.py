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



# criar o caminho da página para GET
@app.get("/exemplo")
def exemplo():
    return "Olá Mundo!"




# criar o caminho da página para POST
@app.post("/exemplo_2")
def exemplo_2(inputs: Inputs):
    # ...
    print(inputs.inp2)
    vendas.append((inputs.inp, inputs.inp2))
    #vendas.append(inputs.inp)
    if (inputs.inp2).lower() == "oi":
        print("concedido")
    else:
        print("Não concedido")    
    return inputs.inp, inputs.inp2


# criar o caminho da página para GET
@app.get("/exemplo_post")
def exemplo():
    # criar uma lista de  dicionário
    lista_de_dicionarios = [{"id": item[0], "nome": item[1]} for item in vendas]
    return lista_de_dicionarios

# criar o caminho da página para GET
@app.get("/exemplo_post/{id_venda}")
def exemplo(id_venda:int):
    return vendas[id_venda]


# inicia se for pela principal
if __name__ == "__main__":
    uvicorn.run(app, port=8000)
