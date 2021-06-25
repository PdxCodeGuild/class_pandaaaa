# https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/
import requests
import pprint
from bs4 import BeautifulSoup


def main():
    url = 'https://pythonprogramming.net/parsememcparseface/'
    payload = {
    }

    r = requests.get(url, params=payload)
    print(r.url)
    soup = BeautifulSoup(r.content,'lxml')

    # Prints contents of first <p>
    # print(soup.p.text)
    body = soup.body
    print(soup.get_text())
    # print(body.prettify())
    # All text in body with <p> tag: 
    # for paragraph in body.find_all('p'):
    #     print(paragraph.text)
    
    # All text between <div> tags:
    # for div in soup.find_all('div',class_='body'):
    #     print(div.text)
main()
