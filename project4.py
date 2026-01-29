import turtle, time, random
from utils import *

# Section 1 - setup
set_background("minecraftcave")
sprite1 = create_sprite("alien", -200, 200)
sprite1.hideturtle()

# TODO - create at least two variables and set their starting value. ex: cookies = 0
stone = 0
iron = 0
diamonds = 0




# Section 2 - controls
# TODO - define an action. ex: def my_control()
def mine_stone():
    global stone
    stone += 1
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    create_sprite("Stone (1).gif",x,y)
window.onkeypress(mine_stone, "space")
def get_iron():
    global iron,stone
    if stone >= 3:
        iron += 1
        stone -= 3
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        create_sprite("iron.gif",x,y)
window.onkeypress(get_iron, "i")
def get_diamonds():
    global iron,diamonds
    if iron >= 3:
        diamonds += 1
        iron -= 3
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        create_sprite("diamonds.gif",x,y)
window.onkeypress(get_diamonds, "d") 

    



# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(100000000000000000000):
    if diamonds >= 100:
        print("you win")
        sprite1.write("YOU WIN!!!!!!!!", font = ("Arial", 40, "normal"))
    
    # TODO - put any repeating actions here

    time.sleep(0.01)
    window.update()