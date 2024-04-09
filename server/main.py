import uvicorn
import multiprocessing as mp

from src.db.common import db_path
from src.server.routes import app
from src.db.initialize import initialize
from src.core.inference.inference import inference


def main(host: str = "0.0.0.0", port: int = 5888):
    print(db_path)
    initialize()
    print("Initialized the database")
    inference_process = mp.Process(target=inference)
    inference_process.start()
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    import fire
    fire.Fire(main)
