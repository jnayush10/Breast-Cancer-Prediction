import pickle as pk
import nump as np
import pandas as pd
from flask import Flask, request, render_template

model = pk.load(open('model.pkl', 'rb'))

# create flask app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    pass


# python main
if __name__ == "__main__":
    app.run(debug=True)
