from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from crud import Database
from classifier import Classifier

classifier_file_path = "model.pickle"

app = FastAPI()

## tests

@app.get("/")
def get_classification(q_sr_id: str, m_sr_id: str):
    sound_recording_q = Database().get_sound_recording(sr_id=q_sr_id)
    sound_recording_m = Database().get_sound_recording(sr_id=m_sr_id)
    if sound_recording_q == None or sound_recording_m==None:
        raise HTTPException(status_code=404, detail=f"Id {q_sr_id} or {m_sr_id} not found in db")
    classification = Classifier(sound_recording_q, sound_recording_m, classifier_file_path).get_prediction()
    return {"class": "valid" if classification==1 else "invalid"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)