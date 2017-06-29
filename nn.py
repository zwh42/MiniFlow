#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 23:53:57 2017

@author: zhaowenhao
"""

from Neuron import *

# add
w, x, y, z = Input(), Input(), Input(), Input()

f = Add(x, y, z, w)
feed_dict = {x: 10, y: 5, z: 6, w: 21}

sorted_neurons = topological_sort(feed_dict)
output = forward_pass(f, sorted_neurons)
output_string = ""
for key in feed_dict.keys():
    output_string = output_string + str(feed_dict[key]) + " + "

output_string = output_string[:-2] + " = " + str(output) + " (according to miniflow.)"
print(output_string)


#Linear
inputs, weights, bias = Input(), Input(), Input()

f = Linear(inputs, weights, bias)

feed_dict = {
    inputs: [6, 14, 3],
    weights: [0.5, 0.25, 1.4],
    bias: 2
}

graph = topological_sort(feed_dict)
output = forward_pass(f, graph)

print(output) # should be 12.7 with this example

    