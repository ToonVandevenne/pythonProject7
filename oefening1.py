import math

#a=int(input("hoelang is de zijde van een kubus"))
#print("De inhoud van de kubus is {}".format(int(math.pow(a,3))))


#r=int(input("hoeveel is de straal?"))
#h=int(input("hoeveel is de hoogte?"))
#print("de inhoud van de cilinder is {}m³".format((math.pi*(r**2)*h)))

#a=8
#print(int(a**(1/3)))

#v=float(input("Hoe snel rijd je in km per u? "))
#print(("Jouw snelheid is\t{}km per u.\nJouw remafstand is\t{} meter.".format(v,round((v**2/100),2))))

#print(round(2+3,2))

#m=float(input("Hoeveel weegt je pakje in kilogram?"))
#d=float(input("Hoeveel kilometer moet het pakje afleggen?"))
#print("Het kost {} euro.".format(round(2+0.15*m+0.08*d,2)))

"""
z1=float(input("lengte zijde van vierkant 1?"))
z2=float(input("lengte zijde van vierkant 2?"))
z3=float(input("lengte zijde van vierkant 3?"))
print("lengte zijde 1:\t{}\nlengte zijde 2:\t{}\nlengte zijde 3:\t{}\noppervlakte 3 vierkanten:\t{}.".
      format(z1,z2,z3,z1**2+z2**2+z3**2))
"""

a=float(input("aantal m² geverfd"))
print("om {}m² te verven kost het {} euro zonder btw".format(a, (a/22)*32+1.5*a))
print("om {}m² te verven kost het {} euro met btw".format(a, 1.21*((a/22)*32+1.5*a)))