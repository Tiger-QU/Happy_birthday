from random import uniform
def monte_carlo():
    print('I will throw 10000000 darts')
    inside, total=0,0
    for throw in range(10000000):
        total=total+1
        x,y=uniform(-1,1),uniform(-1,1)
        if x*x+y*y<=1:
            inside=inside+1
    return inside*4/total

monte_carlo()