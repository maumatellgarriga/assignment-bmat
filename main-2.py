from fastapi import FastAPI
from fuzzywuzzy import fuzz
import sqlite3
import pandas as pd
import numpy as np
import pickle

app = FastAPI()


@app.get("/")
def base(q_sr_id: str, m_sr_id: str): 
    con = sqlite3.connect("db.db")
    q = pd.read_sql_query(f"SELECT * from soundrecording WHERE sr_id = '{q_sr_id}'", con).set_index("id")
    m = pd.read_sql_query(f"SELECT * from soundrecording WHERE sr_id = '{m_sr_id}'", con).set_index("id")
    title_sim = fuzz.ratio(q.title.to_list()[0], m.title.to_list()[0])
    artists_sim = fuzz.ratio(q.artists.to_list()[0], m.artists.to_list()[0])
    contributors_sim = fuzz.ratio(q.contributors.to_list()[0], m.contributors.to_list()[0])
    isrcs_coincidence = fuzz.ratio(q.isrcs.to_list()[0], m.isrcs.to_list()[0])
    x_predict = [title_sim, artists_sim, contributors_sim, isrcs_coincidence]
    
    filename = "model.pickle"
    loaded_model = pickle.load(open(filename, "rb"))
    X_sample = np.array(x_predict).reshape(1,-1).tolist()
    pred = loaded_model.predict(X_sample).tolist()[0]
    result = {}
    result["class"] = "valid" if pred==1 else "invalid"
    return result
