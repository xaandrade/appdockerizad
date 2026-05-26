import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    entorno = os.getenv('APP_ENV', 'development').upper()
    return render_template('index.html', entorno=entorno)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)