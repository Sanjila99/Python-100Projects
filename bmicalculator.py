#-----------BMI Calculator--------------------------

user_weight=float(input("Enter your body weight in kilograms:"))
user_height=float(input("Enter your height in centimeters:"))
user_height=user_height/100
BMI=user_weight/(user_height*user_height)
print("Your Body Mass Index :",BMI)

if BMI<18.5:
    print("Underweight.")
elif 18.5<BMI<24.9:
    print("Normal Weight")
elif 25<BMI<29.9:
    print("Overweight")
elif BMI>=30:
    print("Obese")
else:
    print("Enter Valid Details")