def add_time(start, add, day=''):
    hour = lambda var: var.split(':')[0]
    minute = lambda var: var.split(':')[1]

    start_time = {'hour': int(hour(start)), 'minute': int(minute(start)[:-3]), 'am/pm': start[-2:], 'day': 1}
    add_time = {'hour': int(hour(add)), 'minute': int(minute(add))}

    # print(start_time)
    # print(add_time)

    add_func = lambda unit: start_time[unit] + add_time[unit]

    new_time = {'hour': add_func('hour'), 'minute': add_func('minute'), 'am/pm': start[-2:], 'day': 1}

    if day == '':
        new_time['weekday'] = -50
    elif day.lower() == 'monday':
        new_time['weekday'] = 0
    elif day.lower() == 'tuesday':
        new_time['weekday'] = 1
    elif day.lower() == 'wednesday':
        new_time['weekday'] = 2
    elif day.lower() == 'thursday':
        new_time['weekday'] = 3
    elif day.lower() == 'friday':
        new_time['weekday'] = 4
    elif day.lower() == 'saturday':
        new_time['weekday'] = 5
    elif day.lower() == 'sunday':
        new_time['weekday'] = 6

    while new_time['minute'] > 59:
        new_time['hour'] += 1
        new_time['minute'] -= 60

    while new_time['hour'] > 12:

        if new_time['am/pm'] == 'PM':
            new_time['day'] += 1
            if new_time['weekday'] < 6:
                new_time['weekday'] += 1
            else:
                new_time['weekday'] = 1

        elif new_time['am/pm'] == 'AM':
            new_time['am/pm'] = 'PM'

        new_time['hour'] -= 12

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    if day:
        new_time['the_day'] = weekdays[new_time['weekday']]

    # print(new_time)

    if new_time['day'] == 1 and day == '':
        return f"{str(new_time['hour']).zfill(2)}:{str(new_time['minute']).zfill(2)} {new_time['am/pm']}"
    elif new_time['day'] == 1 and day != '':
        return f"{str(new_time['hour']).zfill(2)}:{str(new_time['minute']).zfill(2)} {new_time['am/pm']}, {new_time['the_day']}"
    elif new_time['day'] == 2 and day == '':
        return f"{str(new_time['hour']).zfill(2)}:{str(new_time['minute']).zfill(2)} {new_time['am/pm']} (Next day)"
    elif new_time['day'] == 2 and day != '':
        return f"{str(new_time['hour']).zfill(2)}:{str(new_time['minute']).zfill(2)} {new_time['am/pm']}, {new_time['the_day']} (Next day)"
    elif new_time['day'] > 2 and day == '':
        return f"{str(new_time['hour']).zfill(2)}:{str(new_time['minute']).zfill(2)} {new_time['am/pm']} ({new_time['day'] - 1} days later)"
    elif new_time['day'] > 2 and day != '':
        return f"{str(new_time['hour']).zfill(2)}:{str(new_time['minute']).zfill(2)} {new_time['am/pm']}, {new_time['the_day']} ({new_time['day'] - 1} days later)"


print(add_time('10:00 AM', '35:00', 'FrIdAy'))
