from simple_term_menu import TerminalMenu
import random

def menu():
  options=['juego','estadisticas','catalogo']
  terminalMenu=TerminalMenu(options)
  menuIndex=terminalMenu.show()
  return menuIndex

def launchScreens(option):
  options={0:'juego.py',1:'statistics.py',2:'catalogo.py'}
  with open(options[option]) as f:
    code=f.read()
  return code
      
if __name__=='__main__':
  option=menu()
  selection=launchScreens(option)
  exec(selection)
