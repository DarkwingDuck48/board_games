from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "hello World!"}


Very_big_str = '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
