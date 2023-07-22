SELECT nombre, correo from alumnos;

SELECT * from alumnos;

SELECT * FROM alumnos WHERE matriculado = 'true';

SELECT * FROM alumnos WHERE matriculado = 'true' and nombre ='Brando';

SELECT nombre, fecha_nacimiento FROM alumnos WHERE nombre IN ('Brando', 'Maria','Maximo');

SELECT * FROM alumnos WHERE matriculado = 'true' and (nombre ='Brando' or apellidos = 'Tari Ramos');