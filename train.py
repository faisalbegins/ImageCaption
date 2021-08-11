if __name__ == '__main__':
    import image_caption_library as mllib
    # load training dataset (6K)
    filename = '/Users/Faisal/Downloads/Flickr8k_text/Flickr_8k.trainImages.txt'
    train = mllib.load_set(filename)
    print('Dataset: %d' % len(train))
    # descriptions
    train_descriptions = mllib.load_clean_descriptions('/Users/Faisal/Downloads/descriptions.txt', train)
    print('Descriptions: train=%d' % len(train_descriptions))
    # photo features
    train_features = mllib.load_photo_features('/Users/Faisal/Downloads/features.pkl', train)
    print('Photos: train=%d' % len(train_features))
    # prepare tokenizer
    tokenizer = mllib.create_tokenizer(train_descriptions)
    vocab_size = len(tokenizer.word_index) + 1
    print('Vocabulary Size: %d' % vocab_size)
    # determine the maximum sequence length
    max_length = mllib.calculate_max_length(train_descriptions)
    print('Description Length: %d' % max_length)

    # define the model
    model = mllib.define_model(vocab_size, max_length)
    # train the model, run epochs manually and save after each epoch
    epochs = 20
    steps = len(train_descriptions)
    for i in range(epochs):
        # create the data generator
        generator = mllib.data_generator(train_descriptions, train_features, tokenizer, max_length, vocab_size)
        # fit for one epoch
        model.fit_generator(generator, epochs=1, steps_per_epoch=steps, verbose=1)
        # save model
        model.save('model_' + str(i) + '.h5')