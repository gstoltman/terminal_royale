from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fontbattle')
def fontbattle():
    return render_template('fontbattle.html')

@app.route('/themebattle')
def themebattle():
    return render_template('themebattle.html')

if __name__ == '__main__':
    app.run(debug=True)