from datetime import datetime

def age_checker(date_string):
    date = datetime.strptime(date_string, '%Y-%m-%d')
    age = datetime.now() - date
    print(age)
    return 'Access denied!'


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))