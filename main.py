import requests

if __name__ == '__main__':

    cities = {
        'Лондон',
        'svo',
        'Череповец'
    }
    payload = {
        'lang': 'ru',
        'n': '3',
        'M': ' ',
        't': ' ',
        }
    url_template = 'https://wttr.in/{}'
    for city in cities:
        url = url_template.format(city)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)
