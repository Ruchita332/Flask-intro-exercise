# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)



@app.route('/')
def index():
    """Starting page"""
    return "Lets do some math!!!"

@app.route('/add')
def do_add():
    """/add
    Adds a and b and returns result as the body.
    """ 
    a = int(request.args.get("a"));
    b = int(request.args.get("b"));
    r_val = str(operations.add (a, b));
    
    # return f"Sum of {a} and {b} is {r_val}";
    return r_val;

@app.route ('/sub')
def do_sub():
    """
    /sub
    Same, subtracting b from a.
    """
    a = int(request.args ["a"]);
    b = int(request.args ["b"]);
    r_val = str(operations.sub (a, b));
    
    # return f"Sub of {a} and {b} is {r_val}";
    return r_val;

@app.route('/mult')
def do_mult():
    """
    /mult
    Same, multiplying a and b.
    """
    a = int(request.args ["a"]);
    b = int(request.args ["b"]);
    r_val = str(operations.mult (a, b));
    
    # return f"Mult of {a} and {b} is {r_val}";
    return r_val;

@app.route ('/div')
def do_div():
    """
    /div
    Same, dividing a by b.
    """
    a = int(request.args ["a"]);
    b = int(request.args ["b"]);
    r_val = str(operations.div (a, b));
    
    # return f"Div of {a} and {b} is {r_val}";
    return r_val;

# Further Study Section

@app.route ('/math/<oper>')
def do_math (oper):
    """Do math on a and b"""
    a = int(request.args ["a"]);
    b = int(request.args ["b"]);
    result = operations.operators[oper](a, b)  #this is an int

    return str(result);

