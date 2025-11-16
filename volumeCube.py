import math

def Cube(r):
    return pow(r,3)

def volumeCube(r):
    return (4/3)*math.pi*Cube(r)

r=int(input("Veillez entrer le rayon du sphère"))
volume=volumeCube(r)
print(f"Volume = {volume:.2f}")