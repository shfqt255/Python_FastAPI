from pydantic import BaseModel
class info(BaseModel):
    name: str
    age: int
    regestration:int

def print_data(Info:info):
    print(Info.name)
    print(Info.age)
    print(Info.regestration)

given_info={
    'name': 'shafqat ullah',
    'age': 30,
    'regestration':25
}

info1=info(**given_info)
print_data(info1)
