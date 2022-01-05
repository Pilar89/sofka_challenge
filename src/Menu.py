from ConfigurarJuego import ConfigurarJuego
from Juego import Juego

class Menu:
  def __init__(self):
    self.configurarJuego = ConfigurarJuego()
    self.juego = Juego()

  def imprimirMenu(self):
    while True:
      print("")
      print("1. Configurar juego")
      print("2. Iniciar juego")
      print("3. Historico de jugadores")
      print("4. Salir")
      opcion = input("Elige la opcion: ")
      if opcion == "1":
        self.configurarJuego.imprimirMenu()
      elif opcion == "2":
        self.juego.iniciar()
      elif opcion == "4":
        break
      else:
        print("Opcion invalida")