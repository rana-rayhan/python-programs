# The suggestion should change if the temperature (measured in degrees Celsius)
# is over 20, 10 or 5 degrees, and also if there is rain on the radar.

print("What is the weather forecast for tomorrow?")

temp = int(input("Temperature: "))
isRain = input("Will it rain (yes/no): ")

print("Wear jeans and a T-shirt")
if temp <= 20:
    print("I recommend a jumper as well")
if temp <= 10:
    print("Take a jacket with you")
if temp <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if isRain == "yes":
    print("Don't forget your umbrella!")
