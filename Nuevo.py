from flask import Flask

app = Flask('__name__')

@app.route("/nuevo")
@app.route("/nuevo/<name>")
@app.route("/nuevo/<name>/<int:edad>")
def nuevo(name= None, edad= None):
    if edad == None:
        
     return f"Tu nombre es: {name}"
 
    else:
        
       return f"Tu nombre es: {name} y su edad es: {edad}" 

if __name__ =='__main__':
    app.run(debug=True)