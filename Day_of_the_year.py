#Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

class Solution: 
    def dayOfYear(self, date: str) -> int: #Takes a string date as input, which is expected to represent a date in the format "YYYY-MM-DD", and it returns an integer representing the day number of the year corresponding to that date.
        # we first make a list of days in a year when a specific
        # month ends
        list_year = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334] #A list representing the cumulative days at the end of each month in a non-leap year

        day = int(date[-2:]) #Extract the day,year,and month from the input date string 
        year = int(date[:4])
        month = int(date[5:7])

        # if year is leap and February is gone, add an extra day
        if year % 4 == 0 and year != 1900 and month > 2:
            day += 1

        # return days of a specific month + date
        return list_year[month-1] + day

#If the year is divisible by 4, not equal to 1900, and the month is greater than 2 (after February), it means it's a leap year, so an extra day is added to the day variable.