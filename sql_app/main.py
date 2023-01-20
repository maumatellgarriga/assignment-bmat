from fastapi import FastAPI, Depends, HTTPException
import uvicorn
import crud, models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from classifier import Classifier

models.Base.metadata.create_all(bind=engine)

classifier_file_path = "model.pickle"

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

## tests

@app.get("/")
def base(q_sr_id: str, m_sr_id: str, db: Session = Depends(get_db)):
    sound_recording_q = crud.get_sound_recording(db=db, sr_id=q_sr_id)
    sound_recording_m = crud.get_sound_recording(db=db, sr_id=m_sr_id)
    if sound_recording_q.sr_id == None or sound_recording_m.sr_id==None:
        raise HTTPException(status_code=404, detail=f"Id {q_sr_id} or {m_sr_id} not found in db")
    classification = Classifier(sound_recording_q, sound_recording_m, classifier_file_path).get_prediction()
    return {"class": "valid" if classification==1 else "invalid"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002)