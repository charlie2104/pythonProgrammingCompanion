#works out a workers wage

hours = int(input("how many hours have you worked today: "))
cars = int(input("how many cars have you made today: "))

wage = (hours * 9) + (cars * 0.60)

print("today you have earned £" + str(wage))
