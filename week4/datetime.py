import datetime
datetime.date.today()  # Generates today's date yyyy,mm,dd
datetime.date.today().strftime("%Y")  # Generates today's year
datetime.date.today().strftime("%B")  # Generates today's month
datetime.date.today().strftime("%d")  # Generates today's date(dd)
datetime.date.today().strftime("%D")  # Generates today's date in mm/dd/yy format
datetime.date.today().strftime("%b")  # Generates today's month in shortened form
datetime.date.today().strftime("%y")  # Generates today's year in shortened form
datetime.date.today().strftime("%m")  # Generates today's month in numeric form
datetime.date.today().strftime("%W")  # Generates today's week number
datetime.date.today().strftime("%w")  # Generates today's weekday of the week
datetime.date.today().strftime("%j")  # Generates today's daty of year
datetime.date.today().strftime("%A")  # Generates today's day of week
datetime.datetime.now()               # Generates current date and time