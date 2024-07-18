#1: creating a list using loops and more methods. Check concept if not sure
n=10
List1=[1+(n-1) for n in range (1, n+1)]
print("List of natural numbers =>10: ", List1)
#2: geometric sequence
n=10
List2=[4*2**n-1 for n in range(1, n-1)]
print("Geometric sequence: ", List2)
#3: Recursive function which is A0=1, and An+1=An*n where n>1
n = 10
A = 1
Recursive=[] #If a list is to made, it must be defined and empty OUTSIDE of the for loop.
for i in range(1, n + 1):
    A *= i #(Same as A=A*i for i in range(1, n+1))
    print(A) #Prints each number in the series
    Recursive.append(A) #Adds elements to the list everytime i = i+1 until it reachs the end of the range defined above
print(Recursive)
#4: 
