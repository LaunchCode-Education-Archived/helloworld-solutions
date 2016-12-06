a = int(input("Please enter a number: "))

if a < 30:
    print("The number must be less greater than 30. Try again.")
if a > 100:
    print("The number must be less than or equal to 100. Try again.")
else:
    if a % 2 == 0:
        print("The number must be odd. Try again.")
    else:
        print("That's a great number. Thanks!")
