# Put your app in here.
from flask import Flask,request
from operations import add, sub, mult, div
app = Flask(__name__)



@app.route('/add')
def url_adding():
    """adding a and b parameters from the url"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)
    return f'<h1>{result}</h1>'

@app.route('/sub')
def url_sub():
    """subtracting a and b parameters from the url"""
    a = int(request.args.get('a'))   
    b = int(request.args.get('b'))   
    result = sub(a,b)
    return str(result)

@app.route('/mult')
def url_mult():
    """multiplying a and b parameters from the url"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)
    return str(result)
@app.route('/div')
def url_div():
    """dividing a and b parameters from the url"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)
    return str(result)

func_dict= {
    'add':add,
    'sub':sub,
    'mult':mult,
    'div':div
}
@app.route('/math/<operation>')
def simplify_func(operation):
    """Avoiding repeating codes
    Putting all codes/operations in one place"""
    url_operation = func_dict.get(operation)
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = url_operation(a,b)
    return str(result)