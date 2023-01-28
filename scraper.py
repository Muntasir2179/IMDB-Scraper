from bs4 import BeautifulSoup
import requests
from csv import writer

try:
    url = 'https://www.imdb.com/chart/top/'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    movies = soup.find(
        'tbody', class_='lister-list').find_all('tr')

    with open('imdb_250.csv', 'w', encoding='utf8', newline='') as f:
        csvWriter = writer(f)
        header = ['Rank', 'Name', 'Year Released']
        csvWriter.writerow(header)

        for movie in movies:
            rank = movie.find('td', class_='titleColumn').get_text(
                strip=True).split('.')[0]
            name = movie.find('td', class_='titleColumn').a.text
            year_release = movie.find('td', class_='titleColumn').span.text.replace(
                '(', '').replace(')', '')

            data = [rank, name, year_release]
            csvWriter.writerow(data)

except Exception as e:
    print(e)
