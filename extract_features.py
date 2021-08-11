if __name__ == '__main__':
    import sys
    from pickle import dump
    from image_caption_library import extract_features
    # extract features from all images
    directory = sys.argv[1]
    features = extract_features(directory)
    print('Extracted Features: %d' % len(features))
    # save to file
    dump(features, open('features.pkl', 'wb'))
