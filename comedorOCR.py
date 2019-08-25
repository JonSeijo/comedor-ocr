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

	diafile = int(filename[-6:-4])

	comida = image_to_string(image, lang='spa')
	comida = comida.replace('\n', ' ')
	comida = comida[2:] if len(comida) > 2 else comida

	menu[diafile] = comida

with open('menu_comedor.json', 'w') as menufile:
	json.dump(menu, menufile, indent=4, separators=(',', ': '))
