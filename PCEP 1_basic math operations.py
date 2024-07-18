x=-788 # x is a variable
y=x*22.002 # y is a new variable dependent on x value
x=int(x) # integer operator; fix the number to the closest integer (NO floats)
f=((3*x)**3+x**2-5*y)/100 #functon
print("Answer:", round(f, 2))#Printing the answer
                                #round function within the print function round up or down the answer, and retain decimal places as it is indicated in the parenthesis
                                 # Ex. If f=22.0091, round(f,3) gives 22.009
