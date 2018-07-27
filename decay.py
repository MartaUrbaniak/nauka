#!/usr/bin/env python3
#-*- coding: utf-8 -*-


##########################

# Autor: Marta Urbaniak #
# Date: 21.05.18        #
# Version 1.0           #

# solving the           #
# radioactive decay     #
# equation              #
# using Euler metod     #

#########################


import pylab

a=[]
b=[]

class decay:
  
  def __init__ (self):
    print "The radioactive decay law is an universal law that describes the statistical behaviour of a large number of nuclides. "
    print "Variables wich are nedded to calculate this dependency are: t-time, dt- period of time, N_o- number of particles at the begining, k-decay constant "
    print "The solution is N, wich is the total number of particles in the sample after time -t."
    
    self.x=[]
    self.y=[]
  
  
  def solution(self, N_0, k, dt):
    
    for t in range(0,8,dt):
      
      N = N_0 + (-k*N_0) *dt
      N_0 = N
      
      #print "N= ",N
      
      self.x.append(t)
      self.y.append(N)
      
      
      
      
 
var=decay()
var.solution(10,0.3,1)

a=var.x
b=var.y

pylab.plot(a,b)
pylab.title('Radioactive decay N(t)')
pylab.xlabel('time [t]')
pylab.ylabel('N (t)')
pylab.savefig('decay.png')
pylab.show()


