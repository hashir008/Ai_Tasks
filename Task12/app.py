from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
app = Flask(__name__)
data = pd.read_csv('data.csv')
for col in data.columns:
    data[col] = data[col].fillna(data[col].mode()[0])
data = data.drop(columns=['Name'])
cat_columns = data.select_dtypes(['object']).columns
encoders = {}
for col in cat_columns:
    codes, uniques = pd.factorize(data[col])
    data[col] = codes
    encoders[col] = uniques  # Save for decoding predictions
x = data.drop(columns=['Company'])
y = data['Company']
# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x, y)
company_names = encoders['Company']
@app.route('/')
def index():
    return render_template('index.html', columns=x.columns)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_features = []
        for col in x.columns:
            val = request.form.get(col)
            if col == 'OS':
                os_list = list(encoders['OS'])
                os_input = val.strip()
                if os_input in os_list:
                    input_features.append(os_list.index(os_input))
                else:
                    input_features.append(0)
            else:
                input_features.append(float(val))
        final_features = [np.array(input_features)]
        prediction = model.predict(final_features)
        predicted_company = company_names[prediction[0]]

        return render_template('index.html',
                               prediction_text=f'Predicted Company: {predicted_company}',
                               columns=x.columns)
    except Exception as e:
        return render_template('index.html',
                               prediction_text=f'Error: {str(e)}',
                               columns=x.columns)
if __name__ == '__main__':
    app.run(debug=True)