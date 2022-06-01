#Note: using Flask 1.1.1 was throwing an error with Jinja and then markup safe
#I tried to downgrade all of these, but it still would not work. So for now I have used Flask 2.1.2

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/')
def main():
    """root landing page"""
    return "Welcome to the Calculator"

@app.route('/add')
def addition():
    """ Add a and b the return answer """

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = add(a,b)
    return f"{res}"

@app.route('/sub')
def subtraction():
    """ Subtract a and b then return answer """

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = sub(a,b)
    return f"{res}"

@app.route('/mult')
def multipliction():
""" Multiply a and b then return answer """

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = mult(a,b)
    return f"{res}"

@app.route('/div')
def division():
    """ Divide a and b then return answer """

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = div(a,b)
    return f"{res}"


operations = {
    'add' : add,
    'sub' : sub,
    'mult' : mult,
    'div' : div
}

@app.route('/math/<operation>')
def math(operation):
""" Do math operation in query with a and b with help from 
operations dictionary then return answer """

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = operations[operation](a,b)
    return f"{res}"