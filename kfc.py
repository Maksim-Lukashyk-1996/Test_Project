import requests
from bs4 import BeautifulSoup

URL = 'https://www.kfc.ru/restaurants'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.1.985 Yowser/2.5 Safari/537.36',
    'accept': '*/*'
}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    items = soup.find_all('div', class_='Mujm2VkJ7g')
    print(items)
    # print(soup.find_all('div', {"class": "Mujm2VkJ7g"}))


# def get_content(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('class', class_='Mujm2VkJ7g')
#     items = soup.find_all('div', attrs={'id':'Mujm2VkJ7g'})
#     restaurants = []
#     for item in items:
#         restaurants.append({
#             'title': item.find('div', class_='Mujm2VkJ7g').get_text(strip=True)
#         })
#
#     print(restaurants)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


parse()
