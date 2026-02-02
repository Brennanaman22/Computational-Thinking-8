import turtle, time, random
from utils import *
# the goal of the game is to win by collecting 100 diamonds 
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
# the mine_stone makes it so when you click the space bar you will get one stone added to 
# the stone variable and a stone block will appear on screen
def get_iron():
    global iron,stone
    if stone >= 3:
        iron += 1
        stone -= 3
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        create_sprite("iron.gif",x,y)
window.onkeypress(get_iron, "i")
# the get_iron makes it so when you press the i key you get one iron added to you iron variable you lose three stone
# and iron ore block appears on screen 
def get_diamonds():
    global iron,diamonds
    if iron >= 3:
        diamonds += 1
        iron -= 3
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        create_sprite("diamonds.gif",x,y)
window.onkeypress(get_diamonds, "d") 
#the get_diamonds lets you get a 1 added to your diamonds variable and you lose three iron and a diamond appears 

    



# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(100000000000000000000):
    if diamonds >= 100:
        print("you win")
        sprite1.write("YOU WIN!!!!!!!! :)", font = ("Arial", 40, "normal"))
    
    # TODO - put any repeating actions here

    time.sleep(0.01)
    window.update()