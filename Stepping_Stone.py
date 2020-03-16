#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:41:53 2020

@author: paul
"""

from pylab import *
import numpy

N=20            # Number of squares=N*N

boundary=N              # failed at boundary==2 !!!
div=8
figure (figsize=(boundary/div,boundary/div))      # pure aesthetics! div by 9 0r 8

#colors=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
colors=['k','w']        # Black n White!

state_vector=numpy.array(empty([N*N,2]))
state_color=numpy.array(empty([N*N],dtype=str))

ctr=0
for i in range(0,N):
    for j in range(0,N):
        c=numpy.random.choice(colors)
        line=plot(i,j,c+'s')      # '_s': square markers
        state_vector[ctr,0]=i
        state_vector[ctr,1]=j
        state_color[ctr]=c
        ctr+=1
              
draw()       
savefig("/home/paul/Documents/Output_Stones/Intial_State.png",dpi=400)



