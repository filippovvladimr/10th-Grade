def LZW(text):

    dictionary = {}
    index = 0

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


print(LZW("aboba"))




def LZW_decompress(codes, dictionary):
    d = {}

    for key in dictionary:
        if len(key) == 1:
            d[dictionary[key]] = key

    index = len(d) + 1
    current = d[codes[0]]
    result = current

    for code in codes[1:]:
        if code not in d:
            word = current + current[0]
        else:
            word = d[code]

        result += word
        d[index] = current + word[0]
        index += 1
        current = word

    return result


# print(LZW_decompress([1, 2, 3, 1], {'A': 1, 'B': 2}))