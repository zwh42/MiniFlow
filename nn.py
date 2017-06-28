#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 23:53:57 2017

@author: zhaowenhao
"""


from Neuron import *

w, x, y, z = Input(), Input(), Input(), Input()

f = Add(x, y, z, w)
feed_dict = {x: 10, y: 5, z: 6, w: 21}

sorted_neurons = topological_sort(feed_dict)
output = forward_pass(f, sorted_neurons)

# NOTE: because topological_sort set the values for the `Input` neurons we could also access
# the value for x with x.value (same goes for y).
#print("{} + {} = {} (according to miniflow)".format(feed_dict[x], feed_dict[y], output))

output_string = ""
for key in feed_dict.keys():
    output_string = output_string + str(feed_dict[key]) + " + "

output_string = output_string[:-2] + " = " + str(output) + " (according to miniflow.)"
print(output_string)


    