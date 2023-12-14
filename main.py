import requests
from bs4 import BeautifulSoup


url = 'https://rpggodscorpse.blogspot.com/search/label/3ed'
headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

def proximapagina(soup):
    #procurar botao proxima pagina
    paginas = soup.find('a', {'class': "blog-pager-older-link"})
    #ir ultima pagina
    if not paginas.find('a', {'blog-pager-older-link'}) :
        prox = soup.find('a', "blog-pager-older-link", href=True)
        url_final = (str(prox['href']))
        return url_final
    else:
        return



site = requests.get(url, headers = headers)
soup = BeautifulSoup(site.content, 'html.parser')
soup1 = BeautifulSoup(soup.prettify(), 'html.parser')
url = proximapagina(soup1)

ficha = soup.find_all("div", {"class": 'post-body entry-content'})


print(ficha)

#titulo = soup.find_all("h2", {"class": 'Black-SectionTitle'})
# char = soup.find_all("h1", {"class": 'Black-SectionTitle'})
# pontos_total = soup.find_all("span", {"class": 'Black-SectionTitle'})
# caracteristicas = soup.find_all("div", {"style": 'display: grid; grid-template-columns: repeat(4, auto)'})
# defesas = soup.find_all("div", {'style' : 'display: grid; grid-template-columns: repeat(2, auto);'})
# pericias = soup.find_all("p")