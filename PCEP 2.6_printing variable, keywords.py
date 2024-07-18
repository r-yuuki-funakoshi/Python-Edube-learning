firstname=input("May I have your first name please?")
lastname=input("May I have your last name please?")
BD=input("Enter your birthday mm/dd/yyyy :")
FN=firstname, lastname #Here, redefine a new variable 
The_Cutest_Name='Aachal', 'Patel' #Define the correct input #Must be written as a string
if FN==The_Cutest_Name: #Use ==(equality) to make "if" keyword so that Python prints the string only when the correct input is input
    print("Such a pretty name HAHA (^ ^)")
else:
    print("My GF has much cuter name...")
#When incorporating variables that have inputs into a function, use + + as a concatenator to make direct input from plugged-in numbers or words for the variables
    #otherwise the function introduces the literal word typed in (Here, lastname, firstname, or BD
print("\nYour name is "+lastname+", "+firstname+" , And Your birthday is "+BD+" \nYour identity is confirmed, Thank you.")

password=input("Now enter password:")
correct_password="112820035312000" #To define the correct value of the put, even integers and any other literals must be strings or displayed green
if password==correct_password:
    print("Congratulation! You have won a kiss! (^ -)")
else:
    print("Sorry!! Challenge again.")

#Key words; False, None, True, and, as, assert, break, class, continue, def, del, elif, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
