import sys

k1,k2,k3,k4 = [int(i) for i in sys.stdin.readline().split()]

min_k = min(k1,k3,k4)

sum =  min_k * 256

k1 = k1 - min_k

min_k = min(k1,k2)

sum += min_k * 32

sys.stdout.write(str(sum)+ "\n")