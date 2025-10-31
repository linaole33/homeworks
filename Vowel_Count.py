def get_count(sentence):
    quantity = 0
    for char in sentence:
        if char == 'a':
            quantity = quantity + 1
        if char == 'e':
            quantity = quantity + 1
        if char == 'i':
            quantity = quantity + 1
        if char == 'o':
            quantity = quantity + 1
        if char == 'u':
            quantity = quantity + 1
    return quantity