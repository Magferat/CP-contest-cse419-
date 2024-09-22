import sys

t =int(sys.stdin.readline())

while t > 0 :

    s = sys.stdin.readline().strip()
    if len(s) == 1 :
        sys.stdout.write("1\n")
    else :
        pos = {"0":[], "1":[]}
        for i in range(len(s)) :
            if s[i] == "0" :
                pos["0"].append(i)
            if s[i] == "1" :
                pos["1"].append(i)

        if len(pos["0"]) == len(pos["1"]) :
            sys.stdout.write("0\n")
        else:
            cost = 0
            if len(pos["0"]) > len(pos["1"]) :
                cost = len(pos["0"]) - len(pos["1"])
                cut = pos["0"][-cost]

                for i in pos['1']:
                    if i > cut:
                        cost += 1
            else:
                cost = len(pos["1"]) - len(pos["0"])
                cut = pos["1"][-cost]

                for i in pos['0']:
                    if i > cut :
                        cost += 1
            sys.stdout.write(str(cost)+"\n")





    t -= 1