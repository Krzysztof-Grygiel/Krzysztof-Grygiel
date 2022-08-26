'''
Wylistowanie obrazów z katalogu "color".
Zamiana ich parametrów (zmiana rozmiaru).
Zapis nowych obrazów do innego katalogu "resize".
Uruchamiamy program:
python resize.py --input color --output resize
'''

from argparse import ArgumentParser
from glob import glob

import PIL.Image
from PIL import Image

parser = ArgumentParser(description='Zmiana wielkosci zdjęć')
parser.add_argument('--input', help='Folder z którego odbieram obrazki', required=True)
parser.add_argument('--output', help='Folder do którego zapisuję obrazki', required=True)
args = parser.parse_args()



for path in glob(args.input + '/*'):
    directory, filename = path.split('\\')
    new_height = 800
    with Image.open(path) as new_image:
        height_percent = (new_height / float(new_image.size[1]))
        width_size = int((float(new_image.size[0]) * float(height_percent)))
        new_image = new_image.resize((width_size, new_height), PIL.Image.NEAREST)
        new_image.save(args.output + '/' + filename)
