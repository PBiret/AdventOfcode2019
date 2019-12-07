import itertools

liste=[3,8,1001,8,10,8,105,1,0,0,21,34,47,72,81,94,175,256,337,418,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,2,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99]

def op1(liste, arg1, arg2, arg3):
    liste[arg3] = liste[arg1] + liste[arg2]

def op2(liste, arg1, arg2, arg3):
    liste[arg3] = liste[arg1] * liste[arg2]

def op3(liste, pos, input_number):
    liste[pos] = input_number

def op4(liste, pos, heap):
    return liste[pos]

def op5(liste, arg1):
    return bool(arg1)

def op6(liste, arg1):
    return not(bool(arg1))

def op7(liste, arg1, arg2, arg3):
        liste[arg3]=int(bool( liste[arg1] < liste[arg2] ))

def op8(liste, arg1, arg2, arg3):
        liste[arg3]=int(bool( liste[arg1] == liste[arg2] ))

def memory(liste, heap):
    index=0
    while True:

        if liste[index]%100==99:
            break

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
            arg3 = liste[index+3]


        if liste[index]%100==1:
            op1(liste, arg1, arg2, arg3)
            index+=4

        elif liste[index]%100==2:
            op2(liste, arg1, arg2, arg3)
            index+=4

        elif liste[index]%100==3:
            op3(liste, arg1, heap.pop())
            index+=2
            
        elif liste[index]%100==4:
            heap[-2] = op4(liste,arg1, heap)
            index+=2

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

        elif liste[index]%100==99:
            print(liste)
            break

        else:
            print("something went wrong\n")
            break


max_thrust = 0
for phase_sequence in list(itertools.permutations([0,1,2,3,4],5)):

    current_phase = list(phase_sequence)
    current_phase.reverse()
    heap = [0,0,0,0,0,0,0,0,0,0,0,0]
    heap[3:len(heap):2] = phase_sequence

    for k in range(5):
        input_list = liste.copy()
        memory(input_list, heap)

    max_thrust = max(max_thrust, heap[0])

print(max_thrust)