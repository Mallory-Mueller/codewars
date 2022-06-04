def spin_words(sentence):
    words = sentence.split(' ')
    new_words = [h[::-1] if len(h) >= 5 else h for h in words]
    return ' '.join(new_words)