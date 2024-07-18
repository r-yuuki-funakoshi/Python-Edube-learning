loop_termination_code="chupacabra"
attempt=0
while True:
    code=input("Enter the loop termination code: ")
    if code==loop_termination_code:
        print("You've successfully left the loop.", "Answer:", loop_termination_code)
        break
    attempt+=1
    if attempt==5:
        print("You've reached the attempt limit.")
        break
    else:
        print("Try again.")
        continue #continue statement is not necessary but ensures that current iteration is skipped and proceeds to the next one
