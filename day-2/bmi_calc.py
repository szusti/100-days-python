#BMI Calculator

height = float(input("Provide your heigh [m] = "))
weight = int(input("Provide your weight [kg] = "))

bmi = weight / (height * height)

print("Your BMI is "+ str(bmi))