from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
    #return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port=8000)

"Some changes added" 
"some changes added" 
