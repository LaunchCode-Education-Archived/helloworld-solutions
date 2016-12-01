principal = input("How much money do you currently have in the bank?")
rate = input("What is your interest rate?")
time = input("Over how many years is the interest compounded?")

principal = float(principal)
rate = float(rate)
time = int(time)

amount = principal * (1 + rate)**time
print("After " + str(time) + " years, you will have $" + str(amount) + " in the bank")
