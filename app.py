from flask import  Flask,render_template,request
import pickle 
import pandas as pd
import numpy as np

app=Flask(__name__)


model=pickle.load(open("model.pkl","rb"))

scaled=pickle.load(open("scaling.pkl","rb"))

print("loaded")

@app.route('/')

def home():
    return render_template('index.html')

@app.route("/predict",methods=["POST"])

def predict():
    if request.method=="POST":
        try:
            atemp=float(request.form["atemp"])
            hum=float(request.form["hum"])
            windspeed=float(request.form["windspeed"])
            holiday=int(request.form["holiday"])
            workingday=int(request.form["workingday"])
            season=int(request.form["season"])
            yr=int(request.form["yr"])
            mnth=int(request.form["mnth"])
            hr=int(request.form["hr"])
            weekday=int(request.form["weekday"])
            weathersit=int(request.form["weathersit"])

            #for one hot encoding creating a dataframe

            input_data={
                'holiday': holiday,
                'workingday': workingday,
                'atemp': atemp,
                'hum': hum,
                'windspeed': windspeed,
                'season': season,
                'yr': yr,
                'mnth': mnth,
                'hr': hr,
                'weekday': weekday,
                'weathersit': weathersit
            }
            input_df=pd.DataFrame([input_data])

            #OneHot Encoding
            categorical_features = ['season', 'mnth', 'hr', 'weekday', 'weathersit', 'yr']

            df=pd.get_dummies(input_df,columns=categorical_features,drop_first=True)

            model_columns=['holiday', 'workingday', 'atemp', 'hum', 'windspeed', 'season_2',
       'season_3', 'season_4', 'mnth_2', 'mnth_3', 'mnth_4', 'mnth_5',
       'mnth_6', 'mnth_7', 'mnth_8', 'mnth_9', 'mnth_10', 'mnth_11', 'mnth_12',
       'hr_1', 'hr_2', 'hr_3', 'hr_4', 'hr_5', 'hr_6', 'hr_7', 'hr_8', 'hr_9',
       'hr_10', 'hr_11', 'hr_12', 'hr_13', 'hr_14', 'hr_15', 'hr_16', 'hr_17',
       'hr_18', 'hr_19', 'hr_20', 'hr_21', 'hr_22', 'hr_23', 'weekday_1',
       'weekday_2', 'weekday_3', 'weekday_4', 'weekday_5', 'weekday_6',
       'weathersit_2', 'weathersit_3', 'weathersit_4', 'yr_1']
            
            input_reindexed=df.reindex(columns=model_columns,fill_value=0)
            


            data_scaled=scaled.transform(input_reindexed)

            prediction=model.predict(data_scaled)

            output=int(round(prediction[0],0))



            return render_template("index.html",prediction_text=f"Predicted Hourly Rentals:{output}")
        
        except Exception as e:
            return render_template("index.html",prediction_text=f"Error:{str(e)}")
        
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)










