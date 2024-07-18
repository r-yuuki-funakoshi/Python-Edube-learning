list=[3,5,4,9,0]

len(list)
print(type(list))
print(type(len))

print("The original list", list)
print("The original length of the list:", len(list)) #len...for LENGTH function can count the number of element(s) in the bracet [] 

del list[0] #Deletes the elements with the number in [] assigned. In this case, 3 will be deleted
print("\nThe new list with [0] deleted", list)
print("The new lenght of the list", len(list))

print("\n",list[-1])  #[-1] refers to 0 or the 4th (0th-4th) number. Then other numbers can be referred to as negative numbers as it is legal

list2 = [1,2,3,4,5,]

del list2[0]
del list2[1]
print("List2 [0] and [1] positions deleted", list2)
