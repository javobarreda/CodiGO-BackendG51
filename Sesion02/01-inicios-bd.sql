CREATE DATABASE pruebas;
create table personas(
	-- Ahora definimos las columnas pertenecientas a la tabla
    id INT,  -- solamente se podran almacenar numeros
    nombre VARCHAR(100), -- se podran almacenar caract. HATA 100 MAXIMO
    dni CHAR(8), -- Se almacenaran 8 caracteres
    fecha_nacimiento DATE, -- seran solamente fecha
    create_at DATETIME, -- sera fecha y hora, minuto y segundo.
    sexo ENUM('MASCULINO','FEMENINO','OTRO','HELICOPTERO'), -- solamente los valores definidos en el parentesis
    estado bool -- o sera true o false
    
);