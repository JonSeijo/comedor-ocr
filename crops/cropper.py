"""
python3 cropper.py agosto19_150_gray.png
"""
import os
import sys
from PIL import Image

if len(sys.argv) == 1:
    raise Exception('Usage: python3 cropper.py <imagename>')

imagename = sys.argv[1]
image = Image.open(imagename)
outfilename = 'comidas/' + os.path.splitext(imagename)[0]

w, h = image.size
print("h, w", h, w)

# FIXME: Numeros magicos

comida_ancho = w // 5
comida_alto = h // 8.9
start_y = h * 0.41 // 1

dia_actual = 0

for fila in range(4):
    for col in range(5):
        offsetx = comida_ancho * col
        offsety = comida_alto * fila + start_y

        print("offsetx offsety", offsetx, offsety)

        imCrop = image.crop((
                            offsetx,
                            offsety,
                            offsetx + comida_ancho - 1,
                            offsety + comida_alto - 1))

        imCrop.save("comidas/dia_" + str(dia_actual).zfill(2) +
                    '.png', "PNG", quality=100)

        dia_actual += 1
