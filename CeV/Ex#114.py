import urllib.error
from urllib import request

try:
    site = request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Site não disponível')
else:
    print('Site disponível!')
    print(site.read())
