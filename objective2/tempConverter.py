#converts temperatures from fahrenheit to centigrade

tempF = int(input("input a temperature in Fahrenheit: "))

tempC = (tempF-32)*(5/9)

print("that is " + str(tempC) + "Centigrade")
