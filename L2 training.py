def solve_qe(a, b, c):
    ### WRITE YOUR ANSWER BELOW
    delta=b**2-4*a*c
    ans1=(-b+(delta)**(0.5))/(2*a)
    ans2=(-b-(delta)**(0.5))/(2*a)
    if delta<0:
        return print("The equation has no real root")
    elif ans1>=ans2:
        return print('The two solutions are '+ str(ans1) +' and '+str(ans2))
    else: return 'The two solutions are '+str(ans2)+' and '+str(ans1)

solve_qe(3,9,6)

from math import sqrt
from random import uniform
def distance(x1, y1, x2, y2):
  dx, dy = x1-x2, y1-y2
  return sqrt((dx*dx) + (dy*dy))

def monte_carlo():
    ### WRITE YOUR CODE BELOW

    for i in range(100000):
        x, y=uniform(0,1),uniform(0,1)
        if distance(x,y,0,0)<=1:
            i=i+1
        return 4*i/100000

monte_carlo()