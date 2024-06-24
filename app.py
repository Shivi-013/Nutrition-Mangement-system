from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get the values from the frontend
        height = float(request.form['height'])/100
        weight = float(request.form['weight'])
        diet_goal = request.form['goal']

        # Perform a simple calculation
        bmi = round((weight)/(height**2),2)

        if diet_goal == 'weightLoss':
             # Render another template with the result as a parameter
            return render_template('output2.html', result=bmi)
        else:
            # Render another template with the result as a parameter
            return render_template('output.html', result=bmi)

    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)