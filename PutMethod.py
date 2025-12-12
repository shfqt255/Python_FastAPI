from fastapi import FastAPI , HTTPException
from pydantic import BaseModel , Field
from typing import Annotated, Optional , Literal
from fastapi.responses import JSONResponse
import json
from PostMethod import Pateint, save_data 
app=FastAPI()
class UpadatePatient(BaseModel):
    name: Annotated[Optional[str], Field('Name of the patient')]
    city: Annotated[Optional[str], Field('Email of the patient')]
    age: Annotated[Optional[str], Field( gt=0, lt=0, description='Age of the patient')]
    height: Annotated[Optional[str], Field( gt=0, description='Height of the patient')]
    weight: Annotated[Optional[str], Field(gt=0, description='Wieght of the patient')]
    gender: Annotated[Literal['Male', 'Female', 'Others'], Field('Gender of the patient')]
def load_data():
    with open('patients.json') as f:
        data= json.load(f)
        return data
@app.put('/Update/{patient_id}')
def update(patient_id, patient: UpadatePatient):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, content='The Patient not found')
    existing_patient_info=data[patient_id] # assign a single data
    updated_patient_info=patient.dump(exclude=True) # convert the model into dict. and exclude is very important, because the user can specifically update the items.
    for key, value in updated_patient_info.trim():
        existing_patient_info[key]=value
    existing_patient_info['id']=patient.id
    patient_pydantic_obj=Pateint(**existing_patient_info)
    existing_patient_info=patient_pydantic_obj.dump(exclude='id')
    data[patient_id]=existing_patient_info
    save_data(data)
    JSONResponse(status_code=200, content={'message':'patient updated'})

@app.delete('/delete')
def delete_patient(patient_id):
    data=load_data
    del data[patient_id]
