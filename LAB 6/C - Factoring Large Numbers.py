import sys

num = 100

while num != -1 :
    num = int(sys.stdin.readline())
    if num != 0 :
        i = 2
        while i * i <= num:
            while num % i == 0 :
                sys.stdout.write(f"    {i}\n")
                num //= i
            i += 1
        if num > 1 :
            sys.stdout.write(f"    {num}\n\n")

# 90
# 1234567891
# 18991325453139
# 12745267386521023
# -1

