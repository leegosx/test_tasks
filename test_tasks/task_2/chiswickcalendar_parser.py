import requests
from bs4 import BeautifulSoup
from datetime import datetime

def parse_article(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find('h1').text.strip() if soup.find('h1') else 'Title not found'
        article_body = soup.find('div', class_='entry-content')
        if article_body:
            for unwanted_tag in article_body.select('h3, em, a, strong'):
                unwanted_tag.extract()
            content = ' '.join([p.text for p in article_body.find_all('p')])
        else:
            content = 'Content not found'
        author_container = soup.find('span', class_='author')
        author = author_container.text.split('/')[0].strip() if author_container else 'Author not found'       
        date_element = soup.find('time', attrs={'datetime': True})
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

    url1 = 'https://chiswickcalendar.co.uk/who-are-the-2024-candidates-for-the-south-west-london-seat-on-the-london-assembly/'
    print(parse_article(url1))
    # url2 = 'https://chiswickcalendar.co.uk/the-apprentice-comes-to-chiswick/'
    # print(parse_article(url2))
    # url3 = 'https://chiswickcalendar.co.uk/police-fire-and-rnli-crews-search-the-river-at-strand-on-the-green/'
    # print(parse_article(url3))
    # url4 = 'https://chiswickcalendar.co.uk/the-old-pack-horse-reopens-after-refurbishment/'
    # print(parse_article(url4))
    # url5 = 'https://chiswickcalendar.co.uk/the-government-inspector-st-michaels-players/'
    # print(parse_article(url5))