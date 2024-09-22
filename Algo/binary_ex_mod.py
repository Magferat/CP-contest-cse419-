# 58^345
m = 10 ** 9 + 7
ans = (58**345) % m
print(ans)

def binary_ex(a,p,m) :

    if p == 0 :
        return 1

    res = binary_ex(a, p//2, m)
    res = (res * res) % m
    if p % 2 != 0 :
        res *= a
        res %= m
    return res


print(binary_ex(58, 345,m))
import math
a = int(input())

c = 0

for i in range(a) :
    if math.gcd(i,a) == 1 :
        c += 1
print(c)
