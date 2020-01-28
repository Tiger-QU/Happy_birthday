from math import sqrt
def solve_qe(a, b, c):
  delta = b*b - 4*a*c
  if delta >= 0:
    ans1  = (-b + sqrt(delta))/(2*a)
    ans2  = (-b - sqrt(delta))/(2*a)
    print('The two solutions are ' + str(ans1) + ' and ' + str(ans2))
  else:
    print('The equation has no real root')

solve_qe(1, 5, 6)
solve_qe(1, 1, 8)


solve_qe(1, 0, -9)
solve_qe(2, 0, 0)
solve_qe(1, 0, 1)