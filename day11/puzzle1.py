import matplotlib.pyplot as plt

liste=[3,8,1005,8,315,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,29,2,1006,16,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,55,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,76,1,101,17,10,1006,0,3,2,1005,2,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,110,1,107,8,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,135,1,108,19,10,2,7,14,10,2,104,10,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,170,1,1003,12,10,1006,0,98,1006,0,6,1006,0,59,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,205,1,4,18,10,1006,0,53,1006,0,47,1006,0,86,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1001,8,0,239,2,9,12,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,266,1006,0,8,1,109,12,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,294,101,1,9,9,1007,9,1035,10,1005,10,15,99,109,637,104,0,104,1,21102,936995730328,1,1,21102,1,332,0,1105,1,436,21102,1,937109070740,1,21101,0,343,0,1106,0,436,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,1,179410308187,1,21101,0,390,0,1105,1,436,21101,0,29195603035,1,21102,1,401,0,1106,0,436,3,10,104,0,104,0,3,10,104,0,104,0,21102,825016079204,1,1,21102,1,424,0,1105,1,436,21102,1,825544672020,1,21102,435,1,0,1106,0,436,99,109,2,21202,-1,1,1,21102,1,40,2,21102,467,1,3,21101,0,457,0,1105,1,500,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,462,463,478,4,0,1001,462,1,462,108,4,462,10,1006,10,494,1102,0,1,462,109,-2,2106,0,0,0,109,4,1202,-1,1,499,1207,-3,0,10,1006,10,517,21102,1,0,-3,22101,0,-3,1,22101,0,-2,2,21101,1,0,3,21101,0,536,0,1106,0,541,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,564,2207,-4,-2,10,1006,10,564,21202,-4,1,-4,1105,1,632,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21101,583,0,0,1106,0,541,22102,1,1,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,602,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,624,21202,-1,1,1,21101,624,0,0,106,0,499,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

def op1(liste, arg1, arg2, arg3):
    liste[arg3] = liste[arg1] + liste[arg2]

def op2(liste, arg1, arg2, arg3):
    liste[arg3] = liste[arg1] * liste[arg2]

def op3(liste, arg1, input_number):
    liste[arg1] = input_number

def op4(liste, pos):
    return(liste[pos])

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

def memory(liste,input_number,index_input, relative_base_input):
    index = index_input
    relative_base = relative_base_input

    while True:

        if liste[index]==99:
            return -1,index,relative_base

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
            op3(liste,arg1,input_number)
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

index, relative_base = 0,0
liste = liste + [0 for _ in range(1000) ]
hull = [[" " for _ in range(100) ] for _ in range(100) ]
robot_position = [50,50]
hull[robot_position[0]][robot_position[1]] = "#"
robot_orientation = [0,-1]
current_output = 0

while(current_output != -1):

    if (hull[ robot_position[0] ][ robot_position[1] ] == " ") or (hull[ robot_position[0] ][ robot_position[1] ] == "."):
       current_output,index, relative_base = memory(liste, 0,index,relative_base)

    elif hull[ robot_position[0] ][ robot_position[1] ] == "#":
       current_output,index, relative_base = memory(liste, 1,index,relative_base)

    if current_output == 1:
        hull[robot_position[0]][robot_position[1]] = "#"
        print("white")

    elif current_output == 0:
        hull[robot_position[0]][robot_position[1]] = "."
        print("black")

    current_output,index, relative_base = memory(liste, 0,index,relative_base)

    robot_orientation = [robot_orientation[1]  * (1 - 2*current_output),robot_orientation[0]  * ( 2*current_output - 1) ]
    
    print(robot_position)
    robot_position = [ robot_position[0] + robot_orientation[0], robot_position[1] + robot_orientation[1] ]

counter = 0
for line in hull:
    counter += line.count("#") + line.count(".")
print(counter)

hull_image = [[0 for _ in range(100) ] for _ in range(100) ]
for k in range(len(hull)):
    for l in range(len(hull[0])):
        if hull[k][l] == " " or hull[k][l] == ".":
            hull_image[len(hull) - k - 1][l] = 0
        elif hull[k][l] == "#":
            hull_image[len(hull) - k - 1][l] = 1

plt.imshow(hull_image)
plt.show()