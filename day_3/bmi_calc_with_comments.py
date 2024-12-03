#BMI Calculator with comments about your bmi value

height = float(input("Provide your heigh [cm] = "))
height = (height / 100)
weight = int(input("Provide your weight [kg] = "))

bmi = round(weight / (height * height),2)

print("Your BMI is "+ str(bmi))

if 18.5 > bmi :
    print("Your are skeleton")
elif 18.5 <= bmi < 25:
    print("Normal weight")
else:
    print("You are fat")

