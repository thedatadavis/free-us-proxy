import requests
from bs4 import BeautifulSoup

def get_proxies():
    r = requests.get('https://www.us-proxy.org/')
    soup = BeautifulSoup(r.content, 'html.parser')

    tbl = soup.find('table')
    rows = tbl.find_all('tr')

    proxies = []

    for row in rows[1:101]:
        cells = row.find_all('td')
        ip = cells[0].text + ':' + cells[1].text
        https = cells[6].text
        last_checked = cells[7].text

        if https == 'yes':
            proxies.append({'ip_address' : ip,
                           'last_checked' : last_checked, })

    return proxies
