r"""
Петя пришел в госте к своей подруге Ане, которая живет в 2n-этажном доме на k-м
этаже. Кнопки этажа в лифте расположены в два столбца, в левом столбце от 1 до n снизу
вверх, а в правом столбце от n + 1 до 2n снизу вверх.
Петя — мальчик невысокого роста, ему всего 6 лет, поэтому он может дотянуться только
до нижних s кнопоквкаждомстолбце.Поэтому,еслионвойдетвлифтнапервомэтаже,он
может нажать одну из кнопок, до которых он может дотянуться, после чего, поднявшись
до некоторого этажа, Пете, возможно, придется пройти несколько пролетов вверх или вниз
по лестнице до k-го этажа.
Помогите Пете понять, сколько пролетов между этажами ему придется пройти по лест-
нице.
Формат входных данных
Первая строка ввода содержит число n (2 ⩽ n ⩽ 109).
Вторая строка ввода содержит число k (2 ⩽ k ⩽ 2n).
Третья строка ввода содержит число s (0 ⩽ s ⩽ n).
Формат выходных данных
Выведите одно число, минимальное число пролетов между этажами, которое Пете при-
дется пройти пешком по лестнице, чтобы попасть на необходимый этаж.
"""


def step_count():
    n = int(input())
    k = int(input())
    s = int(input())

    dist1 = 0
    dist2 = 0
    if s == 0:
        print(k - 1)
        return

    if k <= s:
        dist1 = 0
    else:
        dist1 = k - s


    if k < n + 1:
        dist2 = (n + 1) - k
    elif k <= n + s:
        dist2 = 0
    else:
        dist2 = k - (n + s)


    print(min(dist1, dist2))


# print(step_count())


def count_diff(str):
    k = len(str)
    count = 0
    while k > 0:
        for i in range(len(str) - k + 1):
            sub_str = str[i:i + k]

            for j in range(len(sub_str)):
                if sub_str[j] != sub_str[0]:
                    count += 1
                    break
        k += -1
    return count

print(count_diff("cool"))


def christmas_tree():
    n = int(input())
    max_width = 2 * n + 1

    for k in range(1, n + 1):
        for i in range(k + 1):
            stars_count = 2 * i + 1

            total_dots = max_width - stars_count
            left_dots = total_dots // 2
            right_dots = total_dots - left_dots

            print('.' * left_dots + '*' * stars_count + '.' * right_dots)

# christmas_tree()


