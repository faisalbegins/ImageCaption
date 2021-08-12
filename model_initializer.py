def initialize(app):
    import pickle
    import constants as const
    from keras.models import load_model

    with open(const.TOKENIZER_FILE, 'rb') as tokenizer_file:
        app.tokenizer = pickle.load(tokenizer_file)

    app.model = load_model(const.MODEL_FILE)
