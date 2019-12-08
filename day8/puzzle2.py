import numpy as np
import matplotlib.pyplot as plt

width = 25
height = 6

input_number_file = open("C:/Users/Pierre/Documents/AdventCode2019/inputs/day8.txt", "r")
input_number = input_number_file.readline()


def extract_layers(input_number, width, height):
    layers = []

    number_layers = len(input_number)//(width*height)

    for k in range(number_layers):
        new_layer = [[0] * width]*height

        for i in range(height):
            row = list(input_number[k*width*height + i*width:k*width*height + (i+1)*width])
            new_layer[i] = (list(map(lambda x : int(x),row)))
        layers += [new_layer]

    return layers


def count_numbers(layer, n):
    count = 0
    for row in layer:
        count += row.count(n)
    return count

layers = extract_layers(input_number, width, height)

image = [[2 for _ in range(width) ] for _ in range(height) ]

for layer in layers:
    for k in range(height):
        for l in range(width):
            if image[k][l]==2:
                image[k][l] = layer[k][l]

plt.imshow(image)
plt.show()

