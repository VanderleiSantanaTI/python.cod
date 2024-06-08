from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

# Criar a aplicação FastAPI
app = FastAPI()

# Conectar ao banco de dados SQLite
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS items
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL)''')
conn.commit()

# Modelos Pydantic para entrada e saída de dados
class Item(BaseModel):
    name: str
    price: float

# Rota para criar um novo item
@app.post("/items/")
async def create_item(item: Item):
    cursor.execute("INSERT INTO items (name, price) VALUES (?, ?)", (item.name, item.price))
    conn.commit()
    return {"message": "Item criado com sucesso"}

# Rota para obter um item por ID
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    cursor.execute("SELECT id, name, price FROM items WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    if item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"id": item[0], "name": item[1], "price": item[2]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
