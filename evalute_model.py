if __name__ == '__main__':
    import sys
    import image_caption_library as mllib
    from keras.models import load_model
    # prepare tokenizer on train set

    # load training dataset (6K)
    filename = '/Users/Faisal/Google Drive/imagecaption/Flickr8k_text/Flickr_8k.trainImages.txt'
    train = mllib.load_set(filename)
    print('Dataset: %d' % len(train))
    # descriptions
    train_descriptions = mllib.load_clean_descriptions('/Users/Faisal/Google Drive/imagecaption/descriptions.txt', train)
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
    filename = '/Users/Faisal/Google Drive/imagecaption/Flickr8k_text/Flickr_8k.testImages.txt'
    test = mllib.load_set(filename)
    print('Dataset: %d' % len(test))
    # descriptions
    test_descriptions = mllib.load_clean_descriptions('/Users/Faisal/Google Drive/imagecaption/descriptions.txt', test)
    print('Descriptions: test=%d' % len(test_descriptions))
    # photo features
    test_features = mllib.load_photo_features('/Users/Faisal/Google Drive/imagecaption/features.pkl', test)
    print('Photos: test=%d' % len(test_features))

    # load the model
    filename = '/Users/Faisal/Google Drive/imagecaption/trained_models/model_20epochs_final.h5'
    model = load_model(filename)
    # evaluate model
    mllib.evaluate_model(model, test_descriptions, test_features, tokenizer, max_length)
