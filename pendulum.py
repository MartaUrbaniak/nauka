#-*- coding: utf-8 -*-


##########################

# Autor: Marta Urbaniak #
# Date: 21.07.18        #
# Version 1.0           #

# solving the           #
# mathematical pendulum #
# equation              #

######################### 


import math
import pylab

X=[]
Y=[]

time_array=[]
Energy=[]
Potential_energy=[]
Kinetic_energy=[]


class pendulum():
  
  
  def __init__ (self, r_0, teta_0, omega_0=0, dt_0=0.01):
    
    print "With this program you can solve the matematical pendulum equation using the numerical metod"
    print "At begining it's necessary to choose the primary conditions."
    
    #primary conditions
    
    self.r=r_0
    self.omega=omega_0
    self.teta=teta_0
    self.dt=dt_0
    
    #arrays
    
    self.x=[]
    self.y=[]
    
    self.E=[]
    self.E_p=[]
    self.E_k=[]
    
    self.t=[]

  def calc(self):
    
    global g,m
    
    #constants
    g=9.8 
    m=1     
    
    #energy
    E_temp=0
    Ep_temp=0
    Ek_temp=0
    
    
    #value of angular veliocity and angle in first step
    omega_prim=self.omega+(g/self.r)*math.sin(self.teta)
    teta_prim=self.teta + omega_prim*self.dt
    
    
    for i in range(0,49):
      
      
      omega=omega_prim+(g/self.r)*math.sin(teta_prim) 
      teta=teta_prim+omega*self.dt
      
      
      #calculation of energy
      
      h=self.r+self.r*math.cos(teta_prim)
      #print "Height = ",h
    
      Ep_temp=m*g*h
      Ek_temp=(m*omega**2)/2
      
      #total energy
      E_temp=Ep_temp+Ek_temp
      
      
      omega_prim=omega
      teta_prim=teta
 
      
      self.x.append((self.r)*math.sin(teta))
      self.y.append((self.r)*math.cos(teta))
      
      self.E.append(E_temp)
      self.E_p.append(Ep_temp)
      self.E_k.append(Ek_temp)
      
      
      
  def time(self):
    
    #this function is needed to be call to draw the dependency energy from time on graph.
    
    t_temp=1
    
    for j in range(0,49):
      
      self.t.append(t_temp)
      
      t_temp+=1
      
      
    
    
    
sol=pendulum(10,1.53)
sol.calc()

X=sol.x
Y=sol.y

sol.time()
time_array=sol.t

Energy=sol.E
Potential_energy=sol.E_p
Kinetic_energy=sol.E_k

pylab.subplot(2,1,2)
l2,l3,l1=pylab.plot(time_array, Energy, 'r', time_array, Kinetic_energy, 'b', time_array, Potential_energy, 'g')
pylab.grid(True)
pylab.xlabel('time')
pylab.ylabel('Energy')
pylab.legend((l2,l3,l1),('Energy','Kinetic energy','Potential energy'))

pylab.subplot(2,1,1)
pylab.plot(X,Y)
pylab.title('mathematical pendulum')
pylab.grid(True)
pylab.xlabel('x')
pylab.ylabel('y')
pylab.show()