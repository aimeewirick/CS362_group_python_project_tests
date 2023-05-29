def conv_num(num_str):
    pass


def my_datetime(num_sec):
    # Constants
    sec_per_day = 86400
    sec_per_year = 365 * sec_per_day


    # Days per month
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Calculate number of years...
    years = num_sec // sec_per_year
    secs_left = num_sec - (sec_per_year * years)

    # Helper function to check number of leap years present
    def leap_year(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    # Calculate number of leap years
    leap_years = 0
    for year in range(1970, 1970 + years):
        if leap_year(year):
            leap_years += 1

    # Calculate seconds left after removing the years that have occurred w/ leap years:
    secs_left = secs_left - (sec_per_day * leap_years)

    # Adjust February if current year is a leap year
    if leap_year(1970 + years):
        days_per_month[1] = 29

    # Calculate days that have occurred in current year
    days = (secs_left // sec_per_day)

    # Calculate months
    month = 0
    while month < 12 and days >= days_per_month[month]:
        days -= days_per_month[month]
        month += 1

    # Date components and formatting
    day = days + 1
    month += 1
    year = 1970 + years

    date_string = "{:02d}-{:02d}-{:04d}".format(month, day, year)

    return date_string





