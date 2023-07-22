-- SQL > Structured Query Lenguage

-- DDL (Data Definition Language)
-- CREATE > Crear tablas o bases de datos
-- ALTER > Modificar la estructura de nuestras tablas o columnas
-- DROP > Eliminar tablas, columnas o bases de datos
-- TRUNCATE > Eliminar todos los registros de una tabla

CREATE DATABASE prueba;

CREATE TABLE alumnos (
id SERIAL NOT NULL PRIMARY KEY,
nombre TEXT NOT NULL,
apellidos TEXT,
correo TEXT NOT NULL UNIQUE, -- UNIQUE > significa que el valor no se puede repetir en otro registro
fecha_nacimiento DATE NOT NULL,
matriculado BOOLEAN DEFAULT true -- DEFAULT >
);
