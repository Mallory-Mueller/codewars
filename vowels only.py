def get_count(sentence):
    num = 0
    list = []
    length = len(sentence)
    list[:] = sentence
    # return length
    i = 0
    while length > 0:
        if list[i] == 'a':
            num += 1
            i += 1
            length -= 1
        else:
            i += 1
            length -= 1
    length = len(sentence)
    i = 0
    while length > 0:
        if list[i] == 'e':
            num += 1
            i += 1
            length -= 1
        else:
            i += 1
            length -= 1
    length = len(sentence)
    i = 0

    while length > 0:
        if list[i] == 'i':
            num += 1
            i += 1
            length -= 1
        else:
            i += 1
            length -= 1
    length = len(sentence)
    i = 0
    while length > 0:
        if list[i] == 'o':
            num += 1
            i += 1
            length -= 1
        else:
            i += 1
            length -= 1
    length = len(sentence)
    i = 0
    while length > 0:
        if list[i] == 'u':
            num += 1
            i += 1
            length -= 1
        else:
            i += 1
            length -= 1
    return num
