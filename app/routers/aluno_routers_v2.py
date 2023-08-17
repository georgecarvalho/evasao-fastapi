#Data Handling
import logging
import pickle
import numpy as np
import pandas as pd
from typing import List
from pydantic import BaseModel

# Server
import uvicorn
import gunicorn
from fastapi import APIRouter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#Classifier
from xgboost import XGBClassifier

# Initialize logging
my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.INFO, filename='sample.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

pipeline = pickle.load(open('./data/pipeline20230816.pkl','rb'))

class Aluno(BaseModel):
    campus:str
    curso:str
    modalidade: str 
    genero:str
    raca:str
    companhia_domiciliar:str
    mae_nivel_escolaridade:str
    pai_nivel_escolaridade:str
    estado_civil:str
    trabalha:str
    rendabruta:float
    idade:int
    anoingresso:int
    periodoingresso:int
    qtd_filhos:int

router = APIRouter(
    prefix="",
    tags=["aluno"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def verify_online_api():
    return "API ONLINE V2"

@router.post("/predict")
async def predict(data: Aluno):
    try:
        # Create and return prediction
        X_test = pd.DataFrame(data.dict(),index=[0])
        y_pred = pipeline.predict(X_test)
        return {"prediction": int(y_pred[0])}
    except:
        my_logger.error("Something went wrong!")
        return {"prediction": "error"}