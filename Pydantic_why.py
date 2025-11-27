from pydantic import BaseModel, EmailStr, AnyUrl,  Field
from typing import List, Dict, Optional, Annotated

class Patientinfo(BaseModel):
    name: str= Field(max_length=50)
    age: int=Field(gt=0, lt=150)
    email:EmailStr 
    Weight: Annotated[float, Field( strict=True, title='Weight of the patient', description='The must be number because we used strict ', examples=['Do not write 5 with colon'])]
    allergies: Optional[List[str]]=None
    Other_details: Dict[str, str]

def print_data(Info: Patientinfo):
    print(Info.name)
    print(Info.age)
    print(Info.email)
    print(Info.Other_details)
    print(Info.allergies)

given_info = {
    'Weight': 72.5, #order does not matter. 
    'name': 'shafqat ullah',
    'age': 30,
    'email': 'abd@gmail.com',
    'Other_details': {'phone': '1284848', 'email': 'shafqat@example.com'},
    # 'allergies': ['pollen', 'dust']
}

info1 = Patientinfo(**given_info)
print_data(info1)
