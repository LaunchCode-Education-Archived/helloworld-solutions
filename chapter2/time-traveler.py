current_hour = int(input("What is the current hour?"))
time_to_travel = int(input("How many hours forward will you be traveling?"))

future_hour = (current_hour + time_to_travel) % 24

print("You will be traveling to", '%02d:%02d' %(int(future_hour), int("00")))
