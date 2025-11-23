from fastapi import FastAPI, Path, HTTPException, Query
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
      raise HTTPException(status_code=404, details="Not found")
   
@app.get("/sort")
def sort(sort_by, order):
   sort_by2=["height", "weight", "bmi", "age"]
   order2=["asc", "dsc"]
   if sort_by not in sort_by2:
      raise HTTPException(status_code=400, details="Inavlid Request")
   if order not in order2:
      raise HTTPException(status_code=400, details="Inalid request")
   data=load_data()
   reverse= False if order!="dsc" else True 
   sorted_data=sorted(data.values(), key= lambda x: x.get(sort_by, 0), reverse=reverse)
   return sorted_data