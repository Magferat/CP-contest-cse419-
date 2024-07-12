calories = [int(i) for i in input().strip().split()]

game = input()
s = 0
for i in game:

    s += calories[int(i)-1]
print(s)