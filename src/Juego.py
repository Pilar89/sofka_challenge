from Database import Database
from Historico import Historico

class Juego:
  def iniciar(self):
    nickname = ""
    while nickname == "":
      nickname = input("Escribe tu nickname: ")
    self.nickname = nickname

    preguntas = []
    try:
      preguntas = Database.consultarPreguntasParaJuego()
    except e:
      print(e)
      return

    premios = [0, 1000, 2000, 3000, 5000, 8000]
    ronda = 1
    acumulado = 0
    retirado = False
    for pregunta in preguntas:
      print("Ronda {}, acumulado {}".format(ronda, acumulado))
      (acierto, retirado) = pregunta.preguntar()
      if not acierto:
        break
      acumulado += premios[ronda]
      ronda += 1
      print("Bien! Continuas a la siguiente ronda.")
    if retirado:
      print("Te retiraste con un total ganado de {}".format(acumulado))
    elif ronda > 5:
      print("Felicitaciones. Total ganado de {}".format(acumulado))
    else:
      print("Uppps, perdiste todo")

    self.ronda = ronda
    self.acumulado = acumulado
    Historico.guardarJuego(self)

  def __repr__(self):
    return "{}, ronda {}, acumulado {}".format(self.nickname, self.ronda, self.acumulado)


