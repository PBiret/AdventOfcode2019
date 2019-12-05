

def round3(module):
    return (module//3 - 2)

def sum_list(liste_txt):
    res = 0
    for k in liste_txt:
        res += round3(int(k))
    return res

print(round3(100756))

file = open("./1/input_puzzle1.txt","r")
input = file.readlines()

print(sum_list(input))