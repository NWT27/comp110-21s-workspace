"""Vaccine calculator exercise as a structured program."""


from datetime import datetime, timedelta


__author__ = "730400848"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days_needed: int = days_to_target(population, doses, doses_per_day, target)
    target_date: str = future_date(days_needed)
    print("We will reach " + str(target) + "% vaccination in " + str(days_needed) + " days, which falls on " + target_date.strftime("%B %d, %Y"))
    return None


def days_to_target (population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Computation of how many days are needed until the target is reached."""
    population_vaccinated: int = round(population - (population - (int(doses / 2))))
    people_needing: int = round(((target / 100) * population) - population_vaccinated)
    days_needed: int = round(people_needing / (doses_per_day / 2))
    return (days_needed)


def future_date (days_needed: int) -> str:
    """Computation of the future date that the target will be reached."""
    today: datetime = datetime.today()
    days_needed: timedelta = timedelta(days_needed)
    target_date: datetime = today + days_needed
    str(target_date)
    return target_date


if __name__ == "__main__":
    main()