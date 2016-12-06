day = input("What day of the week is it?")

normal_price = 0.99 * 12

if day == "Sunday":

    # if it isn't Sunday, we save the user from having to answer
    # this question by placing it within the conditional
    date = input("What day of the month is it?")
    date = int(date)

    if date % 2 == 0:
        todays_price = normal_price * 0.75
    else: # day is Sunday, but not even
        todays_price = normal_price
        
else: # day is not Sunday
    todays_price = normal_price

print("The price of a dozen donuts today is:", todays_price)
