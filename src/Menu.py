from ConfigurarJuego import ConfigurarJuego
from Historico import Historico
from Juego import Juego

class Menu:
  def __init__(self):
    self.configurarJuego = ConfigurarJuego()

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
        juego = Juego()
        juego.iniciar()
      elif opcion == "3":
        Historico.mostrar()
      elif opcion == "4":
        break
      else:
        print("Opcion invalida")