from flask import Flask, render_template, request
import numpy as np
import pickle

# Load the model
model = pickle.load(open('models/model.pkl', 'rb'))

# Flask app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get features from the form
    features = request.form['feature']  # User input as a comma-separated string
    features = features.split(',')  # Split the string into a list
    np_features = np.asarray(features, dtype=np.float32)  # Convert to NumPy array

    # Predict
    pred = model.predict(np_features.reshape(1, -1))  # Reshape for a single prediction
    message = ['Cancrouse' if pred[0] == 1 else 'Not Cancrouse']

    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
