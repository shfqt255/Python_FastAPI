from fastapi import FastAPI, Path
import json

app=FastAPI()

def load_data():
    with open("patients.json", "r") as f:
       data= json.load(f)
       return data

@app.get("/readAll")
def read():
   data= load_data()
   return data

@app.get("/pateint/{pateint_id}")
def  readSpecificPateint(pateint_id: str=Path(..., description="Patient Id in DB", examples="P001")): 
   # ... means it is required. In path we can des,examp,greaterEqual etc.
   data=load_data()
   if pateint_id in data:
      return data[pateint_id]
   else:
      return "An Error occured"