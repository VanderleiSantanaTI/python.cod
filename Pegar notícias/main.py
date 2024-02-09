
#class="feed-post bstn-item-shape type-materia"
import requests
import bs4

url = "https://ge.globo.com/"

requisicao = requests.get(url)

pagina = bs4.BeautifulSoup(requisicao.text, "html.parser")


# pegar os elementos "a" que tenha m a classe  "feed-post-link"

lista_notinias = pagina.find_all("div", class_="feed-post-body")



for noticia in lista_notinias:
    print(noticia.text) # pegar apenas os textos
    print(noticia.get("div")) # pegar das divs
    print('######################')
