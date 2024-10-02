from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def aritmetica():

    if request.method == "POST":
        num1 = float(request.form.get('n1'))
        num2 = float(request.form.get('n2'))
        
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        
        if num2 != 0:
            division = num1 / num2
        else:
            division = 'Error: División por cero'
        
        return render_template('index.html', total_suma=suma,
                                            total_resta=resta,
                                            total_multi=multiplicacion,
                                            total_divi=division)

    return render_template('index.html')

@app.route('/divisa', methods=['GET', 'POST'])
def divisas():
       
    if request.method == "POST":
        num = float(request.form.get('num'))
        resultado = num / 4223.03  

        return render_template('divisa.html', resultado=resultado)

    return render_template('divisa.html')

if __name__ == "__main__": 
    app.run(debug=True)



   
