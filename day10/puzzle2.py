import numpy as np

input_file = open("C:/Users/Pierre/Documents/AdventCode2019/inputs/day10.txt", "r")
input_map_temp = input_file.read().splitlines()
input_map = []
for line in input_map_temp:
    input_map += [list(line)]

def get_step(steps):
    if steps[0] == 0:
        return [0,steps[1]//abs(steps[1])]
    if steps[1] == 0:
        return [steps[0]//abs(steps[0]),0]

    abs_step = steps.copy()
    abs_step = list(map(abs, abs_step))

    a = max(abs_step)
    b = min(abs_step)

    factor = np.gcd(a,b)
    return [steps[0]//factor,steps[1]//factor]


def seeable_asteroids(input_map, indexes):
    seeable = []
    for i in range(len(input_map)):
        for j in range(len(input_map[0])):
            if input_map[i][j]=="#" and [i,j] != indexes:
                steps = get_step([ (i - indexes[0]) ,  (j - indexes[1]) ])

                temp_index = [i,j]

                while(temp_index != indexes):
                    
                    temp_index[0] -= steps[0]
                    temp_index[1] -= steps[1]

                    if temp_index == indexes: 
                        seeable += [[i,j]]
                        break

                    if input_map[temp_index[0]][temp_index[1]] == "#":
                        break
                        
                    
    angles = list(map(lambda coords : (np.angle(coords[1]-indexes[1] + (coords[0]-indexes[0])*1j, deg=True)+90)%360,seeable))


    seeable = list(zip(angles, seeable))

    return sorted(seeable)
    
max_index = [22, 17]

counter = 0
while (counter < 200):
    
    seeable = seeable_asteroids(input_map, max_index)

    for _,asteroid in seeable:
        if counter == 199:
            print(counter, asteroid[1] * 100 + asteroid[0])
        input_map[asteroid[0]][asteroid[1]] = "."
        counter += 1

    # print(counter)