year = input("Please input a year:")
year = int(year)

if year % 2 == 0:

    # there will be olympics, but which of winter or summer?
    if year % 4 == 0:
        print('Summer Olympics! "Summer time..."')
    else:
        print("Winter Olympics! Let's watch some skating!")

else:
    print("Sorry, no Olympics this year.")
