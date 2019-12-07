import itertools

liste = [3,8,1001,8,10,8,105,1,0,0,21,34,47,72,81,94,175,256,337,418,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,2,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99]

# liste=[3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

# liste = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
# -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
# 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

def op1(liste, arg1, arg2, arg3):
    liste[arg3] = liste[arg1] + liste[arg2]

def op2(liste, arg1, arg2, arg3):
    liste[arg3] = liste[arg1] * liste[arg2]

def op3(liste, pos, inputs):
    liste[pos] = inputs

def op4(liste, pos):
    return(liste[pos])

def op5(liste, arg1):
    return (liste[arg1] != 0)

def op6(liste, arg1):
    return liste[arg1]==0

def op7(liste, arg1, arg2, arg3):
        liste[arg3]=int(bool( liste[arg1] < liste[arg2] ))

def op8(liste, arg1, arg2, arg3):
        liste[arg3]=int(bool( liste[arg1] == liste[arg2] ))

def memory(liste, index_input, inputs):
    index=index_input
    while True:
        print(index)

        if liste[index]==99:
            return liste,-1,-1

        if (liste[index]%1000)//100>0:
            arg1 = index+1
        else:
            arg1 = liste[index+1]

        if (liste[index]%10000)//1000>0:
            arg2 = index+2
        else:
            arg2 = liste[index+2]

        if (liste[index])//10000>0:
            arg3 = index+3
        else:
            if index+3 < len(liste):
                arg3 = liste[index+3]
            else:
                arg3 = 0   


        if liste[index]%100==1:
            op1(liste, arg1, arg2, arg3)
            index+=4

        elif liste[index]%100==2:
            op2(liste, arg1, arg2, arg3)
            index+=4

        elif liste[index]%100==3:
            op3(liste, arg1, inputs.pop())
            index+=2
            
        elif liste[index]%100==4:
            index+=2
            return liste,op4(liste,arg1),index
            

        elif liste[index]%100==5:
            result = op5(liste,arg1)
            if result:
                index = liste[arg2]
            else:
                index+=3

        elif liste[index]%100==6:
            result = op6(liste,arg1)
            if result:
                index = liste[arg2]
            else:
                index+=3

        elif liste[index]%100==7:
            op7(liste,arg1,arg2,arg3)
            index+=4

        elif liste[index]%100==8:
            op8(liste,arg1,arg2,arg3)
            index+=4

        else:
            print("something went wrong\n")
            break


max_thrust=0

for phase in list(itertools.permutations([5,6,7,8,9],5)):

    temp_out=0
    indexes=[0 for _ in range(5)]
    lists_input = [liste.copy() for _ in range(5)]
    inputs=[[0]]+[[] for _ in range(4)]



    for k in range(5):
        print("Machine : " + str(k))
        lists_input[k],output,indexes[k]=memory(lists_input[k], indexes[k], inputs[k]+[phase[k]])
        inputs[(k+1)%5] = [output]

    while(True):
        if indexes == [-1]*5:

            break

        for k in range(5):
            if indexes == [-1]*5:
                break
            print("Machine : " + str(k))
            lists_input[k],output,indexes[k] = memory(lists_input[k], indexes[k], inputs[k])
            inputs[(k+1)%5] = [output]
            print(indexes)
            if inputs[0] != [-1]:
                temp_out=inputs[0]

    max_thrust = max(temp_out[0], max_thrust)

print(max_thrust)
