import random
from screenprint import *
from simple_term_menu import TerminalMenu
import os

def select_Palabra(idioma):
  exist=True
  with open('palabras.txt') as f:
    lineas=f.readlines()
  while exist:
    linea=random.choice(lineas)
    if idioma in linea:
      exist=False
      palabra=linea.split('|')
      return palabra[0]

def menu_juego():
  options=['español','ingles']
  submenu=TerminalMenu(options)
  indexselection=submenu.show()
  idioma=options[indexselection]
  return idioma

def palabra_juego(letra,word,newword):

  arr=newword.split(' ')
  newword=''.join(arr)
  myword=['' for x in range(len(word))]
  for i,letraComp in enumerate(word):
    if letraComp == newword[i]:
      myword[i]='>'
    else:
      myword[i]=letraComp
      
    
  if letra=='>':
    letra_vacia=[x+' ' for x in newword]
    return ''.join(letra_vacia)
  else:
    letra_vacia=[x+' ' for x in newword if x!=' ']
    if letra in myword:
      pos_letra=myword.index(letra)
      letra_vacia[pos_letra]=myword[pos_letra]
      return ''.join(letra_vacia)
    
idioma=menu_juego()
errors=0
letras=[]
letra='>'
word=select_Palabra(idioma)
startwordarr=['_' for x in range(len(word))]
startword=''.join(startwordarr)
palabra=palabra_juego(letra,word,startword)
newword=palabra
runJuego=True

while runJuego:
  os.system('clear')
  cuerpos=print_errors(errors)
  
  print_body(cuerpos)
  print_word(newword)
  print_intentos(errors)
  print_ocupadas(letras)
  letra=print_escribe()
  if letra in word:
    palabra=palabra_juego(letra,word,newword)
    newword=palabra
    palabra=newword.split(' ')
    palcomp=''.join(palabra)
    if word==palcomp:
      runJuego=False
      print(f'Ganaste la palabra es {word}')
  else:
    errors+=1
    letras.append(letra)  
    if errors>=8:
      runJuego=False
      print(f'PERDISTE la palabra es {word}')
