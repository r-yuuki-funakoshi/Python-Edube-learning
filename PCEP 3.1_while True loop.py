odd_products = 0
even_products = 0

while True: #while True loop enables user to loop the process of counting until  the if statements below "break"
    number1 = input("Enter a number or type MEOW to stop:")
    
    if number1.upper()== "MEOW":
        break
    
    number2 = input("Enter another number or type MEOW to stop:")
    
    if number2.upper() == "MEOW":  
        break
    
    number1 = int(number1) #integer
    number2 = int(number2)

    product = number1 * number2

    if product % 2 == 0:
        even_products += 1 #counts by 1
    else:
        odd_products += 1

print("Total odd products:", odd_products)
print("Total even products:", even_products)

print(number1.islower())
