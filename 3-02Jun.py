# Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
# and asks them how many hours into the future they want to go. Print out what the hour will be that
# many hours into the future, printing am or pm as appropriate. An example is shown below.
# Enter hour: 8
# am (1) or pm (2)? 1
# How many hours ahead? 5
# New hour: 1 pm

hour=int(input("Enter hour now(1-12): "))
time_period=input("Advise time period: am(1) or pm(2): ")
hours_ahead=int(input("How many hours into the future do you want to go?: "))

new_hour= (hour+hours_ahead)

if time_period == "1" and new_hour>=12:
    new_period = "2"
else:
    new_period=time_period

print("New hour:", new_hour%12, "pm" if new_period == '2' else "am")
