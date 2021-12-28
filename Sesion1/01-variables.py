number=10
# variable numerica
numero2=10.5
#variables de texto o string:
nombre="Javier"
apellido='Barreda'
html='''<html>
<p>
</p>'''

print('Buenas noches Perú. Gracias por todo')
print(type(nombre))
print(type(number))
print(type(numero2))

edades = [14,34,32,34,78,35,13,52,31,42,74,'alfredo', True, [14,54]]
print(edades[2:6])

#En javascript tenemos los json que son diccionarios. Si no se una palabra busco en el diccinario
# y ahi saco su valor. Pues lo mismo en python. json=javascrip Object Notation

curso = {
    'nombre2':'Backend',
    'dificultad':'Dificil',
    'skills': [
        {
            'nombre':'Base de datos',
            'nivel':'Intermedio'
        },
        {
            'nombre':'ORM',
            'nivel':'Avanzado'
        }
    ]
}
print(curso['nombre2'])
print(curso['skills'][1]['nivel'])

[primer_mes,segundo_mes,tercer_mes] = ['Enero','Febrero','Marzo']

print(primer_mes)

personas = [{
        'nombre':'Javier',
        'nacionalidad':'peruana',
        'conocimientos':[
            {
                'nombre':'programacion',
                'experiencia':'1 año'
            },{
                'nombre':'ciencias ambientales',
                'experiencia':'3 años'
            }
        ]
    },{
        'nombre':'Lorena',
        'nacionalidad':'colombiana',
        'conocimientos':[
            {
                'nombre':'biología',
                'experiencia':'8 años'
            },{
                'nombre':'ciencias ambientales',
                'experiencia':'5 años'
            }
        ]
    }]

    #nacionalidad de la primera persona
    #hobbies de la segunda persona
    #experiencia del segundo conocimiento de la primera persona

print(personas[0]['nacionalidad'])   
print(personas[1]['conocimientos'])  
print(personas[0]['conocimientos'][0]['experiencia']) 

#fin de la sesion
