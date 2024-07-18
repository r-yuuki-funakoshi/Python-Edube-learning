hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

print(hat_list)
New_element=int(input("Enter an integer to replace an element/scalar from the list with it:"))# Step 1: write a line of code that prompts the user to replace the middle number with an integer number entered by the user.
Number_replaced=int(input("Enter an integer (from 0-4) that is going to be replaced:"))
hat_list[Number_replaced]=New_element

del hat_list[-1]# Step 2: write a line of code that removes the last element from the list.

print("The length of the existing list", len(hat_list))# Step 3: write a line of code that prints the length of the existing list.
print(hat_list)
