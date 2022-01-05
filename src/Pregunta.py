import random
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

  def preguntar(self):
    opciones = [self.opcion1, self.opcion2, self.opcion3]
    opcionCorrecta = random.randint(0, 3)
    opciones.insert(opcionCorrecta, self.opcionCorrecta)
    print("Categoria: {}".format(self.categoria))
    print("{}?".format(self.pregunta))
    opcion = 0
    while opcion <= 3:
      print("{}. {}".format(opcion + 1, opciones[opcion]))
      opcion += 1
    opcionCorrecta += 1
    print("5. Abandonar el juego e irme con mi acumulado")
    intento = ""
    while intento == "":
      try:
        intento = input("Escoja una opcion: ")
        intento = int(intento)
      except:
        pass
    acierto = intento == opcionCorrecta
    retiro = intento == 5
    return (acierto, retiro)

  def __repr__(self):
    return "({}, {}, {}) {}".format(self.id, self.categoria, self.nivel, self.pregunta)
