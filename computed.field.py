from pydantic import BaseModel, computed_field
class Speed(BaseModel):
    distance: float # km
    time: float # hours
    @computed_field
    @property
    def Speed(value) -> float: # it will return the value in float. jo function ka nam, wahi attribute ka nam hoga. 
        return (value.distance/value.time)

data={
    'distance': 600.4,
    'time': 10
}

print(Speed(**data))