"""
This Module will generate a random date between the two dates
and will check if the random date is a Monday.
"""
import datetime
import random


def no_vinnigrete(first_date, second_date):
    """
    :param first_date: string of the first date
    :param second_date: string of the second date
    
    """
    try:
        first_date = datetime.datetime.strptime(first_date, "%Y-%m-%d")
        second_date = datetime.datetime.strptime(second_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format")
        return

    if second_date < first_date:
        first_date, second_date = second_date, first_date

    delta_days = (second_date - first_date).days
    random_days = random.randint(0, delta_days)
    random_date = first_date + datetime.timedelta(days=random_days)

    if random_date.weekday() == 0:   # 0 is Monday
        print("Ain't gettin' no vinaigrette today :(")


if __name__ == "__main__":
    date1 = input("Enter the first date in the format YYYY-MM-DD: ")
    date2 = input("Enter the second date in the format YYYY-MM-DD: ")
    no_vinnigrete(date1, date2)
