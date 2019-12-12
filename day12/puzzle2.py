import itertools

input_file = open("C:/Users/Pierre/Documents/AdventCode2019/inputs/day12.txt", "r")
input_pos_temp = input_file.read().splitlines()

steps_pos_x = []
steps_pos_y = []
steps_pos_z = []
steps_vel_x = []
steps_vel_y = []
steps_vel_z = []
periods = [0 for _ in range(6)]

positions = [[0,0,0] for _ in range(4)]

for k,object_jupiter in enumerate(input_pos_temp):
    temp_positions = object_jupiter[1:-1]
    temp_positions = temp_positions.split(",")
    temp_positions = list(map(lambda x : x.split("=") , temp_positions))
    positions[k] = [int(temp_positions[0][1]),int(temp_positions[1][1]),int(temp_positions[2][1])]

velocities = [[0,0,0] for _ in range(4)]
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

for k in range(NB_STEPS):        
    steps_vel_x += [velocities[0].copy()]
    steps_vel_y += [velocities[1].copy()]
    steps_vel_z += [velocities[2].copy()]    
    steps_pos_x += [positions[0].copy()]
    steps_pos_y += [positions[1].copy()]
    steps_pos_z += [positions[2].copy()]

    apply_gravity(positions, velocities)
    apply_velocity(positions,velocities)

    if velocities[0] in steps_vel_x[-1]:
        print(k)
        if periods[0]==0:
            periods[0] = k
    if velocities[1] in steps_vel_y[-1]:
        print(k)
        if periods[1]==0:
            periods[1] = k
    if velocities[2] in steps_vel_z[-1]:
        print(k)
        if periods[2]==0:
            periods[2] = k
    if positions[0] in steps_pos_x[-1]:
        print(k)
        if periods[3]==0:
            periods[3] = k
    if positions[1] in steps_pos_y[-1]:
        print(k)
        if periods[4]==0:
            periods[4] = k
    if positions[2] in steps_pos_z[-1]:
        print(k)
        if periods[5]==0:
            periods[5] = k
    print(k)
    print(periods)

print(positions,velocities)
print(energy(positions,velocities))