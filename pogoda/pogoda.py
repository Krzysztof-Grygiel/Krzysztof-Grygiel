from requests import get
from json import loads
from terminaltables import AsciiTable

city = input('Dla jakiej stacji pogodowej chcesz znać pogodę? Podaj miasto: ')
url = 'https://danepubliczne.imgw.pl/api/data/synop'
response = get(url)
print(f'Wybrałeś {city}. Możliwe stacje do wyboru to: ')

for name in loads(response.text):
    print(name['stacja'])

def main():
    rows = [
        ['Miasto', 'Data pomiaru', 'Godzina pomiaru', 'Temperatura', 'Prędkość wiatru', 'Suma opadu']
    ]

    for row in loads(response.text):
        if row['stacja'] in city:
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
    print('-----------------')
    print('Pogodynka')
    main()