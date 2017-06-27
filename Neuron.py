#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mini Flow

@author: zhaowenhao
"""

class Node(object):
    def __init__(self, inbound_nodes = []):
        self.inbound_nodes = inbound_nodes
        self.outbound_nodes = []
        
        for node in self.inbound_nodes:
            node.outbound_nodes.append(self)
            self.value = None
            
    def forward(self):
        raise NotImplemented
        

class Input(Node):
    def __init__(self):
        Node.__init__(self)
    
    def forward(self, value = None):
        if value is not None:
            self.value = value
    

class Add(Node):
    def __init__(self, x, y):
        Node.__init__(self, [x, y])
    
    def forward(self):
        for node in self.inbound_nodes:
            self.value = self.value + node.value
            
            
        

