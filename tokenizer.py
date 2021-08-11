if __name__ == '__main__':
    from pickle import dump
    import image_caption_library as mllib
    # load training dataset (6K)
    filename = 'Flickr8k_text/Flickr_8k.trainImages.txt'
    train = mllib.load_set(filename)
    print('Dataset: %d' % len(train))
    # descriptions
    train_descriptions = mllib.load_clean_descriptions('descriptions.txt', train)
    print('Descriptions: train=%d' % len(train_descriptions))
    # prepare tokenizer
    tokenizer = mllib.create_tokenizer(train_descriptions)
    # save the tokenizer
    dump(tokenizer, open('tokenizer.pkl', 'wb'))