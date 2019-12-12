import itertools

input_file = open("C:/Users/Pierre/Documents/AdventCode2019/inputs/day12.txt", "r")
input_pos_temp = input_file.read().splitlines()



positions = [[0,0,0] for _ in range(4)]

for k,object_jupiter in enumerate(input_pos_temp):
    temp_positions = object_jupiter[1:-1]
    temp_positions = temp_positions.split(",")
    temp_positions = list(map(lambda x : x.split("=") , temp_positions))
    positions[k] = [int(temp_positions[0][1]),int(temp_positions[1][1]),int(temp_positions[2][1])]

velocities = [[0,0,0] for _ in range(4)]
NB_STEPS = 1000

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

for _ in range(NB_STEPS):
    apply_gravity(positions, velocities)
    apply_velocity(positions,velocities)

print(positions,velocities)
print(energy(positions,velocities))