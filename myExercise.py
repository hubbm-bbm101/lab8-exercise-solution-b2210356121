import sys

with open(sys.argv[1], "r", encoding="utf8") as f:

    dic = {}
    for i in f:
        i = i.split("\n")[0]
        n = (i.split(":"))[0]
        dic[n] = (i.split(":"))[1]

    for i in sys.argv[2].split(","):
        try:
            u = dic[i]
            print(f"Name: {i}, University: {u} ")

        except KeyError:
            print(f"No record of '{i}' was found!")



