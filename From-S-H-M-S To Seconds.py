# Just a Starter program to calculate the sum of seconds from days, hours, minutes and seconds....

import time


def Form():
    days = int(input("Input days: ")) * 3600 * 24
    hours = int(input("Input hours: ")) * 3600
    minutes = int(input("Input minutes: ")) * 60
    seconds = int(input("Input Seconds: "))

    time = days + hours + minutes + seconds

    print("The amount of seconds", time)


Form()

time.sleep(2)  # A small delay for the UX.



# Starts the different cases a user can input.

yes = {'yes', 'y', 'Yes', 'Y', 'Yeah', 'yeah', 'yess', 'Yess'}
no = {'no', 'n', 'N', 'No', 'Noo', 'noo'}

Message = input("Do you want to do another conversion?").lower()

if Message in yes:
    print("Thank you for using my converter!. Starting again..... ")
    time.sleep(2)
    Form()

elif Message in no:
    print("Okay!")

else:
    print("No answer. Asking user again...")
    time.sleep(2)
    finMessage(

