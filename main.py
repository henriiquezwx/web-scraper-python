import requests
from bs4 import BeautifulSoup
import csv

titulos = []
precos = []

# Vamos raspar os dados das primeiras 3 páginas
for pagina in range(1, 4):
    if pagina == 1:
        url = "http://books.toscrape.com/index.html"
    else:
        url = f"http://books.toscrape.com/catalogue/page-{pagina}.html"

    print(f"Acessando a página {pagina}...")
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        produtos = soup.find_all("article", class_="product_pod")

        for produto in produtos:
            titulo = produto.h3.a["title"]
            preco = produto.find("p", class_="price_color").text
            
            titulos.append(titulo)
            precos.append(preco)
    else:
        print(f"Erro ao acessar a página {pagina}")

# Salva o resultado total na pasta Download
nome_arquivo = "/sdcard/Download/relatorio_produtos.csv"

with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Produto", "Preço"])
    for t, p in zip(titulos, precos):
        escritor.writerow([t, p])

print(f"\nSucesso total! {len(titulos)} produtos salvos em '{nome_arquivo}'.")
