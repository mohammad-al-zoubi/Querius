import yaml
import json
import logging
from logging import getLogger
from pathlib import Path
from pydantic import BaseModel

from backend.QA import generate_chunk_log_embeddings

logger = getLogger(__name__)

logging.basicConfig(level=logging.INFO)


class GeneralConfig(BaseModel):
    embedding_model: str
    reranking_model: str


class AppConfig(BaseModel):
    general: GeneralConfig


def parse_config(yaml_config):
    # Parse the YAML
    with open(yaml_config, 'r') as yaml_file:
        config_dict = yaml.safe_load(yaml_file)

    # Create a Pydantic object
    app_config = AppConfig(**config_dict)
    return app_config


class LogQA:
    def __init__(self):
        self.data_dir = Path(r'backend/QA/data')
        self.config_path = self.data_dir / 'config.yaml'
        self.general_config = parse_config(self.config_path).general
        self.file_tracker = {}
        self.initialize_file_tracker()

    def initialize_file_tracker(self):
        path_to_file_tracker = self.data_dir / 'file_tracker.json'

        if path_to_file_tracker.is_file():
            try:
                with open(path_to_file_tracker, 'r', encoding='utf-8') as file:
                    self.file_tracker = json.load(file)
            except Exception as e:
                logger.error(f'Failed to load file tracker: {e}')
                logger.info('Initializing an empty file tracker...')
                with open(path_to_file_tracker, 'w', encoding='utf-8') as file:
                    json.dump(self.file_tracker, file, indent=4)
        else:
            with open(path_to_file_tracker, 'w', encoding='utf-8') as file:
                json.dump(self.file_tracker, file, indent=4)

    def update_file_tracker(self):
        path_to_file_tracker = self.data_dir / 'file_tracker.json'
        with open(path_to_file_tracker, 'w', encoding='utf-8') as file:
            json.dump(self.file_tracker, file, indent=4)

    def preprocess_logfile(self, path_to_logfile):
        """
        Preprocesses the log file to be used for similarity search.
        Args:
            path_to_logfile [str]: path to the log file

        Returns:
            None

        """
        path_to_logfile = Path(path_to_logfile)
        log_file_dir = self.data_dir / path_to_logfile.stem
        log_file_dir.mkdir(exist_ok=True)
        path_to_logfile_json = log_file_dir / f'{path_to_logfile.stem}.json'
        path_to_logfile_embeddings = log_file_dir / f'{path_to_logfile.stem}_embeddings.json'
        # generate_chunk_log_embeddings(path_to_logfile, path_to_logfile_json, path_to_logfile_embeddings)

        self.file_tracker[path_to_logfile.stem] = {
            'path_to_logfile': str(path_to_logfile),
            'path_to_logfile_json': str(path_to_logfile_json),
            'path_to_logfile_embeddings': str(path_to_logfile_embeddings),
        }
        self.update_file_tracker()


if __name__ == '__main__':
    log = LogQA()
    path = r"C:\Users\Mohammad.Al-zoubi\Documents\projects\Querius\backend\QA\data\test_log_1k.out"
    log.preprocess_logfile(path)
