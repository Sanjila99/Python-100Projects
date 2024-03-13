date = input("What day is it today: ")
print(date)
breakfast = input("How many calories did you have for breakfast? ")
print(breakfast)
lunch = input("How many calories did you have for lunch? ")
print(lunch)
dinner = input("How many calories did you have for dinner? ")
print(dinner)
snack = input("How many calories did you have for your snack? ")
print(snack)

sum = int(breakfast) + int(lunch) + int(dinner) + int(snack)

print(f"Calorie content for {date}: {sum}")