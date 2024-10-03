#current time
from datetime import datetime as dt
import pytz
print(dt.now())
tz = pytz.timezone('Singapore')
print(dt.now(tz))
print(len(pytz.all_timezones))
