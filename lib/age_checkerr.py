from datetime import datetime
import re

def age_checker(birthday_string):
    if not re.match("^\d{4}-\d{2}-\d{2}$",birthday_string):
        raise Exception("Please insert date in YYYY-MM-DD")
    
    birthday = datetime.strptime(birthday_string, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return 'Access granted!' if age >= 16 else 'Access denied!' 
