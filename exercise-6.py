# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.


month_input = input("Enter the month (jan-dec): ").lower()
day_input = int(input("Enter the day of the month: "))

if month_input in ('dec', 'jan', 'feb', 'mar'):
    season = 'winter'
elif month_input in ('apr', 'may', 'june'):
    season = 'spring'
elif month_input in ('jul', 'aug', 'sep'):
    season = 'summer'
else:
    season = 'fall'

if month_input == 'mar' and (day_input < 19):
    season = 'winter'
elif month_input == 'jun' and (day_input < 20):
    season = 'spring'
elif month_input == 'sep' and (day_input < 21):
    season = 'summer'
elif month_input == 'dec' and (day_input < 20): 
    season = 'fall'

print(f'{month_input} {day_input} is in {season}') 
