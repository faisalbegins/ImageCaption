if __name__ == '__main__':
    import sys
    import image_caption_library as mllib
    from keras.models import load_model
    # prepare tokenizer on train set

    # load training dataset (6K)
    filename = sys.argv[1]  # 'Flickr8k_text/Flickr_8k.trainImages.txt'
    train = mllib.load_set(filename)
    print('Dataset: %d' % len(train))
    # descriptions
    train_descriptions = mllib.load_clean_descriptions('descriptions.txt', train)
    print('Descriptions: train=%d' % len(train_descriptions))
    # prepare tokenizer
    tokenizer = mllib.create_tokenizer(train_descriptions)
    vocab_size = len(tokenizer.word_index) + 1
    print('Vocabulary Size: %d' % vocab_size)
    # determine the maximum sequence length
    max_length = mllib.calculate_max_length(train_descriptions)
    print('Description Length: %d' % max_length)

    # prepare test set

    # load test set
    filename = sys.argv[2]  # 'Flickr8k_text/Flickr_8k.testImages.txt'
    test = mllib.load_set(filename)
    print('Dataset: %d' % len(test))
    # descriptions
    test_descriptions = mllib.load_clean_descriptions('descriptions.txt', test)
    print('Descriptions: test=%d' % len(test_descriptions))
    # photo features
    test_features = mllib.load_photo_features('features.pkl', test)
    print('Photos: test=%d' % len(test_features))

    # load the model
    filename = 'model-ep002-loss3.245-val_loss3.612.h5'
    model = load_model(filename)
    # evaluate model
    mllib.evaluate_model(model, test_descriptions, test_features, tokenizer, max_length)
