from __future__ import division

pi = 3.14159265
g = 6.67428*(10**-11)

radius = raw_input("Enter Radius -->")
def display_results(radius , mass , velocity):
    print "Radius of the planet"  , radius/1000 ,"km"
    print "Mass of the planet" , float(mass/10**21) ,"(10**21 kg)"
    print "Escape velocity of the planet" , velocity/1000 , "(km/s)"

def escape_velocity(circumference , acceleration):
    radius = circumference/(2*pi)
    mass = (acceleration * radius ** 2)/g
    vEscape = ((2*g*mass)/radius)**0.5
    display_results(radius , mass , vEscape)

escape_velocity(40075000 , 10)