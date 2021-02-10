"""A vaccination calculator."""

__author__ = "730400848"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import timedelta

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import datetime

population: int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
goal_vaccinated: int = int(input("Target percent vaccinated: "))

today: datetime = datetime.today()

population_vaccinated: int = round(population - (population - (int(doses_administered / 2))))
people_needing: int = round(((goal_vaccinated / 100) * population) - population_vaccinated)
days_need: int = round(people_needing / (doses_per_day / 2))

days_needed: timedelta = timedelta(days_need)
target_date: datetime = today + days_needed

first_half_statement: str = str("We will reach " + str(goal_vaccinated) + "% vaccination in " + str(days_need))
second_half_statement: str = str(" days, which falls on " + target_date.strftime("%B %d, %Y"))
print(first_half_statement + second_half_statement)