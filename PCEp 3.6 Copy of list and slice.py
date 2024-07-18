#Example1
my_list=[1, 2, 3, 4]
my_list2=my_list #Here, the definition of my_list2 is a copy of the name of my_list
                                #Thus, the value of my_list2 will change as the elements of my_list change
my_list[1]=3
print(my_list2)
#The output will be [1,3,3,4]

#Example2
my_list=[1,2,3,4,5]
my_list2=my_list[:] #The slice [:] creates a entirely new copy that is separate from the original copy

my_list[0]=11
print(my_list2)
#The output will be [1,2,3,4,5] NOT [11,2,3,4,5]

#Example3
my_list=[1,2,3,4,5,6]
my_list2=my_list[0:3] #{starting position (INCLUDED) : End (NOT INCLUDED))
print(my_list2)
#The out put must be [1,2,3]

#Example4: Negative indices
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1] #-1 indicates the last number of the element
print(new_list)
#Output will be [8,6,4]

#Example5: del function usage
list1=[1,2,3,4,5,6]
del list1[1:3]
print(list1)

#Example6:
list1=[1,3,5,7,9]
list2=list1[2:]
print(list2)
