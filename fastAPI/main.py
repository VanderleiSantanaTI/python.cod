import requests

# Defina os dados que deseja enviar no corpo da requisição
data = {"id": 2, "titul": "Produto A", "descricao": "10.99", "presente": True}



# Faça a requisição POST para a URL desejada, passando os dados
response = requests.post("http://localhost:8000/enviar/", json=data)

# Verifique o status da resposta
if response.status_code == 200:
    print("Item criado com sucesso!")
else:
    print("Falha ao criar o item. Código de status:", response.status_code)
