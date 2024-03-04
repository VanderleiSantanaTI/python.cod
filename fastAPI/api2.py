"""
"uvicorn api2:app --reload"  => para fazer uma alteração sem precizar reniciar o servidor.
Outra forma é criar um arquivo dev.sh depois colocor no arquivo o "uvicorn api2:app --reload"
aí quando for acionar é só digitar no terminal: sh dev.sh e iniciará a mesma coisa
"""

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class Inputs(BaseModel):
    item: str
    preco_unitario: float
    quantidade: int


vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "darrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 5, "quantidade": 5},
    5: {"item": "latao 1L", "preco_unitario": 8, "quantidade": 3},
    6: {"item": "caixa de leite", "preco_unitario": 3, "quantidade": 10},
    7: {"item": "pacote de arroz", "preco_unitario": 12, "quantidade": 8},
    8: {"item": "pacote de feijão", "preco_unitario": 6, "quantidade": 7},
    9: {"item": "macarrão espaguete", "preco_unitario": 2, "quantidade": 15},
    10: {"item": "molho de tomate", "preco_unitario": 4, "quantidade": 10},
    11: {"item": "saco de batatas", "preco_unitario": 5, "quantidade": 10},
    12: {"item": "pão de forma", "preco_unitario": 3, "quantidade": 10},
    13: {"item": "manteiga", "preco_unitario": 4, "quantidade": 8},
    14: {"item": "queijo mussarela", "preco_unitario": 8, "quantidade": 6},
    15: {"item": "presunto", "preco_unitario": 7, "quantidade": 7},
    16: {"item": "café em pó", "preco_unitario": 10, "quantidade": 5},
    17: {"item": "açúcar", "preco_unitario": 3, "quantidade": 8},
    18: {"item": "sabão em pó", "preco_unitario": 6, "quantidade": 10},
    19: {"item": "detergente", "preco_unitario": 2, "quantidade": 12},
    20: {"item": "papel higiênico", "preco_unitario": 8, "quantidade": 10},
    21: {"item": "shampoo", "preco_unitario": 10, "quantidade": 6},
    22: {"item": "condicionador", "preco_unitario": 10, "quantidade": 6},
    23: {"item": "sabonete", "preco_unitario": 2, "quantidade": 10},
    24: {"item": "creme dental", "preco_unitario": 3, "quantidade": 8},
    25: {"item": "escova de dentes", "preco_unitario": 5, "quantidade": 8}
}


@app.post("/exemplo_post")
async def exemplo_2(inputs: Inputs):
    novo_id = max(vendas.keys()) + 1
    vendas[novo_id] = {"item": inputs.item, "preco_unitario": inputs.preco_unitario, "quantidade": inputs.quantidade}
    return inputs.item, inputs.preco_unitario, inputs.quantidade


@app.get("/")
async def home():
    return {"vendas": len(vendas)}


@app.get("/vendas")
async def home2():
    return [vendas[i + 1] for i in range(len(vendas))]


@app.get("/vendas/{id_venda}")
async def pegar_venda(id_venda: int):
    return vendas[id_venda]


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
