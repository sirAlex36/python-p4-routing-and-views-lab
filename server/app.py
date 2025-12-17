#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route ('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/<string:username>')
def user_profile(username): 

    return f'<h1>Profile for {username}</h1>'

@app.route('/print/<string:value>')
def print_value(value):
    """
    Handles paths like: /print/hello
    Returns the string captured in the URL.
    """
    # Simply return the value captured from the URL
    print(value)
    return value

@app.route('/count/<int:num>')
def count_to_num(num):
    """
    Handles paths like: /count/5
    """
    # For now, we return a string to satisfy the 200 OK status
    # Usually, this route expects a specific string or range
    result =""
    for i in range(num):
        result += f"{i}\n"
    return result

# ... (existing routes) ...

@app.route('/math/<int:num1>/<string:operator>/<int:num2>')
def do_math(num1, operator, num2):
    # Perform the calculation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == 'div': 
        result = num1 / num2
    elif operator == '%':  # Added for the modulo test
        result = num1 % num2
    else:
        return "Invalid Operator", 400
        
    # Return ONLY the result as a string to match the test '10'
    return str(result)



if __name__ == '__main__':
    app.run(port=5555, debug=True)
