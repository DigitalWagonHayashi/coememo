import multiprocessing
import sys
import time
import whisper
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent.parent.parent))
from src.core.inference.modules.models import InferenceSession
from src.db.common import DAO, db_path
from src.db.models import Records


def inference():
    inference_session = InferenceSession("large")
    dao = DAO()
    while True:
        print('inference start')
        with dao.new_session() as session:
            no_inference = session.query(Records).where(Records.inference_at.is_(None)).all()
        if len(no_inference) == 0:
            time.sleep(1)
            continue
        for record in no_inference:
            # print(f"Start inference for record {record.id}")
            # audio_path = record.audio_path
            # inference_session.load_audio(audio_path)
            # result = inference_session.run()
            result = inference_session.transcribe(record.audio_path)
            with dao.new_session() as session:
                session.query(Records) \
                    .filter(Records.id == record.id) \
                    .update({"inference_at": time.time(), "text": result["text"]})
                session.commit()


if __name__ == '__main__':
    inference()
