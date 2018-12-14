import requests
from bs4 import BeautifulSoup

def get_proxies():
    
    anonymity = { 'elite proxy' : {'ip' : True, 'proxy' : True},
                 'anonymous' : {'ip' : True, 'proxy' : False},
                 'transparent' : {'ip' : False, 'proxy' : True},
    }
    
    r = requests.get('https://www.us-proxy.org/')
    soup = BeautifulSoup(r.content, 'html.parser')

    tbl = soup.find('table')
    rows = tbl.find_all('tr')

    proxies = []

    for row in rows[1:201]:
        cells = row.find_all('td')
        ip = cells[0].text + ':' + cells[1].text
        https = cells[6].text
        is_ip_hidden = anonymity[cells[4].text]['ip']
        is_proxy_hidden = anonymity[cells[4].text]['proxy']
        last_checked = cells[7].text

        if https == 'yes':
            proxies.append({'ip_address' : ip,
                            'last_checked' : last_checked,
                            'is_proxy_hidden' : is_proxy_hidden,
                            'is_ip_hidden' : is_ip_hidden, 
                           })

    return proxies
