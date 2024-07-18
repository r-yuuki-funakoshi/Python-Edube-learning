secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    number = input("Enter your best guess or type STOP to quit:")  #input must be inside of the while True statement

    if number.upper() == "STOP": 
        print("Coward! You may challenge again.")
        break
    else:
        number = int(number)  # Convert input to an integer

        if number == secret_number:
            print("Well done, muggle! You are free now.")
            break
        elif 700<number<800:
            print("Wow, that is close. But try again ha ha!!!")
        else:
            print("Ha ha! You're stuck in my loop!")
