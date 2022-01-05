from Database import Database

class Historico:
  def mostrar():
    historico = Database.consultarHistoricoJuegos()
    for juego in historico:
      print(juego)

  def guardarJuego(juego):
    Database.guardarJuego(juego)