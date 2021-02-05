"""A vaccination calculator."""

__author__ = "730400848"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


population: int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
targeted_percentage: int =int(input("Target percent vaccinated: "))

today: datetime = datetime.today()

population_vaccinated: int = int(population - (population - (int(doses_administered / 2))))
people_needing: int = int(((targeted_percentage / 100) * population) - population_vaccinated)
days_needed: int = round(people_needing / (doses_per_day / 2))

timedelta: timedelta = timedelta(days_needed)
target_date: datetime = today + timedelta

if days_needed < 0:
    print ("Goal was reached " + str(abs(days_needed)) + " days ago, which was " + target_date.strftime("%B %d, %Y") + "!")
else:
    if days_needed > 0:
        print("We will reach " + str(targeted_percentage) + "% vaccination in " + str(days_needed) + " days, which falls on " + target_date.strftime("%B %d, %Y"))
    if days_needed == 0:
        print("Goal reached today, " + str(today.strftime("%B %d, %Y")) + "!")
