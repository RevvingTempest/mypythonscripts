from datetime import date
import random

x = 0

for x in range(25):

    start_date = date.today().replace(day=1, month=1).toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))

    print(format(random_day,'%m-%d-%Y'))

    x += 1

    
