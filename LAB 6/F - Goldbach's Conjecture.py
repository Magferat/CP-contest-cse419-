import sys


def run_seive() :

    i = 2
    p = []
    while i < n:
        p.append(i)
        if status[i] == True:
            j = 2 * i
            while j < n:
                status[j] = False
                j += i


        i += 1

# n = 1000000
n = 50
status = [True] * n
status[0] = status[1] = False
facts = {i: [] for i in range(n)}
run_seive()
print(True)

t = 100

while t != 0 :
    t = int(sys.stdin.readline())
    print(t)
    if t != 0 :
        # print(t)
        print(facts[t],t)

# 8
# 20
# 42
# 0
