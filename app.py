from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>WELCOME</h1>'

@app.route('/home')
def home():
    return '<h1>WELCOME HOME</h1>'

@app.route('/back')
def back():
    return '<h1>WELCOME BACK</h1>'

if __name__=="__main__":
    app.run(debug=True)