import sys

t = int(sys.stdin.readline())

enter = []
leave = []

while t > 0:
    e, l = list(map(int, sys.stdin.readline().split()))
    enter.append(e)
    leave.append(l)
    t -= 1
t = len(enter)
enter.sort()
leave.sort()

# print(enter)
# print(leave)

all = ['N'] * (leave[-1] + 1)
# print(all)
all = {}
i = 0

while i < t:
    if enter[i] not in all:
        all[enter[i]] = ["E", 1]
    else :
        s, c = all[enter[i]][0], all[enter[i]][1]
        all[enter[i]] = [s,c]
    all[leave[i]] = 'L'
    i += 1

# print(all)

count = [0] * len(all)

j = 1

while j < len(all):

    c = count[j - 1]
    if all[j] == "E":
        c += 1
        count[j] = c

    elif all[j] == "L":
        c -= 1
        count[j] = c

    else:
        count[j] = c

    j += 1
count.sort()

sys.stdout.write(str(count[-1]) + "\n")