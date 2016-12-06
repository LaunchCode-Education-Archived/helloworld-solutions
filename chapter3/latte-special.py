month = input("What is the month?")

if month == "March":
    day = input("What is the day of the week?")
    if day == "Tuesday":
        print("There is a secret drink today, in celebration of St. Patrick's Day!")
    else:
        print("Sorry, this drink is only offered on Tuesdays in March!")
else:
    print("Sorry, this drink is only offered in March!")
