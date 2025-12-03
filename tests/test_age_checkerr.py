import pytest
from lib.age_checkerr import *
# Age Checker Function Design Recipe

## 1. Describe the Problem
"""
As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

imports: datetime from datetime

def age_checker(date)
    Converts date into datetime object and checks if their age is <=16

    Parameters: (list all parameters and their types)
    date as string

    Returns: (state the return value and its type)
        returns string

    Side effects: (state any side effects)
"""

"""
Given date "2015-12-01"
It returns "Access denied!"
"""
def test_given_date_under_16_returns_access_denied():
    actual = age_checker('2015-12-01')
    expected = 'Access denied!'
    assert actual == expected

"""
Given date "1999-07-22"
It returns "Access granted!"
"""
def test_given_date_above_16_returns_access_granted():
    actual = age_checker('1999-07-22')
    expected = 'Access granted!'
    assert actual == expected

"""
Given date "2009-12-03"
It returns "Access granted!"
"""
def test_given_date_exactly_16_returns_access_granted():
    actual = age_checker('2009-12-03')
    expected = 'Access granted!'
    assert actual == expected

"""
Given an input in wrong format"
It raises an error"
"""
def test_given_date_wrong_format_raises_error():
    with pytest.raises(Exception) as error:
        age_checker('2009-12-3')
    actual = str(error.value)
    expected = 'Please insert date in YYYY-MM-DD'
    assert actual == expected

