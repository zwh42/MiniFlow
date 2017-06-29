#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mini Flow

@author: zhaowenhao
"""

class Neuron(object):
    def __init__(self, inbound_neurons = []):
        self.inbound_neurons = inbound_neurons
        self.outbound_neurons = []
        
        for neuron in self.inbound_neurons:
            neuron.outbound_neurons.append(self)
            self.value = None
            
    def forward(self):
        raise NotImplemented
        

class Input(Neuron):
    def __init__(self):
        Neuron.__init__(self)
    
    def forward(self, value = None):
        if value is not None:
            self.value = value
    

class Add(Neuron):
    def __init__(self, *input_tuple):
        Neuron.__init__(self, list(input_tuple))
        self.value = 0.
    
    def forward(self):
        for neuron in self.inbound_neurons:
            self.value = self.value + neuron.value
            
class Linear(Neuron):
    def __init__(self, inputs, weights, bias):
        Neuron.__init__(self, [inputs, weights, bias])
        self.value = 0.
        
    def forward(self):        
        for input_value, weight in zip(self.inbound_neurons[0].value, self.inbound_neurons[1].value):
            self.value += input_value * weight 
        self.value +=  self.inbound_neurons[2].value   
            
def topological_sort(feed_dict):
    """
    Sort generic nodes in topological order using Kahn's Algorithm.

    `feed_dict`: A dictionary where the key is a `Input` node and the value is the respective value feed to that node.

    Returns a list of sorted nodes.
    """

    input_neurons = [n for n in feed_dict.keys()]

    G = {}
    neurons = [n for n in input_neurons]
    while len(neurons) > 0:
        n = neurons.pop(0)
        if n not in G:
            G[n] = {'in': set(), 'out': set()}
        for m in n.outbound_neurons:
            if m not in G:
                G[m] = {'in': set(), 'out': set()}
            G[n]['out'].add(m)
            G[m]['in'].add(n)
            neurons.append(m)

    L = []
    S = set(input_neurons)
    while len(S) > 0:
        n = S.pop()

        if isinstance(n, Input):
            n.value = feed_dict[n]

        L.append(n)
        for m in n.outbound_neurons:
            G[n]['out'].remove(m)
            G[m]['in'].remove(n)
            # if no other incoming edges add to S
            if len(G[m]['in']) == 0:
                S.add(m)
    return L


def forward_pass(output_neuron, sorted_neurons):
    """
    Performs a forward pass through a list of sorted neurons.

    Arguments:

        `output_neuron`: A neuron in the graph, should be the output neuron (have no outgoing edges).
        `sorted_neurons`: a topologically sorted list of neurons.

    Returns the output neuron's value
    """

    for n in sorted_neurons:
        n.forward()

    return output_neuron.value            
        

