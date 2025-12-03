from datetime import datetime

def age_checker(birthday_string):
    birthday = datetime.strptime(birthday_string, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return 'Access granted!' if age >= 16 else 'Access denied!' 