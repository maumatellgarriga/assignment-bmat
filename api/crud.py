from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import SoundRecording
import models

models.Base.metadata.create_all(bind=engine)

class Database(object):
    def __init__(self) -> None:
       self.db = next(self.get_db())

    def get_db(self):
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def get_sound_recording(self, sr_id: str) -> SoundRecording:
        data = self.db.query(SoundRecording).filter(SoundRecording.sr_id == sr_id).scalar()
        return data