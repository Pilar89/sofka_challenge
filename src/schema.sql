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

insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values ('categoria1', 1, 'pregunta1', 'opcion11', 'opcion21', 'opcion31', 'opcion41');

insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values ('categoria1', 2, 'pregunta2', 'opcion12', 'opcion22', 'opcion32', 'opcion42');

insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values ('categoria1', 3, 'pregunta3', 'opcion13', 'opcion23', 'opcion33', 'opcion43');

insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values ('categoria1', 4, 'pregunta4', 'opcion14', 'opcion24', 'opcion34', 'opcion44');

insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values ('categoria1', 5, 'pregunta51', 'opcion15', 'opcion25', 'opcion35', 'opcion45');

insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values ('categoria1', 5, 'pregunta52', 'opcion15', 'opcion25', 'opcion35', 'opcion45');
