beatles=[]# step 1
print("Step 1:", beatles)

beatles.append("John Lennon")# step 2
beatles.append("Paul McCartney")
beatles.append("George Harrion")
print("Step 2:", beatles)


New_members=input("Enter yes to add two members to the band: ")# step 3
Names="Stu Sutcliffe", "Pete Best"
if New_members=="yes":
    beatles.append("Stu Sutcliffe")
    beatles.append("Pete Best")
print("Step 3:", beatles)

del beatles[3]# step 4
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr")# step 5
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
