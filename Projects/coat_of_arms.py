# Section 1 - Your code
from utils import *
set_background("seattle (1)")

s5 = create_sprite("sheild", 0, 0)
s1 = create_sprite("LOGO", 100, 100)
s2 = create_sprite("cardinal", -100, 100)
s3 = create_sprite("cardinal", -100, -100)
s4 = create_sprite("cardinal", 100, -100)

message1 = create_sprite("alien",-160,200)
message1.color("red")
message1.write("SPRAGGINS",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-155,-250)
message2.color("red")
message2.write("WORK HARD",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()