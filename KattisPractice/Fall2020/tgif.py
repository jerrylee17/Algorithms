months = [
    ('JAN', 31),
    ('FEB', 28),
    ('MAR', 31),
    ('APR', 30),
    ('MAY', 31),
    ('JUN', 30),
    ('JUL', 31),
    ('AUG', 31),
    ('SEP', 30),
    ('OCT', 31),
    ('NOV', 30),
    ('DEC', 31),
]
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

day, month = input().split(' ')
week = input()

elapsed = int(day)
for m, d in months:
    if m == month:
        break
    elapsed += d

dayInd = (days.index(week) + elapsed - 1) % 7
currDay = days[dayInd]
# if (month == 'FEB' and day == '29'):
#     print('TGIF')
if (month == 'FEB' or month == 'JAN') and currDay == 'FRI':
    print('TGIF')
elif not (month == 'FEB' or month == 'JAN') and currDay == 'THU' or currDay == 'FRI':
    print('not sure')
else:
    print(':(')
