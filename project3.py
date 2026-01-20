import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-350
y1 =250
x2 =-350
y2 =100
x3 =-350
y3 =-100
x4 =-350
y4 =-250


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("road")
t1 = create_sprite("bug1",x1,y1)
t2 = create_sprite("bug2",x2,y2)
t3 = create_sprite("bug3",x3,y3)
t4 = create_sprite("bug4",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # Todo - explain here which sprites are faster or slower
for i in range(48):
    x1 += random.randint(1,26)
    x2 += random.randint(4,23)
    x3 += random.randint(5,10)
    x4 += random.randint(6,27)
# bug 4 is most likely to win because its range is the highest so it'll move more on average 
    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("bug 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4: 
    print("bug 2 wins!")
elif x3 >= x2 and x3 >= x4 and x3 >= x1: 
    print("bug 3 wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3: 
    print("bug 4 wins!")
turtle.exitonclick()