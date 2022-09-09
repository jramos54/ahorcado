def print_errors(errornumber):
  cuerpo=[]
  cuerpo_vacio=[' ',' ',' ',' ',' ',' ',' ',' ']
  partes_cuerpo=['0/','|','|','/','\\','|','/','\\']
  if errornumber==0:
    cuerpo=cuerpo_vacio.copy()
  else:
    cuerpo=cuerpo_vacio.copy()
    for i in range(errornumber):
      cuerpo[i]=partes_cuerpo[i]
  return cuerpo

def print_body(cuerpos):
  cabeza=cuerpos[0]
  cuello=cuerpos[1]
  brazo_izq=cuerpos[3]
  brazo_der=cuerpos[4]
  cuerpo=cuerpos[2]
  mas_cuerpo=cuerpos[5]
  pie_izq=cuerpos[6]
  pie_der=cuerpos[7]
  print('____________')
  print('|\n|\n|\n|\n|\n|\n|\n|\n|\n|____________')
  print('\033[10A\033[8C | \033[9B')
  print('\033[9A\033[8C | \033[8B')
  print('\033[8A\033[8C | \033[7B')
  print(f'\033[7A\033[7C{cabeza} \033[6B')
  print(f'\033[6A\033[7C{cuello} \033[5B')
  print(f'\033[5A\033[6C{brazo_izq}{cuerpo}{brazo_der} \033[4B')
  print(f'\033[4A\033[7C{mas_cuerpo} \033[3B')
  print(f'\033[3A\033[6C{pie_izq} {pie_der} \033[2B')

def print_word(word):
  print(f'\033[8A\033[18C {word} \033[7B')

def print_intentos(errors):
  print(f'\033[6A\033[18C Intentos restantes: {8-errors}  \033[5B')  

def print_ocupadas(letras):
  letras_ocupadas=' '
  for letra in letras:
    letras_ocupadas+=letra
  print(f'\033[2A\033[18C Letras ocupadas:{letras_ocupadas} \033[1B')

def print_escribe():
  print('\033[4A\033[18C escribe letra o palabra: \033[4B')
  salida=input('\033[4A\033[18C > ')
  print('\033[2B')
  return salida