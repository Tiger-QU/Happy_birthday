import time
def sing ( name ):
    print('happy birthday to you 👀')
    time.sleep(3)
    print('happy birthday to you 🐒')
    time.sleep(3)
    print('happy birthday to '+ name +' ~~')
    time.sleep(3)
    print('happy birthday to you 🎂 🥚')
    time.sleep(1)

name=input('May I have your name?')
print('hola, '+ name + ', thanks for your response！')
time.sleep(5)
sing (name)