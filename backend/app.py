from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "API operativa con código montado desde el host"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
