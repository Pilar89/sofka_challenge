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

  def consultarPreguntas():
    from Pregunta import Pregunta
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
      pregunta = Pregunta()
      pregunta.id = row[0]
      pregunta.categoria = row[1]
      pregunta.nivel = row[2]
      pregunta.pregunta = row[3]
      pregunta.opcion1 = row[4]
      pregunta.opcion2 = row[5]
      pregunta.opcion3 = row[6]
      pregunta.opcionCorrecta = row[7]
      preguntas.append(pregunta)
    return preguntas
