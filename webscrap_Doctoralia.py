import requests
from bs4 import BeautifulSoup
from lxml import html

url = requests.get('https://www.doctoralia.com.br/ginecologista/sao-paulo')
content = url.content
#tree = html.fromstring(result.content)


soup = BeautifulSoup(content, 'html.parser')
names = soup.find_all(attrs={"itemprop":"name","data-eecommerce-action":"product-click"})
#buyers = tree.xpath('//span[@itemprop="name"]/text()')

for name in names:
    print(name.getText().strip())

#print(buyers)