from flask import Flask, g, request

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return "Hello, world! - Flask"

if __name__ == '__main__':
    app.run(debug=True)
