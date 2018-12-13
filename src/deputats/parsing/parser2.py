import requests
import json
from bs4 import BeautifulSoup
import re

def write_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def write_html(html, filename):
    with open(filename, 'w') as f:
        f.write(html)


def strip_html():

    with open('downloads/proba.html', 'r') as f:
        html = f.read()
        # Удаляем локальные стили
        html = re.sub(r'(?:<style.+?>([^>]*)<\/style>)', '', html)

        # Удаляем локальные скрипты
        html = re.sub(r'(<[\s\/]*script\b[^>]*>)([^>]*)(<\/script>)', '', html)

        # Удаляем escape последовательности
        html = re.sub(r'\&\w+;', '', html)

        

        # Удаляем html теги
        html = re.sub(r'(\<(/?[^>]+)>)', '', html)

        write_html(html, 'downloads/proba2.html')

        #soup = BeautifulSoup(html, 'lxml')




def main():
	strip_html()






if __name__ == '__main__':
	main()