typed = input()

target = ['h','e','l','l','o']

r = []
j = 0
for i in typed:
    if j < 5 and i == target[j]:
        r += [i]
        j += 1
if target == r:
    print('YES')
else:
    print("NO")