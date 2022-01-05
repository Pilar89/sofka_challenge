from BancoPreguntas import BancoPreguntas

class Menu:
  def __init__(self):
    self.bancoPreguntas = BancoPreguntas()

  def imprimirMenu(self):
    while True:
      print("")
      print("1. Configurar juego")
      print("2. Iniciar juego")
      print("3. Salir")
      opcion = input("Elige la opcion: ")
      if opcion == "1":
        self.bancoPreguntas.imprimirMenu()
      elif opcion == "3":
        break
      else:
        print("Opcion invalida")