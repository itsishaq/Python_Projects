import datetime
from dateutil import relativedelta

# Create two imaginary or desired dates
# Here i have given Two sample bday dates
#any dates cane be preferable here.
date1 = datetime.date(2003,6,6)
date2 = datetime.date(2021,12,5)

# Using relativedelta find the difference between the recent date
# and past date.
diff = relativedelta.relativedelta(date2,date1)

# Using datetime module find the years, months, days between those two dates
years = diff.years
months = diff.months
days = diff.days

# Print the output using print statement by formatting values
print('{} years {} months {} days'.format(years,months,days))
