# main.py
import pandas as pd
from fastapi import FastAPI
from classify import classify
app = FastAPI()


@app.post("/classify/")
def classify_logs(logs: list):
    return {"labels": classify(logs)}
