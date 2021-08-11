if __name__ == '__main__':
    import sys
    from image_caption_library import load_doc, \
        load_descriptions, \
        clean_descriptions, \
        to_vocabulary, \
        save_descriptions

    filename = sys.argv[1]
    # load descriptions
    doc = load_doc(filename)
    # parse descriptions
    descriptions = load_descriptions(doc)
    print('Loaded: %d ' % len(descriptions))
    # clean descriptions
    clean_descriptions(descriptions)
    # summarize vocabulary
    vocabulary = to_vocabulary(descriptions)
    print('Vocabulary Size: %d' % len(vocabulary))
    # save to file
    save_descriptions(descriptions, 'descriptions.txt')
