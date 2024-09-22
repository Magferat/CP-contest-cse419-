# https://codeforces.com/problemset/problem/214/A
# problem: 4
import math
n,m = [int(i) for i in input().split()]
a = [i for i in range(int(math.sqrt(n))+1)]
b = [i for i in range(int(math.sqrt(m))+1)]

pair = 0
if n>m:

    j = len(b)-1
    while j>= 0:

        comp = m - b[j]**2
        if comp**2 <= n:
            if comp**2 + b[j] == n:
                pair += 1
        j -= 1
else:
    j = len(a) -1
    while j>= 0:
        comp = n - a[j]**2
        if comp ** 2 <= m:
            if comp**2 + a[j] == m:
                pair += 1
        j -= 1
print(pair)
