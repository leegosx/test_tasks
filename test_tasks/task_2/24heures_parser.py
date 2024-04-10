import requests
from bs4 import BeautifulSoup
from datetime import datetime

def parse_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.find('h1').text.strip() if soup.find('h1') else 'Title not found'
        content = ''
        for paragraph in soup.find_all('p', class_='ArticleParagraph_root__lhFZo'):
            if 'undesirable-class' not in paragraph.get('class', []):
                content += paragraph.text.strip() + ' '
        author_container = soup.find('span', class_='ContentMetaInfo_author__6_Vnu')
        author = author_container.text.split('/')[0].strip() if author_container else 'Author not found'       
        date_element = soup.find('time', attrs={'datetime': True})
        date_text = date_element['datetime'] if date_element else 'Date not found'
        try:
            date = datetime.strptime(date_text, "%Y-%m-%dT%H:%M:%S.%fZ")
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
    # url3 (paid article) ✔ work ✔ 
    # url4 (without author)  ✔ work ✔
    # url5 ✔ work ✔
    # url6 (without author)  ✔ work ✔
    # url7 ✔ work ✔ podcast 
    # url8 ✔ work ✔ video

    url1 = 'https://www.24heures.ch/lausanne-la-drogue-serait-la-cause-de-lagression-a-la-riponne-153549364185' 
    print(parse_article(url1))
    # url2 = 'https://www.24heures.ch/lausanne-le-mort-a-ruchonnet-se-serait-suicide-464092629355'
    # print(parse_article(url2))
    # url3 = 'https://www.24heures.ch/droit-du-bail-contester-un-loyer-pourrait-devenir-complique-323944487136' 
    # print(parse_article(url3))
    # url4 = 'https://www.24heures.ch/kiev-dement-avoir-attaque-la-centrale-nucleaire-de-zaporijjia-961439352902'
    # print(parse_article(url4)) 
    # url5 = 'https://www.24heures.ch/lavaux-la-route-de-la-corniche-sera-fermee-durant-deux-mois-585522460816' 
    # print(parse_article(url5))
    # url6 = 'https://www.24heures.ch/lonu-alarmee-par-lia-militaire-meurtriere-disrael-a-gaza-247713212596' 
    # print(parse_article(url6))
    # url7 = 'https://www.24heures.ch/entre-parentheses-679315148403' 
    # print(parse_article(url7))
    # url8 = 'https://www.24heures.ch/une-eclipse-totale-a-traverse-lamerique-du-nord-659525252890' 
    # print(parse_article(url8))