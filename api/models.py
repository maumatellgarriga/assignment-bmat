from sqlalchemy import Column, String

from database import Base

class SoundRecording(Base):
    __tablename__ = "soundrecording"
    __table_args__ = {'extend_existing': True}

    id = Column(String, primary_key=True, index=True)
    sr_id = Column(String, index=True)
    title = Column(String)
    artists = Column(String)
    isrcs = Column(String)
    contributors = Column(String)