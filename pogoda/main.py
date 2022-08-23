# Korzystamy z https://danepubliczne.imgw.pl/apiinfo
# Dane ze stacji synoptycznych w formacie json
# https://danepubliczne.imgw.pl/api/data/synop
# Korzystamy z biblioteki "requests", którą trzeba doinstalować
# Korzystamy z biblioteki json
# Korzystamy z biblioteki terminaltables https://pypi.org/project/terminaltables/ (install)

from requests import get   #metoda do pobierania danych, inne metody to post, patch, put, delete
from json import loads  #metoda load czyta z pliku na dysku, a loads pozwala zamienić na listę słowników string (tekst)
from terminaltables import AsciiTable   #biblioteka do wyświetlania danych

CITIES = ['Bielsko Biała', 'Lublin', 'Gdańsk']

def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'  #tworzę zmienną url pod którym jest api pogodowe
    response = get(url)     # get(url) - zapytanie o status serwera, <Response [200]>
    # status 2xx - wszystko jest OK
    # status 3xx - przekierowanie (zostajemy przekierowani, np. na https)
    # status 4xx - błąd po stronie użytkownika
    # status 5xx - błąd po stronie serwera
    # print(response.text)    #response.text - zapytanie o tekst spod adresu, wyświetla tekst (string)
    # print(loads(response.text))    #wyświetla listę słowników z danymi (czyli możemy iterować)

    rows = [
        ['Miasto', 'Godzina pomiaru', 'Temperatura']
    ]   #do terminaltables (do wyświetlania)

    for row in loads(response.text):
        # print(row)             #wyświetla słowniki, każdy wiersz to jeden fragment z API (z jednej stacji)
        if row['stacja'] in CITIES:   #wyświetla słowniki z danymi dla miast CITIES
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura']
            ])                          #dodaje kolumny do wyświetlenia

    table = AsciiTable(rows)
    print(table.table)

if __name__ == '__main__':
    print('Pogodynka')
    main()

