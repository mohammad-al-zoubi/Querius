import yaml
import json
import logging
from logging import getLogger
from pathlib import Path
from pydantic import BaseModel

from backend.QA import generate_chunk_log_embeddings, load_embeddings, create_search_index, rerank_results

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

        # Current session parameters
        self.path_to_logfile = None
        self.path_to_logfile_json = None
        self.path_to_logfile_embeddings = None
        self.log_embeddings = None
        self.log_jsons = None
        self.index = None

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

    def preprocess_logfile(self, path_to_logfile: str):
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
        generate_chunk_log_embeddings(path_to_logfile, path_to_logfile_json, path_to_logfile_embeddings)

        self.file_tracker[str(path_to_logfile)] = {
            'path_to_logfile': str(path_to_logfile),
            'path_to_logfile_json': str(path_to_logfile_json),
            'path_to_logfile_embeddings': str(path_to_logfile_embeddings),
        }
        self.update_file_tracker()

    def log_search(self, file_path: str, query: str, top_n_lines: int) -> list:
        """
        Searches the log file for the query and returns the top k results.
        Args:
            file_path [str]: name of the log file
            query [str]: string query to search for
            top_k_lines [int]: number of lines to return
        """
        results = rerank_results(query, self.log_embeddings, self.log_jsons, self.index, top_n=top_n_lines)
        final_results = [{'logline': result.document['text'],
                          'id': result.document['id'],
                          'score': result.relevance_score} for result in results]
        return final_results

    def set_session_parameters(self, file_path):
        if file_path not in self.file_tracker:
            raise ValueError(f'File {file_path} not found in the database. Use the mthod preprocess_logfile() to add '
                             f'this file to the database.')
        file_path = str(Path(file_path))
        self.path_to_logfile = self.file_tracker[file_path]['path_to_logfile']
        self.path_to_logfile_json = self.file_tracker[file_path]['path_to_logfile_json']
        self.path_to_logfile_embeddings = self.file_tracker[file_path]['path_to_logfile_embeddings']

        self.log_embeddings = load_embeddings(self.path_to_logfile_embeddings, mode='list')
        self.log_jsons = load_embeddings(self.path_to_logfile_json, mode='json')
        self.index = create_search_index(self.log_embeddings)

    def get_log_line_by_id(self, line_id):
        """
        Returns the log line by its id.
        Args:
            line_id [int]: id of the log line

        Returns:
            log_line [str]: the log line
        """
        if self.log_jsons is None:
            raise ValueError('Session parameters not set. Use the method set_session_parameters() to set the '
                             'current logfile.')
        return self.log_jsons[line_id]['log_line']


def test():
    log = LogQA()
    path = r"/home/ubuntu/Querius/backend/QA/logs"
    log.preprocess_logfile(path)
    log.set_session_parameters(path)
    print(log.get_log_line_by_id(1000))
    log.log_search(path, 'When were the root privileges removed for user avahi?', 10)
