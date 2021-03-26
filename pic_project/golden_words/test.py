import requests
from lxml import etree
url = 'http://www.huitu.com/photo/dep/20161024/151121905800.html'

response = requests.get(url)
html = etree.HTML(response.text)

title = ''.join(html.xpath('.//h3[@class="info-right-title"]/text()'))

print(title)