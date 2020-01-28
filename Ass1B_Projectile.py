from math import sqrt, sin, pi
def initial_velocity(max_height, angle):
    velocity=sqrt(2*9.8*max_height)/sin(angle*pi/180)
    return velocity 

initial_velocity(10.204081632653063, 45)
initial_velocity(12.085714354185443, 20)
  
