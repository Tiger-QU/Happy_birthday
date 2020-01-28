# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# The expected answer is what you think the line of code will produce if it were to be run in IDLE.
# The final answer is the output after running the line of code in IDLE.

# The first line has already been uncommented for you. Just press F5 to run this file in IDLE

print(42)
# expected answer:42
# final answer:42

print(0000)
# expected answer:0000
# final answer:0

print("the force!")
# expected answer:the force!
# final answer: the force!

print("Hello World")
# expected answer:Hello World
# final answer: Hello World

#print "Hello World"
# expected answer: syntax error ✌️
# final answer: 

print(6 * 9)
# expected answer:54
# final answer: 54

print(2 + 3)
# expected answer:5
# final answer:5

print(2 ** 4)
# expected answer:32
# final answer:16

print(2.1**2.0)
# expected answer:4.41
# final answer:4.41


print(15 > 9.7)
# expected answer:1
# final answer:True

print((5 + 3) ** (5 - 3))
# expected answer:64
# final answer:64

print(--4)
# expected answer:error
# final answer:4

print(1 / 2)
# expected answer:0.5
# final answer:0.5

print(1 / 3)
# expected answer:0.33
# final answer:0.33333333333

#print(1 / 0)
# expected answer:error
# final answer:ZeroDivisionError: division by zero

print(7 / 3 == 7 / 3.0)
# expected answer:error
# final answer:True

print(3 * 6 == 6.0 * 3.0)
# expected answer:error
# final answer:True

print(11 % 3)
# expected answer:--
# final answer:2

print(2 > 5 or (1 < 2 and 9 >= 11))
# expected answer:false
# final answer:false

print(3 > 4 or (2 < 3 and 9 > 10))
# expected answer:false
# final answer:false

print("2" + "3")
# expected answer:23
# final answer:23

print("2" + "3" == "5")
# expected answer:false
# final answer:false

print("2" <= "5")
# expected answer:true
# final answer:true

print("2 + 3")
# expected answer:2+3
# final answer:2+3

print("May the force" + " be " + "with you")
# expected answer:May the force be with you
# final answer:May the force be with you

print("force"*3)
# expected answer:forceforceforce
# final answer:forceforceforce

print('daw' in 'padawan')
# expected answer:1
# final answer:True

a, b = 3, 4 # Do not comment this line

print(a)
# expected answer:3
# final answer:3

print(b)
# expected answer:4
# final answer:4

a, b = b, a # Do not comment this line

print(a)
# expected answer:4
# final answer:

print(b)
# expected answer:3
# final answer:

#print(red == 44)
# expected answer:error
# final answer:NameError: name 'red' is not defined

red, green = 44, 43 # Do not comment this line

print(red == 44)
# expected answer:1
# final answer:True

#print(red = 44)
# expected answer: error
# final answer:TypeError: 'red' is an invalid keyword argument for print()

print("red is 1") if red == 1 else print("red is not 1")
# expected answer:red is 1
# final answer:

print(red - green)
# expected answer: 1
# final answer:

purple = red + green # Do not comment this line

print("purple")
# expected answer:purple
# final answer:purple

print(red + green != purple + purple / purple - red % green)
# expected answer:False
# final answer:False

print(green > red)
# expected answer:1
# final answer:False

print("green bigger") if green > red else print("red equal or bigger")
# expected answer:green bigger
# final answer:red equal or bigger

print(green + 5)
# expected answer:error
# final answer:48

print(round(1.8))
# expected answer:2
# final answer:2

print(int(1.8))
# expected answer:1
# final answer:1

# The following question is to ensure that you have installed
# PILLOW, matplotlib, scipy, numpy and imageio correctly.
# Do not worry about the syntax - just uncomment the line and observe
# the output (if any)

from PIL import *
# expected answer:
# final answer:no output

from matplotlib import *
# expected answer:
# final answer:no output

from scipy import *
# expected answer:
# final answer:no output

from numpy import *
# expected answer:
# final answer: no output

from imageio import *
# expected answer:
# final answer: no output
