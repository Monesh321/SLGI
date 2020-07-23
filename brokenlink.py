import requests
import bs4
from urllib.parse import urljoin, urlparse


def get_title(page):
    soup = bs4.BeautifulSoup(page, 'lxml')
    # text = soup.text
    title = soup.find('title')
    return title


BASE_URL = "https://www.sunlifeglobalinvestments.com/Slgi-Funds/Equity-funds/Sun-Life-US-Equity-Fund?mp=MMBUA&lang=en&fundCurrencyCd=CAD"
page = requests.get(BASE_URL)
# print(page.text)

soup = bs4.BeautifulSoup(page.text, 'lxml')

text = soup.text
# links = soup.findAll(text=True)

# print(links)
# print("\n".join([s for s in (soup.text).split("\n") if s]))
# print(links)

# for link in links:
#     if link.get('href') != None and link.get('href') != '':
#         if 'javascript' not in link.get('href') and '#' not in link.get('href'):
#             url = urljoin(BASE_URL, link.get('href'))
#             parsed_href = urlparse(url)
#             # remove URL GET parameters, URL fragments, etc.
#             url = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
#             print(link.text, "FOR URL: ", url, "STATUS:", requests.get(url).status_code,
#                   get_title(requests.get(url).text))

lines = [line.strip() for line in text.splitlines() if line != '']
#
print('\n'.join([l for l in lines if l != '']))
