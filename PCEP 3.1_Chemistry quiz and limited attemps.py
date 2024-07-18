print("Calculate the nuclear binding energy of U-236 per nucleon.", "\nmass of proton=1.6726E-27 kg", "\nmass of neutron=1.6749E-27kg", "\na.m.u.=1.6605E-27kg")
print("\nAssume that the molar mass of uranium is 236 g/mol for the radioactive isotope and 1 a.m.u. equals 931.5 MeV")
print("You are only allowed to attemp five times")

attempts = 0     #Define the number of attemps and number of it allowed until it reaches the limit and the system stops executing the code
attempts_limit = 5

while True:
    try: #try-execpt ValueError allows user to identify invallid input (float in integer functions) 
        number_protons = int(input("Number of protons: ")) #This value cannot be float, then, put int() function 
        mass_p = float(input("Mass of proton: "))  #Notice: mass and amu are decimal numbers...then float function is the best.
        mass_n = float(input("Mass of neutron: "))
        amu = float(input("a.m.u.: "))

        attempts += 1 

        if attempts == attempts_limit:
            print("Your attempt reached the limit. Please come back after reviewing.")
            break

        number_neutrons=236-number_protons
        number_neutrons=int(number_neutrons)
        
        binding_energy = float(((number_protons * mass_p) + (number_neutrons * mass_n)) / amu - 236) * 931.5 / (number_protons + number_neutrons)
        binding_energy = round(binding_energy, 2)
        answer = 7.58  # In MeV


        if binding_energy == answer: #DO NOT swap the if statement and elif statement below. Otherwise, "Your answer is very close" will only be executed as the right answer also exists in the defined argument
            print("Your answer is correct", "\nYour answer is ", binding_energy, "MeV")
        elif answer - 0.1 < binding_energy < answer + 0.1:
            print("Your answer is very close. Check your calculations.", "\nYour answer is ", binding_energy, "MeV") #""Additional"" condition. Not the main.
        else:
            print("Your answer is incorrect. Please try again. You can attempt", attempts_limit-attempts," more times", "\nYour answer is ", binding_energy, "MeV")

    except ValueError: #This messgae will be executed when invalid number, for example, float in the number of protons
        print("Invalid input. Please enter valid numbers for protons, neutrons, mass_p, mass_n, and amu.")
