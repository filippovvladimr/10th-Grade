r"""
in - входной поток
out - исходящий поток
search buffer - буфер поиска
look ahead buffer - буфер предпросмотра

    (смотрит в начало) sb| lab (сотрит на 4 вперед)

   a b a d a k a d a b r a --->  a| b a d a k a d a b r a ---> a b | a d a k a d a b r a

   offset | length | next
смещение   длинна    следущий
                                    abadabab
как делаем:                         search: abad
первый шаг:                         look-ahead: abab
<0 , 0, a>                          max substr - aba(превикс)
второй шаг:                         <4, 3, b>  b - первая после подстроки
<0, 0 ,b>

<2, 1 , d>
теперь a и b формально записаны и смешаемся на 2
<2, 1, k>
на 2
<4, 3, b>
<0, 0 ,r>
<0, 0, a>

Алгоритм Расшифровки
первая a потом b
смещаемся назад, смотри подстроку длииныы впсываем ему и добавляем бкуву

"""

#print(s[i:j])

encoded = [
    (0, 0, "a"),
    (0, 0, "b"),
    (2, 1, "d"),
    (2, 1, "k"),
    (4, 3, "b"),
    (0, 0, "r"),
    (0, 0, "a")
]
# def decode(encoded):
#     length = len(encoded)
#     resString = ""
#     for i in range(length):
#         char = resString[i-encoded[i][0] : i-encoded[i][0] + encoded[i][1]] + encoded[i][2]
#         resString += char
#     return resString
#
# print(decode(encoded))


def decode(encoded):
    result = ""

    for offset, length, next_char in encoded:
        if offset == 0 and length == 0:
            result += next_char
            continue

        bias = len(result) - offset


        for _ in range(length):
            result += result[bias]
            bias += 1

        result += next_char

    return result
print(decode(encoded))