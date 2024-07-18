a=float(input("input the value of opposite:"))
b=float(input("input he value of adjacent:"))
print("Hypotenuse length is " + str((a**2+b**2)**.5))

#Thanks to str() function, string does not have to be made, and no comma is needed as long as " " + str() is present


x=float(input("x value:")) # input a float value for variable a here
y=float(input("y value:"))  # input a float value for variable b here

print("Addition: " + str(x+y))# output the result of addition here
print("Subtraction: " +str(x-y))# output the result of subtraction here
print("Multiplication: " + str(x*y))# output the result of multiplication here
print("Division: " + str(x/y))
        
print("\nThat's all, folks!")



x = float(input("Enter value for x: "))

y=1/(x+(1/(x+(1/(x+(1/x))))))                 # Write your code here

print("y =", y)
