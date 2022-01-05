create table preguntas (
  id integer primary key autoincrement,
  categoria text,
  nivel integer,
  pregunta text,
  opcion1 text,
  opcion2 text,
  opcion3 text,
  opcionCorrecta text
);
