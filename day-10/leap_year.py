# Check if provided year is leap. Rules:
# This is how you work out whether if a particular year is a leap year. 
# - on every year that is divisible by 4 with no remainder
# - except every year that is evenly divisible by 100 with no remainder 
# - unless the year is also divisible by 400 with no remainder 

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input('What year: '))
leap_status = is_leap(year)
print(f"Does provided year is leap? {leap_status}")
