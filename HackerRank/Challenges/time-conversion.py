import re

time12 = re.match("(\d\d):(\d\d):(\d\d)([AP]M)", input())
hour12 = int(time12.groups()[0])
am = time12.groups()[3] == "AM"
if hour12 == 12:
    hour24 = 0
else:
    hour24 = hour12
if not am:
    hour24 += 12
print("{:02d}:{}:{}".format(hour24, *time12.groups()[1:-1]))