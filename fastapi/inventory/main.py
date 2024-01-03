from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Gilberto","numeros":[1,2,3,4,5]}
