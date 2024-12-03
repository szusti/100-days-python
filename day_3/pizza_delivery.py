# Write a pizza delivery program
# Based on a user's order, work out their final bill.
# Size of the Pizza. S - 15$, M - 20$, L = 25$
# Pepperoni (depending on pizza size) S +2$, M and H +3$
# Extra cheese +1$


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L: ").lower()
pepperoni = input ("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input ("Do you want extra cheeeeeeeeese? Y or N: ").lower()
bill = 0

if extra_cheese == "y":
        bill += 1
if size == "s":
    bill +=15
    if pepperoni == "y":
        bill += 2

elif size == "m":
    bill +=20
    if pepperoni == "y":
        bill += 3

elif size == "l":
    bill +=25
    if pepperoni == "y":
        bill += 3
else:
    print("invalid size has been seected")

if bill > 10:
    print(f"Your bill is {bill}")