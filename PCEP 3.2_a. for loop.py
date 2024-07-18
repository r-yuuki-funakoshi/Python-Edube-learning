#loop1
print("loop1!")
for i in range(10): # it can "browse" large collections of data item by item. #any variable after the keyword "for" is CONTROL VARIABLE--counting the loop's turns
    print("The value of i is currently", i)

#loop2 is identical to loop1 but using while loop
print("loop2=loop1")
u=0
while u<9:
    u+=1
    print("The value of u is currently", u)

#loop3
print("loop3")

import time #importing the module "time"

for i in range(100):
    print("The current time is", time.time()) #time.time() takes NO ARGUMENTS
                                                                                # time.time() module gives current times in seconds since the Unix epoch (January 1, 1970)

#loop4
print("loop4")
for x in range(5, 40, 5): #range() function can have more than one argument. Here x-value starts with 5, 10, 15.....35
    y=x**5/3
    y=float(y)
    print("The value of x:", x)
    print("The value of y:", y)
