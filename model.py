#import necessary libraries
import pandas as pd
import numpy as np

import warnings

warnings.filterwarnings("ignore")


from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split



from sklearn.ensemble import RandomForestRegressor


import pickle

df=pd.read_csv("hour.csv")

Out_column=[	"atemp",	"hum",	"windspeed"]
def rem_Outlier(data,col):
    q1,q2,q3=np.percentile(data[col],(25,50,75))
    IQR=q3-q1
    lower_limit=q1-(1.5*IQR)
    upper_limit=q3+(1.5*IQR)
    df[col]=np.where(df[col]<lower_limit,lower_limit,df[col])
    df[col]=np.where(df[col]>upper_limit,upper_limit,df[col])
    
for col in Out_column:
    rem_Outlier(df,col)

categorical_features = ['season', 'mnth', 'hr', 'weekday', 'weathersit', 'yr']
df= pd.get_dummies(df, columns=categorical_features, drop_first=True)

df.drop(columns=["instant","dteday","casual","registered","temp"],axis=1,inplace=True)

y=df["cnt"]
x=df.drop("cnt",axis=1)

#scaling
scaling=StandardScaler()
x=scaling.fit_transform(x)
x=pd.DataFrame(x)

with open("scaling.pkl","wb") as f:
    pickle.dump(scaling,f)

x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=42,test_size=0.33)

#train the best model

Rf=RandomForestRegressor()
Rf.fit(x_train,y_train)

#save the model

with open("model.pkl","wb") as f:
    pickle.dump(Rf,f)

