from requests import get
from json import loads
from terminaltables import AsciiTable

CITY = input('Dla jakiej stacji pogodowej chcesz znać pogodę? Podaj miasto: ')

def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    rows = [
        ['Miasto', 'Data pomiaru', 'Godzina pomiaru', 'Temperatura', 'Prędkość wiatru', 'Suma opadu']
    ]

    for row in loads(response.text):
        if row['stacja'] in CITY:
            rows.append([
                row['stacja'],
                row['data_pomiaru'],
                row['godzina_pomiaru'],
                row['temperatura'],
                row['predkosc_wiatru'],
                row['suma_opadu']
            ])

    table = AsciiTable(rows)
    print(table.table)

if __name__ == '__main__':
    print('Pogodynka')
    main()