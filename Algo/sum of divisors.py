# we need prime factorisation to find the sum of all divisors
import sys

n = int(sys.stdin.readline())
s = {}
i = 2
while i*i <= n :
     while n % i == 0:
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1
            n //= i
     i += 1

if n > 1 :
    s[n] = 1


print(s)
sum = 1
total_number_of_divisors = 1
for i in s:
    a = i ** (s[i] + 1) - 1
    b = a // (i-1)
    sum *= b
    total_number_of_divisors *= (s[i] + 1)

print(sum)
print(total_number_of_divisors)