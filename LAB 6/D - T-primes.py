
import sys


def run_seive() :

    i = 2

    while i < n:

        # if status[i] == True:
        #     facts[i].append(i)
            facts[i] += 1
            j = 2 * i
            while j < n:
                status[j] = False
                facts[j]+= 1
                j += i

            i += 1
    # return

t = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
n = max(arr) + 1
status = [True] * n
status[0] = status[1] = False
facts = {i: 1 for i in range(n)}
run_seive()
# print(facts)
# print(status)
for num in arr:
    if status[num] == True:
        sys.stdout.write("NO\n")
    else:
        if facts[num] == 3 :

            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")

#
# t = int(sys.stdin.readline())
#
# arr = list(map(int, sys.stdin.readline().split()))
#
# for num in arr:
#     if num == 1 :
#         sys.stdout.write("NO\n")
#     else:
#         k = num
#         fact = []
#         i = 2
#         while i * i <= num:
#             while num % i == 0:
#                 fact.append(i)
#                 num //= i
#             i += 1
#         if num > 1:
#                 fact.append(num)
#
#         f = set(fact)
#         f = list(f)
#         c = k
#         print(f)
#         for i in f :
#
#             a = 1-1/i
#             c *= a
#             # print(i,c, a)
#
#         print(f, c)












