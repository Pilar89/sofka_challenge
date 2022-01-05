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

create table historico (
  id integer primary key autoincrement,
  nickname text,
  ronda integer,
  acumulado integer
);

insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'literatura',
2,
'¿Cuál es el libro más vendido en el mundo después de la Biblia?',
'La Odisea',
'El Señor de los Anillos',
'Cien años de Soledad',
'Don Quijote de la Mancha');


insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'quimica',
1,
'La sal común está formada por dos elementos, ¿cuáles son?',
'Sodio y potasio',
'Sodio y carbono',
'Cristal y sodio',
'Sodio y cloro');


insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'cultura general',
1,
'¿Cuáles de estas construcciones famosas quedan en los Estados Unidos?',
'Torre Eiffel, Museo Guggenheim, Abadía de Westminter',
'La ciudad prohibida, la Sagrada Familia, el Panteón',
'Dancing House, 30 st Mary Axe, La Casa Blanca',
'Estatua de la Libertad, puente Golden Gate, Empire State Building');


insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'astronomia',
2,
'¿Cuál es el orden de los planetas del sistema solar, partiendo desde su centro?',
'Sol, Mercurio, Venus, Luna, Tierra, Marte, Júpiter, Saturno, Urano, Neptuno, Plutón',
'Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano, Neptuno, Plutón',
'Tierra, Venus, Mercurio, Marte, Urano, Neptuno, Plutón',
'Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano, Neptuno');



insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'zoologia',
1,
'¿Cuál es el animal terrestre más grande en la actualidad?',
'Tiburón blanco',
'Ballena azul',
'Pantera',
'Elefante africano');

insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'cultura general',
1,
'¿Cuáles son los nombres de los tres reyes magos?',
'Gaspar, Nicolas y Nataniel',
'Simon, Judas y Mateo',
'Abraham, Noé y Moises',
'Gaspar, Melchor y Baltazar');


insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'astronomia',
2,
'¿Quién fue el primer hombre en pisar la Luna?',
'Michael Collins',
'Buzz Aldrin',
'Charles Conrad',
'Neil Armstrong');

insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'biologia',
2,
'¿Cuál es el tipo sanguíneo considerado como "donante universal"?',
'Tipo A',
'Tipo B',
'Tipo AB',
'Tipo O');


insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'geografia',
3,
'¿Con qué países tiene frontera Ecuador?',
'Brasil y Colombia',
'Bolivia y Brasil',
'Perú y Bolivia',
'Colombia y Perú');

insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'matematicas',
4,
'¿Cuántos grados son necesarios para que dos ángulos sean complementarios?',
'45º',
'360º',
'180º',
'90º');

insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'matematicas',
2,
'¿Cuál es el único número primo par?',
'4',
'3',
'6',
'2');


insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'geografia',
3,
'¿Cuál es el país más grande y el más pequeño del mundo?',
'China y Nauru',
'Estados Unidos y Malta',
'Canadá y Mónaco',
'Rusia y Vaticano');

insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'historia',
4,
'¿Quién pintó la obra "Guernica"?',
'Leonardo DaVinci',
'Frida Kahlo',
'Diego Rivera',
'Pablo Picasso');


insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'historia',
3,
'¿Cuál es el tema del famoso discurso "I have a dream" de Martin Luther King?',
'La Justicia para los menos favorecidos',
'La intolerancia religiosa',
'El premio Nobel de la Paz',
'La igualdad de las razas'); 


insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'historia',
4,
'¿En qué periodo de la prehistoria fue descubierto el fuego?',
'Neolítico',
'Edad de los metales',
'Edad de piedra',
'Paleolítico');

insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'biologia',
3,
'¿Cuál es el cromosoma que determina el sexo masculino?',
'El cromosoma XX',
'El cromosoma X',
'El cromosoma M',
'El cromosoma Y');

insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'quimica',
4,
'¿Cuál es el metal cuyo símbolo químico es Au?',
'Aluminio',
'Arsénico',
'Hierro',
'Oro');


insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'historia',
5,
'¿Quién pintó la bóveda de la capilla sixtina?',
'Donatello',
'Boticelli',
'Leonardo da Vinci',
'Miguel Angel');


insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'zoologia',
5,
'¿Cuáles son los tres predadores del reino animal reconocidos por: 1) habilidad de cazar en grupo, 2) camuflajearse para sorprender a su presa, 3) poseer sentidos refinados?',
'1) León; 2) tiburón blanco; 3) orca',
'1) Tiburón blanco; 2) elefante; 3) escorpión',
'1) Cobra; 2) zorro; 3) cocodrilo',
'1) Hiena; 2) Oso polar; 3) Lobo gris');



insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'historia',
5,
'Según la leyenda de la fundación de Roma, ¿quién amamantó a los gemelos Rómulo y Remo?',
'Una cabra',
'Una vaca',
'Una oveja',
'Una loba');


insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'geografia',
5,
'¿En qué océano queda Madagascar?',
'Océano Pacífico',
'Océano Atlántico',
'Océano Antártico',
'Océano Índico');


insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'historia',
5,
'¿Dónde se originaron los números arábigos?',
'Arabia',
'Persia',
'Roma',
'India');


insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'zoologia',
4,
'¿Cuántas patas tiene una araña?',
'10',
'6',
'12',
'8');


insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'zoologia',
1,
'¿Cuál es el único mamífero que puede volar?',
'Buho',
'Águila',
'Avestruz',
'Murciélago');

insert into preguntas (categoria,nivel,pregunta,opcion1,opcion2,opcion3,opcionCorrecta)
values (
'zoologia',
3,
'¿Cuántos corazones tienen los pulpos?',
'1',
'8',
'4',
'3');
