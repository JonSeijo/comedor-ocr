import json
import os
from PIL import Image
from pytesseract import image_to_string

BASEDIR = './crops/comidas'
files = os.listdir(BASEDIR)
files = [BASEDIR + '/' + filename for filename in files]

menu = {}

for filename in files:
	if '.png' not in filename:
		continue

	print('filename: ', filename)
	image = Image.open(filename)

	comida = image_to_string(image, lang='spa')

	diafile = int(filename[-6:-4])
	menu[diafile] = comida.replace('\n', ' ')

with open('menu_comedor.json', 'w') as menufile:
	json.dump(menu, menufile, indent=4, separators=(',', ': '))
