import calendar
from datetime import datetime

c = calendar.TextCalendar()
strcal = c.formatmonth(datetime.now().year, datetime.now().month)
print(strcal)

# Create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.THURSDAY)
# strcalhtml = hc.formatmonth(2025, 1)
# print(strcalhtml)