def leap_year(year):
    """
    A function that determines whether a given year is a leap year or not.
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
