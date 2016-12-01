miles = float(input("How many miles have you run so far?"))
run_time = float(input("How many hours ago did you start?"))

# Calculate the current pace of the runner
current_pace = miles / run_time

# Calculate the distance they have left to run
distance_remaining = 26.2 - miles

# Calculate time remaining
time_remaining = distance_remaining / current_pace

# Print the result
print("At this rate, you have", time_remaining, "hours to go. Yikes... best of luck")
