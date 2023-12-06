import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Inputs(BaseModel):
        inp : int
        inp2 : str

@app.get("/exemplo")
def exemple() -> str:
    return "ola mundo "

@app.post("/exemplo_2")
def exemple_2(inputs:Inputs) -> str:
     return inputs.inp2

if __name__ == "__main__":
    uvicorn.run(app, port=8000)

http://localhost:8000/exemplo GET
http://localhost:8000/exemplo_2 POST
