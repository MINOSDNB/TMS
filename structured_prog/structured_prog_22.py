from datetime import datetime, timedelta

arr = [{'number': 1,
        'start': 'Minsk',
        'arrive_time': datetime(2023, 3, 20, 12, 30),
        'finish': 'Brest',
        'start_time': datetime(2023, 3, 20, 4, 20)},

       {'number': 2,
        'start': 'Stolbci',
        'arrive_time': datetime(2023, 3, 20, 8, 30),
        'finish': 'Minsk',
        'start_time': datetime(2023, 3, 20, 5, 20)},

       {'number': 3,
        'start': 'Vitebsk',
        'arrive_time': datetime(2023, 3, 20, 20, 30),
        'finish': 'Brest',
        'start_time': datetime(2023, 3, 20, 5, 20)}

        ]
timedelta_train = timedelta(hours=7, minutes=20)

for dict in arr:
    time_in_road = dict['arrive_time'] - dict['start_time']
    if time_in_road > timedelta_train:
        print(dict)
