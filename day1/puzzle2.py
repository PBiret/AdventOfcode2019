

def round3(module):
    if module<=0:
        return 0
    else:
        newfuel = (module//3 - 2)
        print(newfuel)
        return max(newfuel,0) + round3(newfuel)

def sum_list(liste_txt):
    res = 0
    for k in liste_txt:
        res += round3(int(k))
    return res

print(round3(100756))
# print(round3(14))
# print(round3(1969))


file = open("../inputs/day1.txt","r")
input = file.readlines()

print(sum_list(input))