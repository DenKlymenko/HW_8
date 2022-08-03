from datetime import datetime

users = [
    {'name': 'Tom', 'birthday': datetime(year=2022, month=8, day=6)},
    {'name': 'Bill', 'birthday': datetime(year=2022, month=9, day=5)},
    {'name': 'Jill', 'birthday': datetime(year=2022, month=10, day=8)},
    {'name': 'Jan', 'birthday': datetime(year=2022, month=11, day=14)}
]

week = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday',
        4:'Friday', 5:'Suturday', 6:'Sunday'
}

def get_birthdays_per_week():
    today_date = datetime.now()
    for user in users:
        difference = user['birthday'] - today_date
        if difference.days <= 7:
            if user['birthday'].weekday() == 5 or user['birthday'].weekday() == 6:
                print(f"next_monday: {user['name']}")
            else:
                print(f"{week[user['birthday'].weekday()]} : {user['name']}")
get_birthdays_per_week()




