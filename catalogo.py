from simple_term_menu import TerminalMenu
from filewrite import *
import os
os.system('clear')

print('Catalogo de Palabras'.center(80))

def menu():
  options=['Listar Palabras','Agregar Palabras','Regresar Anterior']
  catalogoMenu=TerminalMenu(options)
  indexSelection=catalogoMenu.show()
  return indexSelection

def submenu():
  options=['Menu catalogo','Menu principal','Salir']
  submenu=TerminalMenu(options)
  indexSelection=submenu.show()
  return indexSelection

def execmenu(option):
  options={0:'catalogo.py',1:'main.py',2:'os.system("clear")\nprint("Juego terminado, bye")'}
  if option==2:
    return options[option]
  else:
    with open(options[option]) as f:
      code=f.read()
      
  return code

selection=menu()

if selection==0:
  listaPalabras()
  option=submenu()
  exec(execmenu(option))

if selection==1:
  palabra=input('Ingrese la palabra a agregar: ')
  idioma=input('Ingrese el idioma de la palabra agregada: ')
  categoria=input('Ingresa una clasificacion: ')
  guardarPalabra(palabra,idioma,categoria)

if selection==2:
  exec(open('main.py').read())
  