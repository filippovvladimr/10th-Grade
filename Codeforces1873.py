import math
import sys


c = int(input())
ans = []
for _ in range(c):
    str = input()
    if str == "bca": ans.append("no")
    elif str == "cab": ans.append("no")
    else: ans.append("yes")

for i in ans:
    print(i)

# TODO second

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    best = 0
    for i in range(n):

        b = a[:]
        b[i] += 1
        prod = math.prod(b)
        if prod > best:
            best = prod

    print(best)

# TODO third
def count(row , now):
    res = 0
    if(now == 0 or now == 9 ):
        for i in range(len(row)):
            if row[i] == "X":
                res = res + 1
            else:
                continue
    elif (now == 1 or now == 8):
        if row[0] == "X": res += 1
        if row[9] == "X": res += 1
        for i in range(1,9):
            if row[i] == "X":
                res += 2
    elif (now == 2 or now == 7):
        if row[0] == "X": res += 1
        if row[9] == "X": res += 1
        if row[8] == "X": res += 2
        if row[1] == "X": res += 2
        for i in range(2,8):
            if row[i] == "X":
                res += 3
    elif (now == 3 or now == 6):
        if row[0] == "X": res += 1
        if row[9] == "X": res += 1
        if row[8] == "X": res += 2
        if row[1] == "X": res += 2
        if row[2] == "X": res += 3
        if row[7] == "X": res += 3
        for i in range(3,7):
            if row[i] == "X":
                res += 4
    elif (now == 4 or now == 5):
        if row[0] == "X": res += 1
        if row[9] == "X": res += 1
        if row[8] == "X": res += 2
        if row[1] == "X": res += 2
        if row[2] == "X": res += 3
        if row[7] == "X": res += 3
        if row[3] == "X": res += 4
        if row[6] == "X": res += 4
        if row[4] == "X": res += 5
        if row[5] == "X": res += 5
    return res

resu = []

for i in range(int(input())):
    res = 0
    for j in range(10):
        res += count(input(), j)
    resu.append(res)

for num in resu:
    print(num)



#TODO fourth


def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        k = int(next(it))
        s = next(it)
        ans = 0
        i = 0
        while i < n:
            if s[i] == 'B':
                ans += 1
                i += k
            else:
                i += 1
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

solve()