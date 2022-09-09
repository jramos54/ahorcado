#fileWrite.py 
''' El programa de ahorcado con lectura en archivos.
    Los archivos seran TXT. Hay dos archivos:
    a ) PALABRAS, que contiene tanto palabras en ingles, español y         una categoria con la que se clasificara.
    b) ESTADISTICAS, contiene las estadisticas del juego'''

def leerPalabra(numero):
  with open('palabras.txt','r') as file:
    palabras=file.readlines()
  if len(palabras)<1:
    return palabras[0]
  elif len(palabras)<numero:
    return palabras[-1]
  else:
    return palabras[numero-1].split('|')

def guardarPalabra(palabra,idioma,categoria='general'):
  with open('palabras.txt','a') as file:
    file.write(f'\n{palabra}|{idioma}|{categoria}')

def listaPalabras():
  with open('palabras.txt','r') as file:
    palabras=file.readlines()
  print('PALABRA\t\t\t IDIOMA\t\t\t CATEGORIA\n-------\t\t\t ------\t\t\t ---------')
  for palabra in palabras:
    palabraSplit=palabra.split('|')
    print(f'{palabraSplit[0]}\t\t\t {palabraSplit[1]}\t\t\t {palabraSplit[2]}')

def filtrarPalabras(criterio):
  with open('palabras.txt','r') as file:
    archivo=file.readlines()
  for palabras in archivo:
    palabra=palabras.split('|')
    if criterio in palabra:
      print(f'{palabra[0]}\t\t {palabra[1]}\t\t {palabra[2]}')

