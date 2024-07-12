import sys

n = int(sys.stdin.readline())

# brut force

if n <= 1 :
    print("Not Prime")
else:
    i = 2
    is_prime = True
    while i * i <= n :
        if n % i == 0 :
            is_prime = False
            break
        i += 1

    if is_prime:
        print("Prime")

    else:
        print("Not Prime")
