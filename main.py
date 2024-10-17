import requests

article_id = {
    'Лондон',
    'svo',
    'Череповец'
}

url_template = 'https://wttr.in/{}?lang=ru&T&n=3&M'

for id in article_id:
    url = url_template.format(id)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
