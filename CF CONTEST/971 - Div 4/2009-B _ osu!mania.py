import sys

t = int(sys.stdin.readline())

while t > 0 :

    row = int(sys.stdin.readline())
    note = []
    while row > 0 :
        abc = list(sys.stdin.readline().strip())
        for i in range(4) :
            if abc[i] == "#" :
                note.append(i+1)
        row -= 1
    note.reverse()
    a = ' '.join(map(str, note))
    sys.stdout.write(a+"\n")

    t -= 1
