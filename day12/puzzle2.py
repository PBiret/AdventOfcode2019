import itertools
import numpy as np

input_file = open("inputs/day12.txt", "r")
input_pos_temp = input_file.read().splitlines()

steps_x = []
steps_y = []
steps_z = []
periods=[0,0,0]

positions = [[0,0,0] for _ in range(4)]

for k,object_jupiter in enumerate(input_pos_temp):
    temp_positions = object_jupiter[1:-1]
    temp_positions = temp_positions.split(",")
    temp_positions = list(map(lambda x : x.split("=") , temp_positions))
    positions[k] = [int(temp_positions[0][1]),int(temp_positions[1][1]),int(temp_positions[2][1])]

velocities = [[0,0,0] for _ in range(4)]


init_x = [positions[0][0],positions[1][0],positions[2][0],positions[3][0],velocities[0][0],velocities[1][0],velocities[2][0],velocities[3][0]]
init_y = [positions[0][1],positions[1][1],positions[2][1],positions[3][1],velocities[0][1],velocities[1][1],velocities[2][1],velocities[3][1]]
init_z = [positions[0][2],positions[1][2],positions[2][2],positions[3][2],velocities[0][2],velocities[1][2],velocities[2][2],velocities[3][2]]

NB_STEPS = 500000000

def apply_gravity(positions, velocities):
    pairs = list(itertools.combinations(range(4), 2))
    for i,j in pairs:
        for k in range(3):
            if positions[i][k] > positions[j][k]:
                velocities[i][k] -=1
                velocities[j][k] +=1
            elif positions[i][k] < positions[j][k]:
                velocities[i][k] +=1
                velocities[j][k] -=1


def apply_velocity(positions, velocities):
    for k,vel in enumerate(velocities):
        for j in range(3):
            positions[k][j] += vel[j]

def energy(positions, velocities):
    ener = 0

    for k in range(4):   
        temp = [0,0]
        for i in range(3):
            temp[0] += abs(positions[k][i])
            temp[1] += abs(velocities[k][i])
        ener += temp[0]*temp[1]
    return ener

k = 0

while(0 in periods):

    k += 1

    apply_gravity(positions,velocities)
    apply_velocity(positions, velocities)

    if periods[0] == 0:
        steps_x += [[positions[0][0], positions[1][0],positions[2][0],positions[3][0],velocities[0][0], velocities[1][0],velocities[2][0],velocities[3][0]]].copy()
    if periods[1] == 0:
        steps_y += [[positions[0][1], positions[1][1],positions[2][1],positions[3][1],velocities[0][1], velocities[1][1],velocities[2][1],velocities[3][1]]].copy()
    if periods[2] == 0:
        steps_z += [[positions[0][2], positions[1][2],positions[2][2],positions[3][2],velocities[0][2], velocities[1][2],velocities[2][2],velocities[3][2]]].copy()

    if [positions[0][0], positions[1][0],positions[2][0],positions[3][0],velocities[0][0], velocities[1][0],velocities[2][0],velocities[3][0]] == init_x:
        if periods[0] == 0:
            periods[0] = k
            print(k, periods)

    if [positions[0][1], positions[1][1],positions[2][1],positions[3][1],velocities[0][1], velocities[1][1],velocities[2][1],velocities[3][1]] == init_y:
        if periods[1] == 0:
            periods[1] = k
            print(k, periods)

    if [positions[0][2], positions[1][2],positions[2][2],positions[3][2],velocities[0][2], velocities[1][2],velocities[2][2],velocities[3][2]] == init_z:
        if periods[2] == 0:
            periods[2] = k
            print(k, periods)


    

    # print(steps_x)


print(positions,velocities)
print(k)


      
print(np.lcm(np.lcm(periods[0],periods[1]), periods[2])) 
  