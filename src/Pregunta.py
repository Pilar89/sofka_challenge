from Database import Database

class Pregunta:
  def crearNueva():
    while True:
      pregunta = Pregunta()
      pregunta.categoria = input("Escribe la categoria: ")
      pregunta.nivel = input("Escribe el nivel de la pregunta, de 1 a 5: ")
      pregunta.pregunta = input("Escribe la pregunta: ")
      pregunta.opcion1 = input("Escribe la primera opcion de respuesta incorrecta: ")
      pregunta.opcion2 = input("Escribe la segunda opcion de respuesta incorrecta: ")
      pregunta.opcion3 = input("Escribe la tercera opcion de respuesta incorrecta: ")
      pregunta.opcionCorrecta = input("Escribe la opcion de respuesta correcta: ")
      if pregunta.esValida():
        break
      print("Pregunta con datos vacios o no validos")

    pregunta.guardar()

  def esValida(self):
    try:
      self.nivel = int(self.nivel)
      return (self.categoria != ""
        and self.nivel >= 1
        and self.nivel <= 5
        and self.pregunta != ""
        and self.opcion1 != ""
        and self.opcion2 != ""
        and self.opcion3 != ""
        and self.opcionCorrecta != "")
    except:
      return False

  def guardar(self):
    Database.guardarPregunta(self)
