import requests
from bs4 import BeautifulSoup
from datetime import datetime

def parse_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find('h1').text.strip() if soup.find('h1') else 'Title not found'
        content = ''
        for paragraph in soup.find_all('p', class_='paragraph'):
            if 'undesirable-class' not in paragraph.get('class', []):
                content += paragraph.text.strip() + ' '
        author_container = soup.find('span', class_='author-art')
        author = author_container.text.split('/')[0].strip() if author_container else 'Author not found'       
        date_element = soup.find('p', class_='is-last-update')
        date_text = date_element['datetime'] if date_element else 'Date not found'
        try:
            date = datetime.strptime(date_text, "%Y-%m-%dT%H:%M:%S%z")
        except ValueError:
            date = 'Date format is not recognized'

        return {
            'title': title,
            'content': content,
            'author': author,
            'date': date,
        }
    
    else:
        return {'error': f'Failed to retrieve the article. HTTP status code: {response.status_code}'}
    
if __name__ == '__main__':
    # url1  ✔ work ✔ 
    # url2  ✔ work ✔ 
    # url3  ✔ work ✔ 
    # url4 ✔ work ✔
    # url5 ✔ work ✔

    url1 = 'https://corrieredibologna.corriere.it/notizie/cronaca/24_aprile_10/vittime-centrale-suviana-chi-erano-889216ee-5fd9-423c-bcc2-36ee4a2a1xlk.shtml'
    print(parse_article(url1))
    # url2 = 'https://corrieredibologna.corriere.it/notizie/cronaca/24_aprile_10/scuole-besta-a-bologna-l-appello-di-lepore-dopo-la-tregua-ora-il-parco-don-bosco-torni-di-tutti-add9ffeb-4dda-42c7-a3d5-c6576cfe7xlk.shtml'
    # print(parse_article(url2))
    # url3 = 'https://corrieredibologna.corriere.it/notizie/politica/24_marzo_29/europee-2024-l-incontro-pd-tra-schlein-e-bonaccini-per-le-elezioni-il-governatore-capolista-nel-nord-est-o-non-correra-6e4dbcbf-e57f-4b8a-9c27-738d0bc19xlk.shtml'
    # print(parse_article(url3))
    # url4 = 'https://corrieredibologna.corriere.it/notizie/politica/24_aprile_08/imprese-e-sindacati-in-campo-progetti-di-lungo-respiro-ma-tante-complessita-ora-serve-piu-dialogo-f9b4202c-ccee-4199-b3aa-be07319bfxlk.shtml'
    # print(parse_article(url4))\
    # url5 = 'https://corrieredibologna.corriere.it/notizie/sport/24_aprile_07/serie-a-frosinone-bologna-0-0-allo-stirpe-finisce-a-reti-inviolate-20982d00-b0fa-45db-aa22-d371f2097xlk.shtml'
    # print(parse_article(url5))