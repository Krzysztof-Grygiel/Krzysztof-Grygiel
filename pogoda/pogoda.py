from requests import get
from json import loads
from terminaltables import AsciiTable   #biblioteka do wyświetlania danych

CITY = input('Z jakiej stacji diagnostycznej chciałbyś pozyskać dane? Podaj miasto: ')


def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    rows = [
        ['Miasto', 'Godzina pomiaru', 'Temperatura']
    ]

    for row in loads(response.text):
        if row['stacja'] in CITY:
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura']
            ])
        # else:
        #     print('Nie ma takiego miasta')
        #     break

    table = AsciiTable(rows)
    print(table.table)


if __name__ == '__main__':
    print('Pogodynka')
    main()

