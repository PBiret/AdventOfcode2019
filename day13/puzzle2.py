import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def op1(liste, arg1, arg2, arg3):
    liste[arg3] = liste[arg1] + liste[arg2]

def op2(liste, arg1, arg2, arg3):
    liste[arg3] = liste[arg1] * liste[arg2]

def op3(liste, arg1, joystick_pos):
    liste[arg1] = joystick_pos

def op4(liste, pos):
    return liste[pos]

def op5(liste, arg1):
    return (liste[arg1]!=0)

def op6(liste, arg1):
    return (liste[arg1]==0)

def op7(liste, arg1, arg2, arg3):
        liste[arg3]=int(bool( liste[arg1] < liste[arg2] ))

def op8(liste, arg1, arg2, arg3):
        liste[arg3]=int(bool( liste[arg1] == liste[arg2] ))

def op9(liste, arg1):
        return liste[arg1]

def memory(liste, index_input, relative_base_input ,joystick_pos):
    index=index_input
    relative_base=relative_base_input
    
    while True:

        if liste[index]==99:
            return -2,0,0

        if (liste[index]%1000)//100==1:
            arg1 = index+1
        elif (liste[index]%1000)//100==0:
            arg1 = liste[index+1]
        elif (liste[index]%1000)//100==2:
            arg1 = liste[index+1]+relative_base

        if (liste[index]%10000)//1000==1:
            arg2 = index+2
        elif (liste[index]%10000)//1000==0:
            try:
                arg2 = liste[index+2]
            except IndexError:
                arg2=index+2
        elif (liste[index]%10000)//1000==2:
            arg2 = liste[index+2]+relative_base

        if (liste[index])//10000==1:
            arg3 = index+3
        elif (liste[index])//10000==0:
            try:
                arg3 = liste[index+3]
            except IndexError:
                arg3=index+3
        elif (liste[index])//10000==2:
            arg3 = liste[index+3]+relative_base

        if liste[index]%100==1:
            op1(liste, arg1, arg2, arg3)
            index+=4

        elif liste[index]%100==2:
            op2(liste, arg1, arg2, arg3)
            index+=4

        elif liste[index]%100==3:
            op3(liste,arg1,joystick_pos)
            index+=2
            
        elif liste[index]%100==4:
            index+=2
            return op4(liste,arg1),index,relative_base

        elif liste[index]%100==5:
            if op5(liste,arg1):
                index = liste[arg2]
            else:
                index+=3

        elif liste[index]%100==6:
            if op6(liste,arg1):
                index = liste[arg2]
            else:
                index += 3

        elif liste[index]%100==7:
            op7(liste,arg1,arg2,arg3)
            index += 4

        elif liste[index]%100==8:
            op8(liste,arg1,arg2,arg3)
            index += 4

        elif liste[index]%100==9:
            relative_base += op9(liste,arg1)
            index += 2

        else:
            print("something went wrong\n")
            break

tile_id = 0

input_text_file = open("inputs/day13.txt", 'r')
input_text = input_text_file.read().splitlines()[0].split(",")
liste = list(map(lambda x : int(x), input_text))

liste = liste + [0]*1000
index_input,relative_base_input = 0,0
screen = [[0 for _ in range(200)] for _ in range(200)]

score = 0

def joystick_input(screen):
    x_ball = 0
    x_paddle = 0
    for line in screen:
        if 4 in line:
            x_ball = line.index(4)
        if 3 in line:
            x_paddle = line.index(3) 
    return np.sign(x_ball-x_paddle)

while tile_id != -2:

    joystick_pos = joystick_input(screen)
    print(joystick_pos)

    x,index_input,relative_base_input = memory(liste,index_input,relative_base_input,joystick_pos)
    y,index_input,relative_base_input = memory(liste,index_input,relative_base_input,joystick_pos)
    tile_id,index_input,relative_base_input = memory(liste,index_input,relative_base_input,joystick_pos)

    if x == -1 and y == 0:
        score = tile_id

    elif tile_id != -2 and x != -2 and y!= -2:
        screen[y][x] = tile_id

    else:
        break
    # print(x,y,tile_id)

plt.imshow(screen)
plt.show()

print(score)