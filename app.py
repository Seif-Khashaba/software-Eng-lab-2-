from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')  # Correct the template name here

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']

    return render_template('result.html', name=name, email=email, age=age)

if __name__ == '__main__':
    app.run(debug=True)
