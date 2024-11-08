from math import pi
from random import choice as ch
from math import trunc

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]
random_planet = ch(planets)
print(random_planet)

# assigning planets their radius (km)
radius = 0

if random_planet == 'Mercury':
    radius += 2440
elif random_planet == 'Venus':
    radius += 6052
elif random_planet == 'Earth':
    radius += 6371
elif random_planet == 'Mars':
    radius += 3390
elif random_planet == 'Saturn':
    radius += 58232
else:
    print("Oops! An error occurred.")

area = (4 * (pi) * (radius ** 2))
print(f'The randomly choisen planet {random_planet} has a radius of {radius} kms and an area of {area:.2f} km^2')

