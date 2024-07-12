t = int(input().strip())

while t > 0:
    n, x = [int(i) for i in input().split()]
    stations = [int(i) for i in input().split()]
    gap = [stations[0]]
    gap += [stations[i+1] - stations[i] for i in range(len(stations)-1)]
    gap += [(x - stations[-1])*2]
    print(max(gap))
    t -= 1