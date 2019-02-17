from bottle import route, run, template, request
import json
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/json')
def returnsingle():
    # data = 
    return(data)


run(host='localhost', port=8080)