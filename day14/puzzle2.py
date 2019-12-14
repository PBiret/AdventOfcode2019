input_text_file = open("inputs/day14.txt", 'r')
input_text = input_text_file.read().splitlines()
import math

reactions = {} # dict with product as key, and points to a tuple with the amount created and a list of tuples or amounts needed and chemicals
needed = {"ORE" : 0}
leftovers = {"ORE" : 0}

def extract_chemicals(reaction):
    new_reaction = reaction.split(" ")
    new_reaction.remove("=>")
    for k in range(len(new_reaction)):
        if k%2==0:
            new_reaction[k] = int(new_reaction[k])
        else:
            if new_reaction[k][-1]==",":
                new_reaction[k] = new_reaction[k][:-1]
    
    return new_reaction[-1],new_reaction[-2],[(new_reaction[k], new_reaction[k+1]) for k in range(0,len(new_reaction)-2,2)]
        


for reaction in input_text:
    extracted = extract_chemicals(reaction)
    reactions[extracted[0]] = (extracted[1], extracted[2])
    leftovers[extracted[0]] = 0
    needed[extracted[0]] = 0

no_needed = needed.copy()
no_leftovers = leftovers.copy()

def generate_needed(chemical, needed_chem):
    
    reaction = reactions[chemical]
    number_reactions = math.ceil(needed_chem/reaction[0])
    leftover_result = number_reactions * reaction[0] - needed_chem
    leftovers[chemical] += leftover_result

    needed[chemical] = 0
    for chemicals in reaction[1]:
        needed_chemicals = chemicals[0] * number_reactions
        needed[chemicals[1]] += max(0, needed_chemicals - leftovers[chemicals[1]] )
        leftovers[chemicals[1]] -= min(needed_chemicals, leftovers[chemicals[1]])

generate_needed("FUEL" , 1)

count_over = False
while(not count_over):
    count_over = True
    for chemical in needed:
        if chemical != "ORE":
            if needed[chemical] != 0:
                count_over = False
                generate_needed(chemical, needed[chemical])

print(needed["ORE"])


def dichotomy(a,b):


    global needed
    needed = no_needed.copy()
    global leftovers
    leftovers = no_leftovers.copy()

    generate_needed("FUEL" ,(a+b)//2)

    count_over = False
    while(not count_over):
        count_over = True
        for chemical in needed:
            if chemical != "ORE":
                if needed[chemical] != 0:
                    count_over = False
                    generate_needed(chemical, needed[chemical])

    temp_ab = needed["ORE"]
    if temp_ab > 1000000000000:
        return (a,(a+b)//2)
    else:
        return ( (a+b)//2 , b)

a=0
b=10000000

while b-a > 1:
    a,b = dichotomy(a,b)
    print(a,b)


needed = no_needed.copy()
leftovers = no_leftovers.copy()

generate_needed("FUEL" ,a)

count_over = False
while(not count_over):
    count_over = True
    for chemical in needed:
        if chemical != "ORE":
            if needed[chemical] != 0:
                count_over = False
                generate_needed(chemical, needed[chemical])

print(needed["ORE"])

generate_needed("FUEL" ,b)

count_over = False
while(not count_over):
    count_over = True
    for chemical in needed:
        if chemical != "ORE":
            if needed[chemical] != 0:
                count_over = False
                generate_needed(chemical, needed[chemical])

print(needed["ORE"])