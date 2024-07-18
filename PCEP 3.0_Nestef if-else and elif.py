a=float(input("a=")) #half of the paths difference in Bragg's Law
d=float(input("d=")) #Distance bewtween atomic planes
c=float(input("c=")) #Reflection angle
n=float(input("n="))
#Assume n is 1

import math #imports math functions from library and use math.sin or math.cos

wavelength=2*d*math.sin(c)/n

print("n times wavelength=2a=" + str(2*a))

if wavelength<=150E-12:
    if wavelength<150E-12:
        print("Wavelenth",wavelength,"is shorter than 150pm")
    else:
        print("Wavelength",wavelength, "is equal to 150pm")
else:
    print("Wavelength",wavelength, "is greater than 150pm")

n=(2*a)/wavelength
correct_n=1

if n==correct_n:
    print("\nThe answer is consistent", "\nYour answer was n=", n)
elif 1<=n<2 or 1>=n>-2:
    print("\nThe answer is acceptable", "\nYour answer was n=", n) #elif is from else if, meaning that  elif statement allows user to consider multiple conditions 
elif n!=correct_n:
    print(n==correct_n, "\nThe answer is not consistent", "\nYour answer was n=", n)
elif n>3:
    print(n!=correct_n, "\nThe answer for n is greater than 3", "\nYour answer was n=", n)
else:
    print("\nRedo the calculation")
