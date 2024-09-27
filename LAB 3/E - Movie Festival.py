import sys

t = int(sys.stdin.readline())

movies = {}

while t > 0 :

    movie = sys.stdin.readline().strip()
    ts = movie
    s,e = map(int,movie.split())
    movies[movie] = e - s
    # movies[s] = e - s
    t -= 1
# print(movies)

new = dict(sorted(movies.items(), key=lambda item : item[1]))

# print(new)
busy = 0
count = 0

for k,v in new.items() :
    s, e = map(int, k.split())
    if s >= busy :
        busy = e
        count += 1

print(count)