age = int(input("What is your age?"))

if age >= 16:

    print("You can drive!")

    if age >= 18:
        print("You can vote!")

    if age >= 21:
        print("You can drink!")

else:
    print("Some day, kid...")
