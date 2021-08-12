def initialize(app):
    import pickle
    import constants as const
    from keras.models import load_model

    # load tokenizer
    with open(const.TOKENIZER_FILE, 'rb') as tokenizer_file:
        app.tokenizer = pickle.load(tokenizer_file)

    # load caption generator model
    app.model = load_model(const.MODEL_FILE)

    # load pre trained vgg16 model & re-structure the model
    from keras.models import Model
    from keras.applications.vgg16 import VGG16
    model = VGG16()
    model = Model(inputs=model.inputs, outputs=model.layers[-2].output)

    # hack around: forcing keras to download vgg16 weight during initialization
    import caption_generator as generator
    generator.extract_features(model, const.UPLOAD_DIR + "/init_image")

    app.pre_trained_model = model
