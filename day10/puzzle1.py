import numpy as np

input_file = open("C:/Users/Pierre/Documents/AdventCode2019/inputs/day10.txt", "r")
input_map_temp = input_file.read().splitlines()
input_map = []
for line in input_map_temp:
    input_map += [list(line)]
print(input_map)


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


def is_seeable_asteroids(input_map, indexes):
    counter = 0
    for i in range(len(input_map)):
        for j in range(len(input_map[0])):
            if input_map[i][j]=="#" and [i,j] != indexes:
                steps = get_step([ (i - indexes[0]) ,  (j - indexes[1]) ])

                temp_index = indexes.copy()

                while(temp_index != [i,j]):
                    
                    temp_index[0] += steps[0]
                    temp_index[1] += steps[1]

                    if temp_index == [i,j]: 
                        counter +=1
                        break

                    if input_map[temp_index[0]][temp_index[1]] == "#":
                        break
                        
                    
                
    return counter
    

max_counter = 0
max_index=[0,0]

for i in range(len(input_map)):
    for j in range(len(input_map[0])):
        if input_map[i][j] == "#":
            print(i,j)
            counter =  is_seeable_asteroids(input_map, [i,j])
            if max_counter < counter :
                max_index=[i,j]
                max_counter = counter

print(max_counter)
print(max_index)