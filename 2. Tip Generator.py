name=input("Enter you name:\n")
print("Hi " + name + ", welcome to the tip calculator!")
bill=float(input("What was the total bill?\n$"))
tip=int(input("What percentage of tip would you like to give?\n"))
persons=int(input("How many people to split the bill?\n"))
tip=(tip/100)*bill
bill+=tip
individual_bill=round(bill/persons,2)
print(f"Each person should pay: ${individual_bill}")