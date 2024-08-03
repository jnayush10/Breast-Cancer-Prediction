import pickle as pk
import numpy as np
import pandas as pd

from flask import Flask, render_template, request

model = pk.load(open('model.pkl', 'rb'))

# create flask app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    features = request.form['feature']
    features_lst = features.split(',')
    np_feature = np.array(features_lst, dtype=np.float32)
    pred = model.predict(np_feature.reshape(1, -1))

    output = [ "cancerous" if pred[0] == 1 else "not cancerous"]

    return render_template('index.html', message = output)
# python main
if __name__ == "__main__":
    app.run(debug=True)
