from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline
import uvicorn



app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


pipe = pipeline("text-classification", "dsbert")


class DM(BaseModel):
    data:str





@app.post("/pred")
async def create_item(dm: DM):
    sb = dm.data

    return pipe(sb)
    # return dm





@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')