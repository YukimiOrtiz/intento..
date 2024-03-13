from flask import Flask

app = Flask ('__name__')

@app.route('/')
@app.route('/calculadora/<operation>/<int:num1>/<int:num2>')
def calculadora(n1,n2,operation):
    if operation == "+":
        return f" La suma de como resultado: {n1 + n2}"
    elif operation == "-":
        return f" La resta da como resultado: {n1 - n2}"
    elif operation == "*":
        return f" La multiplicacion da como resultado: {n1 * n2}"
    elif operation == "/":
        return f" La divicion de como resultado: {n1 / n2}"
    elif operation == "**":
        return f" La elevacion da como resultado: {n1 ** n2}"
    
    
if __name__ == '__main__':
    app.run(debug=True)