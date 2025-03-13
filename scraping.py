import requests
from bs4 import BeautifulSoup

# URL do site no Framer
url = "https://caaju.framer.website"  # 🔥 Substitui isso pela URL real do teu site

# Fazendo a requisição HTTP
response = requests.get(url)

# Verifica se deu tudo certo
if response.status_code == 200:
    # Pegando o HTML da página
    html_content = response.text

    # Usando BeautifulSoup pra parsear o HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Pegando o conteúdo do CSS (normalmente Framer inclui no <style> ou como link externo)
    styles = soup.find_all("style")  # Captura CSS embutido
    css_links = [link["href"] for link in soup.find_all("link", rel="stylesheet")]  # Links externos

    # Salvando o HTML
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    # Salvando o CSS embutido
    with open("styles.css", "w", encoding="utf-8") as f:
        for style in styles:
            f.write(style.text + "\n")

    # Baixando os arquivos CSS externos
    for i, css_link in enumerate(css_links):
        css_response = requests.get(css_link)
        if css_response.status_code == 200:
            with open(f"external_style_{i}.css", "w", encoding="utf-8") as f:
                f.write(css_response.text)

    print("Scraping concluído! HTML e CSS salvos com sucesso. 🚀")

else:
    print(f"Erro ao acessar o site: {response.status_code}")