a, b, c, d = map(int, input().split())

ans = max(min(a, b), min(c, d))

ans = max(ans, min(a, c, b + d))
ans = max(ans, min(a, d, b + c))
ans = max(ans, min(b, c, a + d))
ans = max(ans, min(b, d, a + c))

print(ans)
