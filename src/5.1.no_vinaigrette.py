import datetime
import random

from dateutil.rrule import weekday




def no_vinaigrette():
    """
    This function will take two dates as input and will generate a random date between the two dates.
    It will check if the random date is a Monday. If it is, it will print "I don't have vinaigrette".
    """
    first_date = input("Enter the first date in the format YYYY-MM-DD: ")
    second_date = input("Enter the second date in the format YYYY-MM-DD: ")

    try:
        first_date = datetime.datetime.strptime(first_date, "%Y-%m-%d")
        second_date = datetime.datetime.strptime(second_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format")
        return

    random_date = random.randint(first_date.toordinal(), second_date.toordinal())
    random_date = datetime.datetime.fromordinal(random_date)

    if datetime.date.weekday(random_date) == 0:   # 0 is Monday
        print("I dont have vinaigrette")


if __name__ == "__main__":
    no_vinaigrette()
