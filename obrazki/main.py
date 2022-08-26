'''
Wylistowanie obrazów z katalogu "color".
Zamiana ich parametrów.
Zapis nowych obrazów do innego katalogu "blackandwhite.
Uruchamiamy program:
python main.py --input color --output blackandwhite
'''

'''
ArgumentParser służy do odbioru argumentów
parse_args() - funkcja do odbioru danych
'''
from argparse import ArgumentParser
'''
glob - służy do wyświetlenia ścieżek do plików
'''
from glob import glob
'''
PIL - moduł Pillow, służy do działań na obrazach
https://pillow.readthedocs.io/en/stable/
'''
from PIL import Image

parser = ArgumentParser(description='Zamiana kolorowych zdjęć na czarno-białe')
'''
funkcje które opisują pierwszy argument "--input" i drugi argument "--output", help- opis
required = True - elementy wymagane
'''
parser.add_argument('--input', help='Folder z którego odbieram obrazki', required=True)
parser.add_argument('--output', help='Folder do którego zapisuję obrazki', required=True)
args = parser.parse_args()   #przypisuje zawartość do argumentów
'''
wydruk argumentów (czyli co się znajduje w input, a co w output,
w związku z tym, że input i output są wymagane to program musimy uruchomić z tymi argumentami, 
czyli python main.py --input obrazy --output wyniki
obrazy i wyniki to przykłady, co doda do argumentów
jak uruchomimy help (python main.py -h lub python main.py --help) to powinien wypisac powyższe teksty z help
'''
# print(args)
#wyświetla zawartość input i zawartośc output: obrazy wyniki
# print(args.input, args.output)

# glob(args.input) - tylko katalog, + '/*" - także zawartość (wszystko)
# uruchamiamy python main.py --input color --output blackandwhite
# split - dzieli wynik na directory i filename (oddzielone \)
# wyświetlamy ścieżkę oraz oddzielnie directory i oddzielnie filename

for p in glob(args.input + '/*'):
    directory, filename = p.split('\\')
    print(p, directory, filename)
    with Image.open(p) as new_image:
# z opisu Pillow - transformacje pomiędzy każdym obsługiwanym trybem a trybami "L" i "RGB"
        new_image = new_image.convert("L")
        # z opisu, args.output + '/' + filename - ścieżka do zapisu nowego obrazka
        new_image.save(args.output + '/' + filename)

'''
po uruchomieniu python main.py --input color --output blackandwhite powinien przekonwertować
i zapisać nowe obrazki do katalogu 'blackandwhite'
'''