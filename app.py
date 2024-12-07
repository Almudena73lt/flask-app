from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Bienvenidos a mi aplicación Flask!'

@app.route('/about')
def about():
    return '¡Acerca de esta página!'

@app.route('/uic')
def uic.func():
    return 'uic'

if __name__=='__main__':
    app.run(debug=True)










