import sys

t = int(sys.stdin.readline())

while t > 0 :

    sig = sys.stdin.readline().strip()
    count = [0,0]
    for s in sig :
        if s == '1':
            count[1] += 1
        else:
            count[0] += 1
    pair = min(count)
    if pair % 2 == 0 :
        sys.stdout.write("NET\n")
    else:
        sys.stdout.write("DA\n")

    t -= 1