import requests
from bs4 import BeautifulSoup
from datetime import datetime

def parse_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find('h1').text.strip() if soup.find('h1') else 'Title not found'
        article_body = soup.find('div', class_='inner-post-entry')
        content = ' '.join([p.text for p in article_body.find_all('p')]) if article_body else 'Content not found' 
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
    # url6 ✔ work ✔
    # url7 ✔ work ✔ 

    url1 = 'https://www.breakinglatest.news/news/small-cryptominers-in-the-eye-of-the-ande-news-cde/'
    print(parse_article(url1))
    # url2 = 'https://www.breakinglatest.news/sports/akshay-bhatia-after-pga-tour-victory-at-golf-event/'
    # print(parse_article(url2))
    # url3 = 'https://www.breakinglatest.news/news/too-sweet-to-be-a-drug-dog-roger-the-labrador-wins-hearts-of-taiwanese-with-earthquake-rescue/'
    # print(parse_article(url3))
    # url4 = 'https://www.breakinglatest.news/news/ansbach-financial-injection-for-student-cafe/'
    # print(parse_article(url4))
    # url5 = 'https://www.breakinglatest.news/news/social-security-stimulus-checks-who-are-the-citizens-eligible-to-receive-the-ud-1400-bonus-in-april-united-states-rppusa/'
    # print(parse_article(url5))
    # url6 = 'https://www.breakinglatest.news/world/ukraine-sows-852-1-thousand-hectares-by-april-5/'
    # print(parse_article(url6))
    # url7 = 'https://www.breakinglatest.news/business/these-are-the-consequences-of-ukraines-lack-of-ammunition-on-the-battlefield/'
    # print(parse_article(url7))