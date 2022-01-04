from flask import Flask, request
# el request nos da toda la información del cliente: hora de solicitud, info, método al cual quiere acceder el cliente.

app = Flask(__name__)

#endpoint. NO SE DICE URL. el URL es el dominio + endpoint
@app.route('/', methods=['POST','GET'])
def inicio():
    # REQUEST.method nos da el metodo que esta queriendo acceder el cliente Y cómo podriamos ver si e sun post o un get.
    #Y como sabemos si es GETO o POST?
    print(request.method)

    if request.method =='POST':
    # Captura lel json enviado por el cliente y lo convierte a un diccionario para que python lo entienda.
        print (request.get_json())
    # validar si hay el nombre y si lo hay entonces retornar un saludo con ese nombre: Hola, Javier!
    # SI no hay nombre, entonces indicar que falta info: ESTADO 400
        data = request.get_json()
        #guardo diccionario en variable llamada data
        if(data['nombre']):
            #si hay variable nombre en data entonces
            nombre = data['nombre']
            return 'Hola,{}!'.format(nombre)
        else:
            return 'Necesito la info',400

    elif request.method =='GET':
        return  'Bienvenido a mi API de productos', 200

if __name__=='__main__':
    app.run(debug=True)

# Si es que name igual a main recien ingresamos a la línea 6. Pero si es un archivo seundario, NO podra levantar el proyecto, entonces no se usará FLASK. Es para validar el proyecto. 

