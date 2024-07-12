import sys

arr = list(map(int, sys.stdin.readline().split()))

# 55 89 20 29 36 74 5 1 6 17 113
n = 10000000
prime_status = [True]*10000000

# print(prime_status)

prime_status[0] = prime_status[1] = False

i = 2

while i < n :

    if prime_status[i] == True :
        j = i*2
        while j < n :
            prime_status[j] = False
            j += i

    i += 1

for i in arr:
    print(i,prime_status[i])


