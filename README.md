# Comedor-OCR

IMPORTANTISIMO:

REQUIERE TESSERACT-OCR EN VERSION +4.
Versiones previas funcionan pero dan resultados bastante malos en comparacion. Puede tener que ver con la calidad de las imagenes con las que estamos trabajando

Se requiere:
- tesseract-ocr
- tesseract-ocr-spa

Python3:
- pytesseract

-----
## Instrucciones

Antes de ejecutar los scripts se necesita un preproceso para resizear y convertir a B&N

```bash
convert agosto19.png -resize 150% agosto19_150.png
convert agosto19_150.png -type Grayscale agosto19_150_gray.png
```

Lo siguiente que hacemos es recortar cada uno de los dias en una imagen sepadara, para poder aplicarles el ocr.

!!CUIDADO: Es probable que con un cambio de mes los recuadros de los dias se encuentren en otras coordenadas. Hay que revisar esto para generalizarlo un poco. #TODO

```bash
cd crops
python3 cropper.py agosto19_150_gray.png
```

Las imagenes recortadas se encuentran en crops/comidas.

Ejecutamos el ocr para las imagenes recortadas:

```bash
python3 comedorOCR.py
```

Los resultados se obtienen en ```menu_comedor.json```