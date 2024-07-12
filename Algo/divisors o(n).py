import sys

n = int(sys.stdin.readline())


s = []
i = 1
while i <= n :
    if n % i == 0 :
        s.append(str(i))
    i += 1

print(' '.join(s))