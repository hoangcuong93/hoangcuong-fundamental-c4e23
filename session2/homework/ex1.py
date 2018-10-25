wei = int(input("weight = "))
hei = int(input("height = "))
n = hei / 100
BMI = wei / (n**2)
print("BMI =", BMI)
if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Nomar")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")