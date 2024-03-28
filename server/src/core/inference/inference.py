import multiprocessing
import time
import whisper

from modules.models import InferenceSession
from src.db.common import DAO, db_path
from src.db.models import Records


def inference():
    inference_session = InferenceSession("large")
    dao = DAO(db_path)
    while True:
        with dao.get_session() as session:
            no_inference = session.query(Records).filter(Records.inference_at == None).all()
        if len(no_inference) == 0:
            time.sleep(1)
            continue
        for record in no_inference:
            audio_path = record.audio_path
            inference_session.load_audio(audio_path)
            result = inference_session.run()
            with dao.get_session() as session:
                session.query(Records) \
                    .filter(Records.id == record.id) \
                    .update({"inference_at": time.time(), "text": result.text})
