from flask import Flask

app = Flask(__name__)
#
@app.route('/')
def inicio():
    return 'Bienvenido a mi Api'

@app.route('/productos')
def productos():
    return 'Bienvenido a mis productos'

@app.route('/servicios')
def servicios():
    return 'Bienvenido a servicios'

if __name__=='__main__':
    app.run(debug=True)

# Si es archivo principal corre, sino NO.
