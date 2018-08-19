import calendar

year_list = []
for year in range(1996, 1000, -10):
    if calendar.isleap(year) and calendar.weekday(year, 1, 26) == 0:
        year_list.append(year)

print(year_list)  # he is the second youngest  # google whose birthday is year_list[1]/1/27 --> Mozart
