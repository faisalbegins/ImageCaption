def initialize(app):
    import constants as const
    import pickle
    with open(const.TOKENIZER_FILE, 'rb') as tokenizer_file, \
            open(const.MODEL_FILE, 'rb') as model_file:
        app.tokenizer = pickle.load(tokenizer_file)
        app.model = pickle.load(model_file)

