from flask import Flask, render_template, request, flash
import pickle
import pandas as pd
import sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


app = Flask(__name__, instance_relative_config=True)

app.secret_key = 'some_secret'

model_Hl= pickle.load(open('model_Hl.pkl', 'rb'))
model_St= pickle.load(open('model_St.pkl', 'rb'))
model_Dp= pickle.load(open('model_Dp.pkl', 'rb'))

@app.route('/')
def home():
     return render_template('index.html')


@app.route('/predicted', methods=['POST','GET'])
def predicted():
  if request.method == 'POST':
     age = request.form.get('age')
     sexe = request.form.get('sexe')
     ed_level = request.form.get('ed_level')
     neurotism = request.form['neurotism']
     extraversionness = request.form['extraversionness']
     openness = request.form['openness']
     agreability = request.form['agreability']
     conscientiousness = request.form['conscientiousness']
     impulsiveness = request.form['impulsiveness']
     sensation_seeking = request.form['sensation_seeking']
     

     print(sensation_seeking)
     exemple={'Age' : [age], 'Sexe' :[sexe],'Education_level': [ed_level],'Neuroticism':[neurotism], 'Extraversionness':[extraversionness] ,'Openness':[openness],'Agreability':[agreability],'Conscientiousness':[conscientiousness],'Impulsiveness':[impulsiveness],'Sensation_Seeking':[sensation_seeking] }
     df=pd.DataFrame.from_dict(exemple)

     
     outputs=[]
     Hl_predicted=model_Hl.predict_proba(df)
     outputs.append(Hl_predicted[0][1])

     St_predicted=model_St.predict_proba(df)
     outputs.append(St_predicted[0][1])

     Dp_predicted=model_Dp.predict_proba(df)
     outputs.append(Dp_predicted[0][1])
          
          
     names=["Hallucinogènes","Stimulants","Dépresseurs"]
     for i in range(0,3):
          text='Votre risque de consommation de drogues de type '+ names[i]+' est de '+ str(round(outputs[i],2)*100)+ '%'
          flash (text)
     
  return render_template('response.html')


@app.route('/dashboard.html')
def dashboard():
    df_consom= pd.read_csv('df_consom.csv').head(150)

    return render_template('dashboard.html',  tables=[df_consom.to_html(classes='data', header="true")])


if __name__== "__main__":    
     app.run(debug=True, port=81)
