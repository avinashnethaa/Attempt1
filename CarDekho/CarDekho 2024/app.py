from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('models/random_forest_regression_model1.pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')  # Fix typo here

standard_to_ = StandardScaler()

@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel = 0
    if request.method == 'POST':
        YEAR = int(request.form['Year'])
        Present_Price = float(request.form['Present_Price'])  # Fix typo here
        Kms_Driven = int(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        Fuel_Type_Petrol = request.form['Fuel_Type_Petrol']
        if Fuel_Type_Petrol == 'Petrol':
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        else:
            Fuel_Type_Diesel = 1
            Fuel_Type_Petrol = 0
        Year = 2024 - YEAR
        Seller_Type_Individual = request.form['Seller_Type_Individual']
        if Seller_Type_Individual == 'Individual':
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0
        Transmission_Manual = request.form['Transmission_Manual']
        if Transmission_Manual == 'Manual':
            Transmission_Manual = 1
        else:
            Transmission_Manual = 0
        # Correct the usage of features in the model prediction
        Prediction = model.predict([[Present_Price, Kms_Driven, Owner, Fuel_Type_Petrol, Year,
                                    Seller_Type_Individual, Transmission_Manual]])
        output = round(Prediction[0], 2)
        if output < 0:
            return render_template('index.html', prediction_text='Sorry Your')
        else:
            return render_template('index.html', prediction_text='You can check below')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
