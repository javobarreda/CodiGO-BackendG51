class Persona:
    # variables > atributos. Variables dentro de clase son ATRIBUTOS
    #las variables dentro de una clase son ATRIBUTOS.
    nombre=''
    edad=0
    estatura=0.0

    def saludar():
        print('Hola')
# Funcion dentro de clase = METODOS. Es una acción de la persona.

    def __init__(self, nombre_de_la_persona, edad_persona,estatura_persona, sexo_persona):
        self.nombre = nombre_de_la_persona
        self.edad = edad_persona
        self.estatura = estatura_persona
        self.sexo= sexo_persona
#Con el constructor inicializamos los atributos de la clase
# self sirve para referenciar a la plantilla que se esta utilizando. Con el atributo self referencias todos los atr y metodos en la presente instalizacion. SE HACE UNA FOTO COPIA modificando los atributos.

    # aqui estamos inicializando las variables. Estas variables no pueden ser utilizadas aqui
    #porque la clase es la plantilla. 
    #ESTO ES: CUANDO CREES A UNA PERSONA, usarás estas características:

javier = Persona(nombre_de_la_persona='Javier', edad_persona=22, estatura_persona=1.72, sexo_persona='Masculino')
print(javier.nombre)
    #Para que las características salgan al lado de persona como linea 11, debemos cntar con un inicializador = constructor. Ese es el encargado de inicializar las variables de una clase.