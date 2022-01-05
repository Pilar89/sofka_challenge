import random
import sqlite3

con = sqlite3.connect('database.sqlite')

class Database:
  def guardarPregunta(pregunta):
    sql = """
    INSERT INTO preguntas (
      categoria,
      nivel,
      pregunta,
      opcion1,
      opcion2,
      opcion3,
      opcionCorrecta
    )
    values (?,?,?,?,?,?,?)
    """
    cur = con.cursor()
    cur.execute(sql, (
      pregunta.categoria,
      pregunta.nivel,
      pregunta.pregunta,
      pregunta.opcion1,
      pregunta.opcion2,
      pregunta.opcion3,
      pregunta.opcionCorrecta))
    con.commit()

  def consultarTodasPreguntas():
    sql = """
    select
      id,
      categoria,
      nivel,
      pregunta,
      opcion1,
      opcion2,
      opcion3,
      opcionCorrecta
    from preguntas
    order by categoria, nivel
    """
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    preguntas = []
    for row in rows:
      pregunta = Database.crearPreguntaDesdeRow(row)
      preguntas.append(pregunta)
    return preguntas

  def consultarPreguntasParaJuego():
    todasPreguntas = Database.consultarTodasPreguntas()
    random.shuffle(todasPreguntas)
    preguntas = []
    nivel = 1
    while nivel <= 5:
      for pregunta in todasPreguntas:
        if pregunta.nivel == nivel:
          preguntas.append(pregunta)
          break
      nivel += 1
    if len(preguntas) < 5:
      raise "no hay suficientes preguntas"
    return preguntas

  def crearPreguntaDesdeRow(row):
    from Pregunta import Pregunta
    pregunta = Pregunta()
    pregunta.id = row[0]
    pregunta.categoria = row[1]
    pregunta.nivel = row[2]
    pregunta.pregunta = row[3]
    pregunta.opcion1 = row[4]
    pregunta.opcion2 = row[5]
    pregunta.opcion3 = row[6]
    pregunta.opcionCorrecta = row[7]
    return pregunta

  def guardarJuego(juego):
    sql = """
    INSERT INTO historico (
      nickname,
      ronda,
      acumulado
    )
    values (?,?,?)
    """
    cur = con.cursor()
    cur.execute(sql, (
      juego.nickname,
      juego.ronda,
      juego.acumulado))
    con.commit()

  def consultarHistoricoJuegos():
    from Juego import Juego
    sql = """
    select
      nickname,
      ronda,
      acumulado
    from historico
    order by nickname, acumulado
    """
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    historico = []
    for row in rows:
      juego = Juego()
      juego.nickname = row[0]
      juego.ronda = row[1]
      juego.acumulado = row[2]
      historico.append(juego)
    return historico
