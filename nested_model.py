from pydantic import BaseModel, EmailStr

class Address(BaseModel):
    street: str
    city: str
    zipcode: str


class User(BaseModel):
    name: str
    email: EmailStr
    age: int
    address: Address  # Nested model


user_data = {
    "name": "Shafqat Ullah",
    "email": "shfqt25@gmail.com",
    "age": 25,
    "address": {
        "street": "Street 5",
        "city": "Islamabad",
        "zipcode": "44000"
    }
}

user = User(**user_data)

user_dict = user.model_dump()
print("Dictionary:", user_dict)

user_json = user.model_dump_json() 
print("JSON:", user_json)
 # we can use include or exclude properties. 