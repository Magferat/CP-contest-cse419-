# https://codeforces.com/problemset/problem/233/A
# problem 4

n = int(input())
if n % 2 != 0:
    print(-1)
else:
    a = [int(i) for i in range(1,n+1)]
    i = 1
    while i<n+1:
        if i == a[i-1]:
            a[i-1],a[i] = a[i], a[i-1]
            i += 2

    print(*a, sep=' ')