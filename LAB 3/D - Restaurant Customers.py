import sys

t = int(sys.stdin.readline())
n = t
entry = []
leave = []
all = []
while t > 0:
    e, l = list(map(int, sys.stdin.readline().split()))
    entry.append(e)
    leave.append(l)
    all.append(e)
    all.append(l)
    t -= 1
entry.sort()
leave.sort()
all.sort()
# print(entry)
# print(leave)
# print(all)

e, l, c = 0,0, 0
guest = 0
max = 0
while c < 2*n :

    if e < n and entry[e] == all[c] :
        guest += 1
        e += 1
    elif l < n and leave[l] == all[c] :
        guest -= 1
        l += 1

    if guest > max :
        max = guest


    # print(all[c])
    c += 1


sys.stdout.write(str(max))


#
# finish = leave[-1]
# current = entry[0]
# guest = [0]* (leave[-1]+1)
#
# # print(finish,current,guest)
# e, l = 0,0
# max = 0
# while current <= finish:
#     guest[current] = guest[current - 1]
#     # print(current,e,l, guest)
#     if e < len(entry) and current == entry[e] :
#         guest[current] += 1
#         e += 1
#     if l < len(leave) and current == leave[l] :
#         guest[current]  -= 1
#         l += 1
#     if guest[current] > max :
#         max = guest[current]
#     current += 1
#
# # print(finish,current,guest)
# sys.stdout.write(str(max))


