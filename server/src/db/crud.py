import time
from uuid import uuid4

from src.db.common import DAO
from src.db.models import Records


def save_voice(voice_path: str, machine_id: str):
    dao = DAO()
    record_id = str(uuid4())
    with dao.new_session() as session:
        new_instance = Records(
            id=record_id,
            audio_path=voice_path,
            inference_at=None,
            text=None,
            machine_id=machine_id,
            voice_id=str(uuid4()),
            recorded_at=time.time()
        )
        session.add(new_instance)
        session.commit()
    return record_id
