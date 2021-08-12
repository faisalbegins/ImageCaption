import os
TOKENIZER_FILE = f'{os.environ.get("DATA_ROOT_DIR")}/tokenizer.pkl'
MODEL_FILE = f'{os.environ.get("DATA_ROOT_DIR")}/{os.environ.get("MODEL_FILE")}'
UPLOAD_DIR = f'{os.environ.get("UPLOAD_DIR")}'
MAX_SEQ_LENGTH = 34
