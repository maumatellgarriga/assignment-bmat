from fastapi import FastAPI

app = FastAPI()

@app.get("/?q_sr_id={q_sr_id}&m_sr_id={m_sr_id}")
async def read_item(item_id):
    return {"item_id": item_id}