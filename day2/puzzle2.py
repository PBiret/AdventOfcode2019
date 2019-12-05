liste = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]
liste[1]=12
liste[2]=2

def op1(liste, pos1, pos2, pos3):
    liste[pos3] = liste[pos1] + liste[pos2]

def op2(liste, pos1, pos2, pos3):
    liste[pos3] = liste[pos1] * liste[pos2]

def check(liste, index):
    pos1, pos2, pos3 = liste[index+1], liste[index+2], liste[index+3]
    result = True
    result = result and (not (index+3 >= len(liste)))
    result = result and (not (index < 0))
    result = result and (not (pos1 > len(liste)))
    result = result and (not (pos2 > len(liste)))
    result = result and (not (pos3 > len(liste)))
    result = result and (not (pos1 < 0))
    result = result and (not (pos2 < 0))
    result = result and (not (pos3 < 0))
    return result

def memory(liste):
    index=0
    while True:
        if not(check(liste, index)):
            return(0)
        if liste[index]==1:
            op1(liste, liste[index+1], liste[index+2], liste[index+3])
        elif liste[index]==2:
            op2(liste, liste[index+1], liste[index+2], liste[index+3])
        elif liste[index]==99:
            return(liste[0])
        else:
            print("something wrent wrong\n")
            return(0)
        index+=4

print(memory(liste))

for i in range(100):
    for j in range(100):
        liste = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]
        liste[1]=i
        liste[2]=j

        if memory(liste) == 19690720:
            print(100*i+j)
            break