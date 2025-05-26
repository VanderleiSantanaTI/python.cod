from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from geopy.geocoders import Nominatim
import folium
from fastapi.responses import HTMLResponse

# Inicializa o FastAPI
app = FastAPI()

# Serve a pasta 'images' como uma pasta estática pra arquivos de imagem personalizados
# (como ícones do Folium)
# app.mount("/static", StaticFiles(directory="images"), name="static")

# Criação do ícone com o caminho correto
# icon = folium.CustomIcon(icon_image='http://127.0.0.1:8000/static/point.png', icon_size=(30, 30))


# Permitir todas as origens para o CORS (você pode configurar para permitir origens específicas, se necessário)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Inicializa o geolocalizador
geolocator = Nominatim(user_agent="sistema_trafego")

# Função para geocodificar o endereço
def endereco_para_coordenada(endereco: str):
    try:
        location = geolocator.geocode(endereco, timeout=10)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao geocodificar o endereço: {str(e)}")

# Definindo a estrutura de dados para os pontos e a posição atual
class PontosEntrega(BaseModel):
    pontos: list[str]
    posicao_atual: dict  # Latitude e longitude da posição atual

@app.post("/pontos_entrega", response_class=HTMLResponse)
async def pontos_entrega(pontos: PontosEntrega):
    print(f"Dados recebidos: {pontos}")  # Para verificar os dados recebidos

    if not pontos.pontos:
        raise HTTPException(status_code=400, detail="Nenhum ponto de entrega enviado.")

    # Cria o mapa base, usando a posição atual como ponto inicial
    mapa = folium.Map(location=[pontos.posicao_atual['lat'], pontos.posicao_atual['lon']], zoom_start=12)

    # Adiciona os pontos de entrega no mapa
    for ponto in pontos.pontos:
        lat, lon = endereco_para_coordenada(ponto)
        if lat and lon:
            icon = folium.CustomIcon(icon_image='http://127.0.0.1:8000/static/package.png', icon_size=(30, 30))
            # icon = folium.CustomIcon(icon_image='/images/point.png', icon_size=(30, 30))
            # icon = folium.Icon(color='red', icon='cloud', prefix='fa')
            folium.Marker([lat, lon], popup=ponto, icon=icon).add_to(mapa)

    # Retorna o mapa gerado
    return mapa._repr_html_()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
