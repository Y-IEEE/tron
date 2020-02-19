from flask import Flask

app = Flask(__name__)


# TODO: temporary



@app.route('/')
def index():
    return render_template('index.html')
