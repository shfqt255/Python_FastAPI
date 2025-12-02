from pydantic import BaseModel, field_validator, Field, EmailStr
class PatientInfo(BaseModel):
    Name: str
    Email: EmailStr
    marks:int
    @field_validator('Email')
    @classmethod # Field validator hamesha class method hota hai
    def email_validator(cls, value):
        valid_domains=['gmail.com' , 'careers.com', 'hiring.com']
        domain_names=value.split('@')[-1]
        if domain_names not in valid_domains:
            raise ValueError('Not a valid email')
        else:
            return value

    @field_validator('Name', ) 
    @classmethod
    def name_validator(cls, value):
        return value.upper()

    @field_validator('marks',mode='before') # Mode before is used to validate the value before transformation. And default one which is after
#used to validate the value after transformation. The transition is **info . This before mode will show an error. Becuase it connot deal to compare 
# string 50 with intger 0 or 100. The after mode will work becaouse it will convert the 50 in int.
    @classmethod
    def marks_validator(cls, value):
            if 0 < value <= 100:
                return value
            else:
             raise ValueError('Marks must be between 0 and 100')

info={
    'Name' : 'Shafqat Ullah',
    'Email': 'shfqt25@gmail.com',
    'marks':'50',
    }

info_obj=PatientInfo(**info)

def print_data(info: PatientInfo):
    print(info.Name)
    print(info.Email)
    print(info.marks)

print_data(info_obj)


