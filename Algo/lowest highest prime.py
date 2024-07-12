import sys

n = int(sys.stdin.readline())

l = 1000000
prime_status = [True]*1000000
high, low = [0]*1000000, [0]*1000000
prime_status[0] = prime_status[1] = False
i = 2

while i < l :

    if prime_status[i] == True :
        high[i] = i
        low[i] = i
        j = i*2
        while j < l :
            prime_status[j] = False
            high[j] = i
            if low[j] == 0 :
                low[j] = i
            j += i
    i += 1

print(n,prime_status[n])
print(high[n], low[n])

hp = high[n]
factors = {}

while n > 1 :

    hp = high[n]

    while n % hp == 0:
        if hp in factors:
            factors[hp] += 1
        else:
            factors[hp] = 1
        n //= hp


print(factors)