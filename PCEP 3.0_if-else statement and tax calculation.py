income = float(input("Enter the annual income: "))

if income<85528:
    tax=income*.18-556.2
else:
    tax=(income-85528)*0.32+14839.2
tax = round(tax, 0)

if tax>=0:
    print("The tax is:", tax, "thalers")
else:
    print("Tha tax is:", 0.0, "thalers")
