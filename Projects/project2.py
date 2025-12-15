lays_points = 0
doritos_points = 0
pringles_points = 0
print("pleas answer with the LETTER A B or C")
input("")

answer1 = input("Do you like A thinner chips, B thicker, or C in between?    ")
if answer1 == "A" or answer1 == "a":
    pringles_points += 3 
elif answer1 == "B" or answer1 == "b":
    doritos_points += 2
elif answer1 == "C" or answer1 == "c":
    lays_points += 2

answer2 = input("Do you like A triangles, B weird ovals, or C uniform ovals?    ")
if answer2 == "A" or answer2 == "a":
    doritos_points += 2
elif answer2 == "B" or answer2 == "b": 
    lays_points += 2
elif answer2 == "C" or answer2 == "c":
    pringles_points += 2

answer3 = input("Do you like A real potatoes, B corn, or C processed potatoes?    ")
if answer3 == "A" or answer3 == "a":
    lays_points += 2
elif answer3 == "B" or answer3 == "b":
    doritos_points += 2
elif answer3 == "C" or answer3 == "c":
    pringles_points += 2

answer4 = input("Do you like A bags, B more bags, or C cylinders?    ")
if answer4 == "A" or answer4 == "a":
    lays_points += 2
elif answer4 == "B" or answer4 == "b":
    doritos_points += 2
elif answer4 == "C" or answer4 == "c":
    pringles_points += 2

answer5 = input("Do you like things A deep fried, B seasoned and fried, or C cooked on a conveyor belt?    ")
if answer5 == "A" or answer5 == "a":
    lays_points += 2
elif answer5 == "B" or answer5 == "b":
    doritos_points += 2
elif answer5 == "C" or answer5 == "c":
    pringles_points += 2



if pringles_points >= lays_points and pringles_points >= doritos_points:
    print("you are a pringles chip person you lik pringles and money and have great hair")
elif lays_points >= pringles_points and lays_points >= doritos_points:
    print("you are a lays person and you like leys, chilling with friends, and have good humor")
elif doritos_points >= lays_points and doritos_points >= pringles_points:
    print("you are a doritos person and like doritos,pizza, and have a nice attitude")