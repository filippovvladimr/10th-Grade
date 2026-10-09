def LZ78_compress(text):
    dictionary = {}
    result = []
    current = ""

    for char in text:
        if current + char in dictionary:
            current += char
        else:
            index = dictionary.get(current, 0)
            result.append((index, char))
            dictionary[current + char] = len(dictionary) + 1
            current = ""

    if current:
        result.append((dictionary[current], ""))

    return result

textik = "ABOBABOBOBA"
pairs = LZ78_compress(textik)
print(LZ78_compress(textik))


def LZ78_decompress(dictionary):
    dictionary = [""]
    result = ""

    for pair in pairs:
        index = pair[0]
        char = pair[1]

        current = dictionary[index] + char
        result += current

        if char:
            dictionary.append(current)

    return result


print(LZ78_decompress(pairs))