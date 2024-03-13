from flask import Flask

app = Flask('__name__')

@app.route('/')
@app.route('/calculadora/<operation>/<int:num1>/<int:num2>/<int:num3>')
def calculadora(num1,num2,num3,operation):
    
    if operation == "+":
        return f" La suma de la operación es: {num1 + num2 + num3}"
    elif operation == "-":
        return f" La resta de la operación es: {num1 - num2 - num3}"
    elif operation == "*":
        return f" La multiplicacion de la operación es: {num1 * num2  *num3}"
    elif operation == "//":
        return f" La divicion de la operación es: {num1 // num2 // num3}"
    elif operation == "**":
        return f" La elevacion de la operación es: {num1 ** num2 **num3}"
    
    
if __name__ == '__main__':
    app.run(debug=True)