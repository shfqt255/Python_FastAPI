from pydantic import BaseModel, Field, EmailStr, model_validator
class contactInfo(BaseModel):
    Name:str
    Email: EmailStr
    age: int

    @model_validator(mode='after')
    @classmethod
    def modalValditor(cls, model):
        if model.age <18 and not model.Email.endswith('kids.com'):
            raise ValueError('Under 18 must use kids.com ')

data={
    'Name': 'Shafqat Ullah',
    'Email': 'shfqt25@kids.com',
    'age':16

}
user=contactInfo(**data)
print(user)