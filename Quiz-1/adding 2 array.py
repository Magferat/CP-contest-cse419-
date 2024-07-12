a = [1,6,8,10]

b = [2,3,7]

# c = a+b
# c.sort()
# print(c)
new = []

if len(a) < len(b) :
    i, j = 0, 0
    while i < len(a):

        if a[i] < b[j]:
            new += [a[i]]
            i += 1
        elif a[i] > b[j]:
            new += [b[j]]
            j += 1
        else:
            new += [a[i]]
            new += [b[j]]
            i += 1
            j += 1
    new += b[j::]

else:
    i, j = 0, 0
    while j < len(b):

        if a[i] < b[j]:
            new += [a[i]]
            i += 1
        elif a[i] > b[j]:
            new += [b[j]]
            j += 1
        else:
            new += [a[i]]
            new += [b[j]]
            i += 1
            j += 1
    new += a[i::]
print(new)
