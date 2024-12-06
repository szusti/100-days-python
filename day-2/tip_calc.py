# -------- Tip Caclulator ------
# Ask for total bill
# How much bill percentage
# How many people to split the bill
# Show how much each person need to pay

total_bill = float(input("How much you had to pay for all? "))
tip_percentage = int(input("How much tip you would like to give [%]"))
num_of_people = int(input("How many people to split the bill? "))

person_bill_no_tip = round(total_bill / num_of_people,2)
tip_total = total_bill * float(0.01 * tip_percentage)
tip_person = tip_total / num_of_people 
bill_per_person = person_bill_no_tip + tip_person
print(f"Each person need to pay {bill_per_person} pln")

