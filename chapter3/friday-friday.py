month = input("What month is it?")
day = input("What day is it")

if month == "June":
    if day == "Friday":

        # check the weather
        weather = input("Is it raining or sunny?")
        if weather == "sunny":
            print("The concert will be outside today!")
        else:
            print("The concert will be held inside the art museum")

    else:
        print("Sorry, concerts are only held on Fridays")
else:
    print("Sorry, concerts are only held in June")
