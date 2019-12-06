import numpy

file = open("C:/Users/Pierre/Documents/AdventCode2019/inputs/day6.txt","r")
input = file.read().splitlines()
def list_planets(input):
    planets_list=[]
    for orbit in input:
        planets=orbit.split(")")
        for planet in planets:
            if not(planet in planets_list):
                planets_list += [planet]
    return planets_list

def list_orbits(input):

    planets_list = list_planets(input)
    orbits_list = [[] for _ in range(len(planets_list))]

    for orbit in input:
        planets=orbit.split(")")
        orbits_list[planets_list.index(planets[0])] += [planets[1]]
        # print(planets)

    return planets_list,orbits_list

def count_orbits(input):
    planets_list,orbits_list = list_orbits(input)
    orbits_count = [0]*len(planets_list)
    for k,orbiters in enumerate(orbits_list):
        orbits_count[k] = len(orbiters)
    return planets_list, orbits_list, orbits_count

def terminal_recursive(planets_list, orbits_list, planet, result):
    if orbits_list[planets_list.index(planet)]==[]:
        return result
    else:
        current_orbits = orbits_list[planets_list.index(planet)]
        new_result = result
        for k in range(len(current_orbits)):
            subplanet = current_orbits[k]
            # print(subplanet)
            new_result = 1 + terminal_recursive(planets_list, orbits_list, subplanet, new_result)
        return(new_result)



def count_all_orbits(input, planet):
    planets_list, orbits_list, _ = count_orbits(input)
    result = terminal_recursive(planets_list, orbits_list, planet, 0)
    return result

# print(list_orbits(input)[1])
# print(count_all_orbits(input, "C"))

result = 0
for planet in list_planets(input):
    result += count_all_orbits(input, planet)
print(result)