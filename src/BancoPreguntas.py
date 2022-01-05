from Database import Database
from Pregunta import Pregunta

class BancoPreguntas:
  def imprimirMenu(self):
    while True:
      print("")
      print("1. Crear pregunta")
      print("2. Ver preguntas")
      print("3. Volver")
      opcion = input("Elige la opcion: ")
      if opcion == "1":
        Pregunta.crearNueva()
      elif opcion == "2":
        self.mostrarPreguntas()
      elif opcion == "3":
        break
      else:
        print("Opcion invalida")

  def mostrarPreguntas(self):
    preguntas = Database.consultarTodasPreguntas()
    for pregunta in preguntas:
      print(pregunta)