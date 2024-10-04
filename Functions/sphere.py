from math import pi
def sphereArea(radius):
    area = 4 * pi * radius ** 2
    return round(area, 2)

def sphereVolume(radius):
    volume = 4 / 3 * pi * radius ** 3
    return round(volume, 2)

def test():
    print(f'The area of a sphere of radius 4 is {sphereArea(4)}')
    print(f'The volumen of a sphere of radius 7 is {sphereVolume(7)}')

test()