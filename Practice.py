from math import sqrt

def critical_point_small(a, b, c, d):
    ### WRITE YOUR ANSWER BELOW
    #general form of differentiation: 3ax^2+2bx+c
    L=solve_qe_small (3*a,2*b,c)
    return L

def critical_point_large(a, b, c, d):
    ### WRITE YOUR ANSWER BELOW
    L=solve_qe_large (3*a,2*b,c)
    return L
    
def solve_qe_small (a,b,c):
    delta=b**2-4*a*c
    ans1=(-b+sqrt(delta))/(2*a)
    ans2=(-b-sqrt(delta))/(2*a)
    return ans2

def solve_qe_large (a,b,c):
    delta=b**2-4*a*c
    ans1=(-b+sqrt(delta))/(2*a)
    ans2=(-b-sqrt(delta))/(2*a)
    return ans1

critical_point_small(1, -2, -2, 1)

1 <= 10 == 5 > 5
1 > 10 != 5 <= 5
1<4<20
2<10>8
if <expression>:
    <statement(s) 1>
else:
    <statement(s) 2>

from math import sqrt
def solve_ce(a, b, c, d):
    ### WRITE YOUR ANSWER BELOW
    x=(-b**3/(27*a**3)+b*c/(6*a**2)-d/(2*a)+sqrt((-b**3/(27*a**3)+b*c/(6*a**2)-d/(2*a))**2+(c/(3*a)-b**2/(9*a**2))**3))**(1/3)
    +(-b**3/(27*a**3)+b*c/(6*a**2)-d/(2*a)-sqrt((-b**3/(27*a**3)+b*c/(6*a**2)-d/(2*a))**2+(c/(3*a)-b**2/(9*a**2))**3))**(1/3)
    -b/(3*a)
    return x
    
solve_ce(1, -3, -3, -2)

def solve_qe_large (a,b,c)
    delta=b**2-4*a*c
    ans1=(-b+sqrt(delta))/2*a
    ans2=(-b-sqrt(delta))/2*a
    return ans1