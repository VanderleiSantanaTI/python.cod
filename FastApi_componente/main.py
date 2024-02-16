'''
1 - Criar um ambiente virtual: "python -m venv venv" ou melhor pelo pycharm
2  - Ativar o ambiente virtual: venv\Scripts\activate
3  - caso queira desativar    : deactivate
4  - python -m pip install --upgrade pip
5  - pip install fastapi
6  - pip install "uvicorn[standard]"
7  - uvicorn main:app --reload => para colocar no ar
8  - pip freeze => vai tudo que foi instalado no ambiente virtual
9  - pip freeze > requeriment.txt => criar um aquivo (instalações)
10 - pip install -r requeriment.txt => instala todo requiriments
11 - criar um aquivo .bat pra windows por "uvicorn main:app --reload" dentro dele para rodar com o comando ".\dev.bat"
'''
from fastapi import FastAPI

from indb import generate_products


app = FastAPI()
produto = generate_products()

@app.get("/")
def get_products():
    return {"products": produto}

