from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model.predict(final)
    prediction = float(prediction)
    print(prediction)

    if prediction < int(50):
        return render_template('index.html',
                               pred='For Values of SO2 "{0}", NO2 "{1}", RSPM "{2}", SPM "{3}", The Quality of Air is '
                                    'Good.\n ''AQI is {4}'.format(int_features[0], int_features[1], int_features[2],
                                                                  int_features[3], prediction))
    elif prediction < int(100):
        return render_template('index.html',
                               pred='For Values of SO2 "{0}", NO2 "{1}", RSPM "{2}", SPM "{3}", The Quality of Air is '
                                    'Satisfactory.\n ''AQI is {4}'.format(int_features[0], int_features[1],
                                                                          int_features[2],
                                                                          int_features[3], prediction))
    elif prediction < int(200):
        return render_template('index.html',
                               pred='For Values of SO2 "{0}", NO2 "{1}", RSPM "{2}", SPM "{3}", The Quality of Air is '
                                    'Moderately Polluted.\n ''AQI is {4}'.format(int_features[0], int_features[1],
                                                                                 int_features[2],
                                                                                 int_features[3], prediction))
    elif prediction < int(300):
        return render_template('index.html',
                               pred='For Values of SO2 "{0}", NO2 "{1}", RSPM "{2}", SPM "{3}", The Quality of Air is '
                                    'Poor.\n ''AQI is {4}'.format(int_features[0], int_features[1],
                                                                  int_features[2],
                                                                  int_features[3], prediction))
    elif prediction < int(400):
        return render_template('index.html',
                               pred='For Values of SO2 "{0}", NO2 "{1}", RSPM "{2}", SPM "{3}", The Quality of Air is '
                                    'very Poor.\n ''AQI is {4}'.format(int_features[0], int_features[1],
                                                                       int_features[2],
                                                                       int_features[3], prediction))
    else:
        return render_template('index.html',
                               pred='For Values of SO2 "{0}", NO2 "{1}", RSPM "{2}", SPM "{3}", The Quality of Air is '
                                    'Severe.\n ''AQI is {4}'.format(int_features[0], int_features[1],
                                                                    int_features[2],
                                                                    int_features[3], prediction))


if __name__ == '__main__':
    app.run(debug=True)
