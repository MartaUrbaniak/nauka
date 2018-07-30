#!/usr/bin/env python3
#-*- coding: utf-8 -*-


##########################

# Autor: Marta Urbaniak #
# Date: 28.07.18        #
# Version 1.0           #

# solving the           #
# radioactive decay     #
# equation              #
# using Runge-Kutta IV  #
# matod                 #
######################### 


import pylab

class function:
  
  def __init__ (self, k_init):
    
    #This function is using to calculete sequent steps in main function in decay class 
    
    self.k=k_init
  
  def f(self,n):
    return -(self.k*n)


class decay(function):
  
  def __init__(self,k_const):
    print "The radioactive decay law is an universal law that describes the statistical behaviour of a large number of nuclides. "
    print "Variables wich are nedded to calculate this dependency are: t-time, dt- period of time, N_o- number of particles at the begining, k-decay constant "
    print "The solution is N, wich is the total number of particles in the sample after time -t."
    
    print "In first step you should check the value of decay constant - wich is defferetn for various elements."
    
    function.__init__(self,k_const)
    
    self.x=[]
    self.y=[]

  
  def main(self, N_o, dt=0.5):
    
    for t in range(0,30):
      
      step_1=self.f(N_o)*dt
      step_2=self.f(N_o+0.5*step_1)*dt
      step_3=self.f(N_o+0.5*step_2)*dt
      step_4=self.f(N_o+step_3)*dt

      N=N_o+(step_1+2*step_2+2*step_3+step_4)/6

      N_o=N
      
      #print N
      
      self.x.append(t)
      self.y.append(N)


sol=decay(0.3)
sol.main(20)

pylab.plot(sol.x,sol.y)
pylab.title('Radioactive decay N(t)')
pylab.xlabel('time [t]')
pylab.ylabel('N (t)')
pylab.savefig('decay_Runge-Kutta_metod.png')
pylab.show()