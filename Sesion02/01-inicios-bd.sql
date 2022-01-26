CREATE DATABASE pruebas;

USE pruebas;
create table personas(
	-- Ahora definimos las columnas pertenecientas a la tabla
    id INT PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT ,  -- Solo se puede una primary,y solo una que sea incrementable. Que sea incrementableIRREPETIBLEMENTE Y DEBE ESTAR LLENO,solamente se podran almacenar numeros
    nombre VARCHAR(100) NOT NULL DEFAULT 'JAVIER', -- se podran almacenar caract. HATA 100 MAXIMO
    dni CHAR(8) UNIQUE NOT NULL, -- Se almacenaran 8 caracteres
    fecha_nacimiento DATE, -- seran solamente fecha
    created_at DATETIME NOT NULL, -- sera fecha y hora, minuto y segundo.
    sexo ENUM('MASCULINO','FEMENINO','OTRO','HELICOPTERO'), -- solamente los valores definidos en el parentesis
    estado bool -- o sera true o false
);
-- Sirve para modificar nombre de columna ALTER TABLE personas RENAME COLUMN nombre TO nombrecito;

-- aHORA Ingresamos los DATOS
-- DML  = Data Manipulation Language: Lenguaje sub de SQL
-- INSERT: Sirve para ingresar nueva info a una tabla   en especifico

INSERT INTO personas (id, nombre, dni, fecha_nacimiento, sexo, estado, created_at) VALUES 
					 (1, 'Javier', '73830351','1999-03-22', 'Masculino', true, now());
					
INSERT INTO personas (id, nombre, dni, fecha_nacimiento, sexo, estado, created_at) VALUES 
					 (2, 'Eduardo', '19837456','1999-03-22','masculino',true,now());                   
    
INSERT INTO personas (id, nombre, dni, fecha_nacimiento, sexo, estado, created_at) VALUES 
					 (3, 'Ana Maria', '19837056','1999-03-22','masculino',false,now());      
          
-- SELECT: Leer datos de una determinada tabla o tablas
SELECT nombre, id FROM personas;

SELECT * FROM personas WHERE id=1 and nombre='Javier' and estado = true;
SELECT * FROM personas WHERE id=1 and nombre='Javier' or estado = false;
 -- Aqui trases absolutamente todo en lugar de solo el nombrey id anteriormente. 


SELECT * FROM personas ORDER BY sexo ASC; 
SELECT * FROM personas ORDER BY sexo DESC; 

-- CREAR UN TABLA LLAMADA ACTIVIDADES, DONDE HAY ID, NOMBRE, INTESIDAD Y ESTADO--
-- ESTADO, LE ID TIEN QUE SER PK Y UNIQUE, EL NOMBRE NO PUEDE EXCEER LOS 20 CARACTERES, LA INTENSIDAD DEBE SER BAJA , MEDIA ,ALTA O MUY ALTA Y SU ESTADO VO F.

CREATE TABLE actividades(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT UNIQUE,
    nombre VARCHAR(20),
    intensidad ENUM('baja','media','alta','muy alta'),
    estado BOOL,
    persona_id int,
    -- para las relaciones le metemos la foreign key
    FOREIGN KEY (persona_id) REFERENCES personas(id)
);
-- Sirve para agregar una nueva columna
ALTER TABLE actividades ADD persona_id INT;
-- Sirve para agregar una nueva relacion Foreign Key en una tabla
ALTER TABLE actividades ADD FOREIGN KEY(persona_id) REFERENCES personas(id);

INSERT INTO actividades(nombre,intensidad, estado, persona_id) VALUES
					   ('PARILLADAS', 'ALTA', true, 1);
-- DDL Data Definition Language : Lenguaje de Definicion de datos
-- CREATE: Crear tablas, bases de datos y funciones y procedimientos almacenados entre otros
-- DROP: Eliminar completamente toda una tabal, una base de datos una estructura
-- ELIMINA ABSOLUTAMENTE TODO, su estructura y definición previa. TODO SE VA.alter
DROP TABLE personas;