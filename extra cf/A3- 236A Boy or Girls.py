import sys

name = sys.stdin.readline()

distinct = {}
num = 0
for ch in name :

    if ch not in distinct :
        distinct[ch] = num
        num += 1

if num % 2 == 0:
    sys.stdout.write("IGNORE HIM!")
else:
    sys.stdout.write("CHAT WITH HER!")