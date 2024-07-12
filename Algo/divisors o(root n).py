import sys

n = int(sys.stdin.readline())


s = []
i = 1
while i*i <= n :
    if n % i == 0:
        s.append(i)
        if n / i != i:
            s.append(n//i)

    i += 1
s.sort()
print(s)