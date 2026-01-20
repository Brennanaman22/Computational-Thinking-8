# Section 1 - Your code
from utils import *
set_background("barn")

s1 = create_sprite("cow", 100, -100)
s2 = create_sprite("chickens", -100, -100)
s2 = create_sprite("corgi", -150, -100)
s2 = create_sprite("dog", 150, -150)

message1 = create_sprite("alien",-200,200)
message1.color("blue")
message1.write("yay",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()