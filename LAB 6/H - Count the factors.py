
import sys


def run_seive() :

    i = 2

    while i < n:

        if status[i] == True:
          # facts[i].append(i)
            facts[i] += 1
            j = 2 * i
            while j < n:
                status[j] = False
                facts[j] += 1
                j += i

        i += 1
    # return


n = 1000000
# n = 10
status = [True] * n
status[0] = status[1] = False
facts = {i: 0 for i in range(n)}

run_seive()
# print(facts)
# print(status)

t = -1

while t != 0 :

    t = int(sys.stdin.readline())
    if t > 0 :
        sys.stdout.write(f"{t} : {facts[t]}\n")

# 289384
# 930887
# 692778
# 636916
# 747794
# 238336
# 885387
# 760493
# 516650
# 641422
# 0
