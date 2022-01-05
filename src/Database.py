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