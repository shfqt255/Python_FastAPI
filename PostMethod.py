import json
from pydantic import BaseModel , Field, computed_field
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException
from typing import Annotated, Literal
class Pateint(BaseModel):
    id: Annotated[str, Field(..., description='Id is required',example='P001')]
    name: Annotated[str, Field(..., description='Name is required')]
    city: Annotated[str, Field(..., description='City Name is required')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age must be greater than zero')]
    gender: Annotated[Literal['Male', 'Female', 'Others'], Field(..., description='Gender is required' )]
    height: Annotated[float, Field(..., gt=0,  description='Required, age should be enter in meters')]
    weight: Annotated[float, Field(..., description='Required, weight should be enter in kgs')]

    
    @computed_field
    @property
    def bmi(self)->float:
        bmi=self.weight/(self.height**2)
        return bmi
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi <18.5:
            return 'Underwieght'
        elif(self.bmi <25):
            return 'Normal'
        elif(self.bmi <30):
            return 'Normal'
        else:
            return 'base'
def load_data():
        with open('patients.json') as f:
            data= json.load(f)
            return data
def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)
app= FastAPI()
@app.post('/create')
def create_patient(patient:Pateint):
    # load data
    data= load_data()
    # check if the patient is already exists.
    if(patient.id in data):
        raise HTTPException(status_code=400, detail='The Patient already exists')
    data[patient.id]=patient.model_dump(exclude=['id'])

    save_data(data)
    JSONResponse(status_code=200, content={'message': 'All is well'})

        

