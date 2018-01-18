import math

length = float(input("Enter length in cm: "))
radius = float(input("Enter radius in cm: "))

area = radius * radius * math.pi
volume = area * length

print("Area is {0:.2f} cm^2".format(area))
print("Volume is {0:.2f} cm^3".format(volume))