t = int(input().strip())
all_name = {}
while t > 0:
    name = input()

    if name not in all_name.keys():
        all_name[name] = 0
        print('OK')
    else:
        all_name[name] += 1
        print(f"{name}{all_name[name]}")

    t -= 1


