from math import sqrt, sin,pi
def heron(a,b,c):
    p=(a+b+c)/2
    area=sqrt(p*(p-a)*(p-b)*(p-c))
    return area


def  inverse_acute_heron(a, area):
    L=solve_qe(-1,a**2,-area**2)
    b=2*sqrt(L)
    return b
inverse_acute_heron(1, heron(1,1,1))


def solve_qe(a, b, c):
    delta = b*b - 4*a*c
    if delta >= 0:
        ans1 = (-b + sqrt(delta))/(2*a)
        ans2 = (-b - sqrt(delta))/(2*a)
    return ans1
    