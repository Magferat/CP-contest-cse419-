
# we know,
# A x B = GCD(A,B) x LCM(A,B)
# LCM = (A x B) // GCD(A<B)

import sys

a,b = list(map(int, sys.stdin.readline().split()))
# GCD
x,y = a,b
while a > 0 :
    t = a
    a = b % t 
    b = t
gcd = b
# LCM

lcm = (x*y) // gcd
print(x,y)
print(gcd, lcm)




