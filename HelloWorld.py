from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def HelloWorld():
    return {
    'message': 'Hello World'
}

@app.get("/about")
def about():
    return{ 'Introduction': 'My name is Shafqat Ullah. I am recently graduate in computer science. I am learning FastApi' }