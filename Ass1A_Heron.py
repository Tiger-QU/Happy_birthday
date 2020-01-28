from math import sqrt, sin,pi
def heron(a,b,c):
    p=(a+b+c)/2
    area=sqrt(p*(p-a)*(p-b)*(p-c))
    return area

print(heron(1,1,sqrt(2)))
print(heron(3, 4, 5))