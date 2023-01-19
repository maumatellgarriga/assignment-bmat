from fastapi import FastAPI
from fuzzywuzzy import fuzz
import sqlite3
import pandas as pd
import numpy as np
import pickle

app = FastAPI()

model_file = "model.pickle"
model = pickle.load(open(model_file, "rb"))

@app.get("/")
def base(q_sr_id: str, m_sr_id: str):
    con = sqlite3.connect("db.db")
    q = pd.read_sql_query(f"SELECT * from soundrecording WHERE sr_id = '{q_sr_id}'", con).set_index("id")
    m = pd.read_sql_query(f"SELECT * from soundrecording WHERE sr_id = '{m_sr_id}'", con).set_index("id")
    
    def compute_word_similarity(ds1, ds2, column_name):
        return fuzz.ratio(ds1[column_name].to_list()[0], ds2.title.to_list()[0])
    def compute_conicidence(ds1, ds2, column_name):
        if ds1[column_name].to_list()[0] == ds2[column_name].to_list()[0]:
            return 1
        return 0
        
    title_sim = compute_word_similarity(q, m, "title")
    artists_sim = compute_word_similarity(q, m, "artists")
    contributors_sim = compute_word_similarity(q, m, "contributors")
    isrcs_coincidence = compute_conicidence(q, m, "isrcs")
    x_predict = [title_sim, artists_sim, contributors_sim, isrcs_coincidence]
    
    X_sample = np.array(x_predict).reshape(1,-1).tolist()
    pred = model.predict(X_sample).tolist()[0]
    result = {}
    result["class"] = "valid" if pred==1 else "invalid"
    return result
