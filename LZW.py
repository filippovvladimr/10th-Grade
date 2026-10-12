def LZW(text):

    dictionary = {}
    index = 1

    for char in text:
        if char not in dictionary:
            dictionary[char] = index
            index += 1

    result = []
    current = ""

    for char in text:
        if current + char in dictionary:
            current += char
        else:
            dictionary[current + char] = index
            result.append(dictionary[current])
            index += 1
            current = char

    if current:
        result.append(dictionary[current])

    return result, dictionary


print(LZW("свинья"))














