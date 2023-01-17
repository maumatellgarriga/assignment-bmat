from fastapi import FastAPI
import pandas as pd
import sqlite3
from fuzzywuzzy import fuzz
from databases import Database

app = FastAPI()

# database = Database("sqlite:///db.db")

# @app.on_event("startup")
# async def database_connect():
#     await database.connect()


# @app.on_event("shutdown")
# async def database_disconnect():
#     await database.disconnect()


# def get_sr_metadata(sr_id: str):
#     query = f"SELECT * from soundrecording WHERE sr_id = {sr_id}"
#     results = database.fetch_all(query=query)
#     return results #pd.read_sql_query(f"SELECT * from soundrecording WHERE sr_id = {sr_id}", database).set_index("id")

# def compute_features(q_sr_id, m_sr_id):
#     def conicidence(word1, word2):
#         if word1 == word2:
#             return 1
#         return 0
#     ds = get_sr_metadata(q_sr_id).join(get_sr_metadata(m_sr_id))
#     ds["title_sim"] = ds.apply(lambda x: fuzz.ratio(x.q_title, x.m_title), axis=1)
#     ds["artists_sim"] = ds.apply(lambda x: fuzz.ratio(x.q_artists, x.m_artists), axis=1)
#     ds["contributors_sim"] = ds.apply(lambda x: fuzz.ratio(x.q_contributors, x.m_contributors), axis=1)
#     ds["isrcs_coincidence"] = ds.apply(lambda x: conicidence(x.q_isrcs, x.m_isrcs), axis=1)
#     return ds

# def predict(ds):
#     return 0

@app.get('/?q_sr_id={q_sr_id}&m_sr_id={m_sr_id}')
def base(q_sr_id, m_sr_id):
    return {f"{q_sr_id}": m_sr_id}
    #return get_sr_metadata("spotify_apidsr__2NbYAPqE6FTyQte9kW4vgr")