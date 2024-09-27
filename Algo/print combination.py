import sys

s = "abc"
all = []
def combo(s, new, idx) :

    if idx == len(s) :
        print(new)
        all.append(new)
        return
    combo(s, new+s[idx], idx+1)
    combo(s, new, idx+1)

combo(s,"", 0)

print(" ".join(all))
