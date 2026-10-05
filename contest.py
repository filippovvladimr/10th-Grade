a, b, c, d = map(int, input().split())

ans = max(min(a, b), min(c, d))

ans = max(ans, min(a, c, b + d))
ans = max(ans, min(a, d, b + c))
ans = max(ans, min(b, c, a + d))
ans = max(ans, min(b, d, a + c))

print(ans)

r"""
    #include <iostream>
    #include <algorithm>
    using namespace std;

    int main() {
        long long a, b, c, d;
        cin >> a >> b >> c >> d;
// Квадрат целиком внутри одного из прямоугольников
    long long ans = max(min(a, b), min(c, d));

    // Склеиваем стороны a и c
    ans = max(ans, min({a, c, b + d}));

    // Склеиваем стороны a и d
    ans = max(ans, min({a, d, b + c}));

    // Склеиваем стороны b и c
    ans = max(ans, min({b, c, a + d}));

    // Склеиваем стороны b и d
    ans = max(ans, min({b, d, a + c}));

    cout << ans;

    return 0;
}
"""
