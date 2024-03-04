from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
import sqlite3
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Configurar o middleware CORS para permitir todas as origens
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou especifique os domínios permitidos
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # ou especifique os métodos permitidos
    allow_headers=["*"],  # ou especifique os headers permitidos
)
class Inputs(BaseModel):
    item: str
    preco_unitario: float
    quantidade: int


# Função para conectar ao banco de dados SQLite
def connect_db():
    return sqlite3.connect('vendas.db')


# Cria a tabela 'vendas' se não existir
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS vendas (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      item TEXT,
                      preco_unitario REAL,
                      quantidade INTEGER)''')
    conn.commit()
    conn.close()


# Adiciona uma venda ao banco de dados
def add_venda(item, preco_unitario, quantidade):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO vendas (item, preco_unitario, quantidade)
                      VALUES (?, ?, ?)''', (item, preco_unitario, quantidade))
    conn.commit()
    conn.close()


# Obtém todas as vendas do banco de dados
def get_vendas():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vendas')
    vendas = cursor.fetchall()
    conn.close()
    return vendas


# Atualiza uma venda no banco de dados pelo ID
def update_venda(id_venda, item, preco_unitario, quantidade):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''UPDATE vendas SET item = ?, preco_unitario = ?, quantidade = ?
                      WHERE id = ?''', (item, preco_unitario, quantidade, id_venda))
    conn.commit()
    conn.close()


# Exclui uma venda do banco de dados pelo ID
def delete_venda(id_venda):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM vendas WHERE id = ?', (id_venda,))
    conn.commit()
    conn.close()


create_table()


@app.post("/item_post")
async def item_post(inputs: Inputs):
    add_venda(inputs.item, inputs.preco_unitario, inputs.quantidade)
    return inputs.item, inputs.preco_unitario, inputs.quantidade


@app.delete("/item_delete/{id_venda}")
async def deletar_venda(id_venda: int):
    delete_venda(id_venda)
    return {"mensagem": "Venda excluída com sucesso"}


@app.put("/vendas/{id_venda}")
async def atualizar_venda(id_venda: int, inputs: Inputs):
    update_venda(id_venda, inputs.item, inputs.preco_unitario, inputs.quantidade)
    return {"mensagem": "Venda atualizada com sucesso"}


@app.get("/")
async def quant_venda():
    return {"vendas": len(get_vendas())}


@app.get("/item")
async def total_venda():
    return {"vendas": get_vendas()}


@app.get("/item/{id_venda}")
async def pegar_venda(id_venda: int):
    vendas = get_vendas()
    for venda in vendas:
        if venda[0] == id_venda:
            return {"id": venda[0], "item": venda[1], "preco_unitario": venda[2], "quantidade": venda[3]}
    raise HTTPException(status_code=404, detail="Venda não encontrada")


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
