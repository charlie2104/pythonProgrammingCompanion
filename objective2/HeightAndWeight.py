#converts height from inches to cm and weight from stone to kg

height1 = int(input("give your height in inches: "))
weight1 = int(input("give your weight in stone: "))

height2 = height1 * 2.54
weight2 = weight1 *6.364

print("your height in cm is: " + str(height2))
print("your weight in kg is: " + str(weight2))
