from sqlalchemy.orm import Session
from fastapi import HTTPException

import models

def get_sound_recording(db: Session, sr_id: str) -> models.SoundRecording:
    data = db.query(models.SoundRecording).filter(models.SoundRecording.sr_id == sr_id).scalar()
    return data