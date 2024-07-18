#Assume
#: 4 buildings, 40 floors in each building, and 30 rooms on each floor
#False=vacant True=occcupied
rooms=[[[False for r in range(20)] for f in range(10)] for b in range(4)]

print(rooms)
print(rooms[1][9][1])

#Making reservations
rooms[0][0][0]=True
rooms[1][9][19]=True

print(rooms)
print("Room number1, first floor, first building, occupancy: ", rooms[0][0][0])

#Calculating vacancy on the 5th floor in the 4th building

vacancy=0

for room_number in range(20):
    rooms[3][4][1]=True #new reservations
    rooms[3][4][4]=True
    if not rooms[3][4][room_number]: #if not False or...True, vancancy counted by 1, or if not True or...False, not counted
        vacancy+=1
print("Vacancy on the 5th floor in the 4th building: ", vacancy)
