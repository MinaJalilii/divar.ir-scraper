import requests
from bs4 import BeautifulSoup

page = requests.get('https://divar.ir/s/tehran/buy-apartment/pasdaran')

soup = BeautifulSoup(page.content, "html.parser")

boxes = soup.find_all('div', class_='kt-post-card__body')
for item in boxes:
    title = item.find('h2', class_='kt-post-card__title')
    price = item.find('div', class_='kt-post-card__description')
    address = item.find('span', class_='kt-post-card__bottom-description kt-text-truncate')
    if title is not None:
        title = title.text.strip()
        print(title)
    else:
        title = 'Not defined'
    if price is not None:
        price = price.text.strip()
        print(price)
    else:
        price = 'Not defined'
    if address is not None:
        address = address.text.strip()
        print(address)
    else:
        address = 'Not defined'
    print('------------------------------------')

url = 'https://api.divar.ir/v8/web-search/1/apartment-sell'
lastPostDate = 1709959888033990
# last post date is not static, you should check it every time you want to run this code
for j in range(1, 4):
    page = j
    data = {
        "page": page,
        "json_schema": {
            "category": {
                "value": "apartment-sell"
            },
            "districts": {
                "vacancies": [
                    "67"
                ]
            },
            "sort": {
                "value": "sort_date"
            },
            "cities": [
                "1"
            ]
        },
        "last-post-date": lastPostDate
    }
    header = {"Content-Type": "application/json"}
    answer = requests.post(url, json=data, headers=header)
    result = answer.json()

    for i in result['web_widgets']['post_list']:
        title = i['data']['title']
        print(title)
        price = i['data']['middle_description_text']
        print(price)
        location = i['data']['bottom_description_text']
        print(location)
        print('----------------------------------')
    lastPostDate = result['last_post_date']
