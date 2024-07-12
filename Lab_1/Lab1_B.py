t = int(input().strip())


while t > 0:

    word = input()
    r = word
    if len(word) > 10 :
        r = f"{word[0]}{len(word)-2}{word[-1]}"
    print(r)

    t -= 1