'''
Pobieranie nazw produktów po adresie www.
Korzystamy z adresu nowości w audioteka.pl
'''
import requests
from lxml import html

url = 'https://audioteka.com/pl/audiobooks/new'
page = requests.get(url)
tree = html.fromstring(page.content)      #funkcja fromstring służy do wyświetlenia html w postaci drzewa
print(tree)    #page.content - zawartość strony www w postaci tekstu (string), tree - element html
'''
- na stronie wyszukujemy w kodzie (na linku klikamy prawym przyciskiem i Zbadaj)
fragment kodu dotyczącego danego elementu i 
- kopiujemy xPath - prawy przycisk
myszy i Copy --> xPath
- usuwamy fragment kodu przy div (div[1] dotyczy konkretnego produktu, natomiast div wszystkich)
- Na końcu dodajemy "/text()" żeby otrzymać tekst (skopiowano i tytuł książki i autora - oddzielnie)
'''
xpath_selector ='/html/body/div/div/div/div/div/div/h2/a/text()'
xpath_author ='/html/body/div/div/div/div/div/div/div/a/text()'
'''
z drzewa chcemy znaleźć odpowiedni element używając xpath
'''
products = tree.xpath(xpath_selector)
authors = tree.xpath(xpath_author)
'''
aby ładnie wyświetlić tekst (strip - bez znaków tabulacji i końca linii)
'''
print()
print('Tytuły:')
for product in products:
    print(product.strip())
print()
print('Autor, czyta i cena:')
for author in authors:
    print(author.strip())

