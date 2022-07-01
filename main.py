# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class model_input(BaseModel):
    age : int
    sex : int
    chest_pain : int
    restbp : int
    cholestoral : int
    fasting_blood_sugar : int
    restecg : int
    max_heart_rate : int
    exercise_angina : int
    oldpeak : float
    slope : int
    major_vessels : int
    thal : int

#loading the saved model
heartdisease_model=pickle.load(open('heartdisease_model.sav','rb'))

@app.post('/heartdisease_prediction')

def heartdiseasepred(input_parameters: model_input):
    input_data=input_parameters.json()
    input_dictionary=json.loads(input_data)
    
    age=input_dictionary['age']
    sex=input_dictionary['sex']
    cp=input_dictionary['chest_pain']
    rbp=input_dictionary['restbp']
    cl=input_dictionary['cholestoral']
    fbs=input_dictionary['fasting_blood_sugar']
    recg=input_dictionary['restecg']
    mhr=input_dictionary['max_heart_rate']
    ang=input_dictionary['exercise_angina']
    oldpeak=input_dictionary['oldpeak']
    slop=input_dictionary['slope']
    mv=input_dictionary['major_vessels']
    thal=input_dictionary['thal']
    
    input_list=[age,sex,cp,rbp,cl,fbs,recg,mhr,ang,oldpeak,slop,mv,thal]
    prediction=heartdisease_model.predict([input_list])
    if(prediction[0]==0):
        return "The person has a Healthy Heart"
    else:
        return "The person has a Heart Disease"
    

