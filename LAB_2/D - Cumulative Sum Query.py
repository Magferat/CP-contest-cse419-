n = int(input().strip())
arr = [int(i) for i in input().strip().split()]

t = int(input().strip())

while t > 0:
    start, end = [int(i) for i in input().split()]
    s = sum(arr[start:end+1])
    print(s)
    t -= 1