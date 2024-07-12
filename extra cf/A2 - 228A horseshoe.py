import sys

colors = [int(i) for i in sys.stdin.readline().split()]


colors.sort()

s = 0

i = 1

while i < 4 :
    if colors[i] == colors[i-1]:
        s += 1
    i += 1

sys.stdout.write(str(s) + "\n")