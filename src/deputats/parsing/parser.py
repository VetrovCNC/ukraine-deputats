import requests
import json
from bs4 import BeautifulSoup
import re
from ..models import Deputat


def write_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def download_html(url, filename):
    r = requests.get(url)
    with open(filename, 'w') as f:
        f.write(r.text)


def download_photo(url, filename):
    r = requests.get(url, stream=True)
    with open(filename, 'bw') as f:
        for chunk in r.iter_content(5000):
            f.write(chunk)


def get_all_pages(links):
    for link in links:
        filename = 'downloads/pages/' + link.split('/')[-1] + '.html'
        download_html(link, filename)


def get_all_links(index_filename):
    links = []
    with open(index_filename, 'r') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'lxml')
        ps = soup.find_all('p', class_='title')
        for p in ps:
            link = p.find('a').get('href')
            links.append(link)
    return links


def get_all_photos(deputats):
    c = 0
    for deputat in deputats:
        c += 1
        img = deputat.get('vrd_photo')
        vrd_id = deputat.get('vrd_id')
        filename = '../../../media/deputats/photos/' + vrd_id + '.jpg'
        try:
            download_photo(img, filename)
            print('{}. {}'.format(c, img))
        except:
            print('{}! {}. {}'.format('ERROR', c, img))


def parse_index_page(index_filename):
    deputats = []
    with open(index_filename, 'r') as f:
        html = f.read()
        # Исправляем ошибку в скачанной индексной странице ;-)
        html = re.sub(r'<dt><dd>', '</dt><dd>', html)
        soup = BeautifulSoup(html, 'lxml')
        lis = soup.find('ul', class_='search-filter-results search-filter-results-thumbnails').find_all('li')
        c = 0
        for li in lis:
            c += 1
            a = li.find('a')
            link = a.get('href')
            full_name = a.text
            surname, name, patronymic = full_name.split(' ')
            vrd_id = link.split('/')[-1]
            filename = '../../../media/deputats/photos/' + vrd_id + '.jpg'
            img = li.find('img').get('src')
            # извлекаем инфо "Обраний по:"
            selected_by = li.find('dt', text='Обраний по:')
            if selected_by:
                selected_by = selected_by.next_sibling.text
                gender = 'm'
            else:
                selected_by = li.find('dt', text='Обрана по:')
                if selected_by:
                    selected_by = selected_by.next_sibling.text
                    gender = 'f'
                else:
                    selected_by = ''
                    gender = ''
            # извлекаем инфо "Партія:"
            party = li.find('dt', text='Партія:')
            party = party.next_sibling.text if party else ''
            # извлекаем инфо "Номер у списку:"
            party_number = li.find('dt', text='Номер у списку:')
            party_number = party_number.next_sibling.text if party_number else 0
            # извлекаем инфо "Фракція"
            fraction = li.find('dt', text='Фракція')
            fraction = fraction.next_sibling.text if fraction else ''
            # извлекаем инфо "Посада"
            position = li.find('dt', text='Посада')
            position = position.next_sibling.text if position else ''
            # извлекаем инфо "Регіон:"
            region = li.find('dt', text='Регіон:')
            region = region.next_sibling.text if region else ''
            deputats.append(
                dict(
                    vrd_link=link,
                    vrd_id=vrd_id,
                    vrd_photo=img,
                    surname=surname,
                    name=name,
                    patronymic=patronymic,
                    selected_by=selected_by,
                    party=party,
                    party_number=party_number,
                    fraction=fraction,
                    position=position,
                    region=region,
                    gender=gender
                )
            )
    return deputats


def create_deputats(deputats):
    for deputat in deputats:
        d = Deputat.objects.create(
            vrd_link=deputat.get('vrd_link'),
            vrd_id=int(deputat.get('vrd_id')),
            vrd_photo=deputat.get('vrd_photo'),
            surname=deputat.get('surname'),
            name=deputat.get('name'),
            patronymic=deputat.get('patronymic'),
            selected_by=deputat.get('selected_by'),
            party=deputat.get('party'),
            party_number=int(deputat.get('party_number')),
            fraction=deputat.get('fraction'),
            position=deputat.get('position'),
            region=deputat.get('region'),
            gender=deputat.get('gender'),
        )



def main():
    # http://w1.c1.rada.gov.ua/pls/site2/p_deputat_list
    url = 'http://w1.c1.rada.gov.ua/pls/site2/fetch_mps?skl_id=9'
    index_filename = 'downloads/index.html'
    
    # Скачиваем список всех депутатов
    # download_html(url, index_filename)
    
    # Получаем список всех ссылок на страницы с 
    # подробной инфой по депутатам
    # links = get_all_links(index_filename)

    # Скачиваем все страницы с подробной инфой по депутатам
    # get_all_pages(links)

    deputats = parse_index_page(index_filename)
    #write_json(deputats, 'deputats.json')

    # Скачиваем фото каждого депутата
    # get_all_photos(deputats)


if __name__ == '__main__':
    main()