import sys

t = int(sys.stdin.readline())

while t > 0 :

    digits = sys.stdin.readline()
    sum = int(digits[0]) + int(digits[1])
    sys.stdout.write(str(sum)+"\n")

    t -= 1