import sys

t = int(sys.stdin.readline())
m = 1000000007

def f(n,m) :
    if n == 0 : return 0
    elif n == 1 : return 1
    else:
        n_1 = f(n-1,m) % m
        n_2 = f(n - 2, m) % m
        s = ( n_1 + n_2 ) % m
        return s

print(f(t,m))