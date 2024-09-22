# m = 10**9 + 7

# addition
# (a+b) mod 7
import sys

a,b = list(map(int, sys.stdin.readline().split()))
print("addition")
print((a+b)%7)
print(((a%7)+(b%7))%7)

print("multiplication")

print((a*b)%7)
print(((a%7)*(b%7))%7)

print("sub")

print((a-b)%7)
print(((a%7)-(b%7))%7)
print(((a%7)-(b%7) + 7)%7)



