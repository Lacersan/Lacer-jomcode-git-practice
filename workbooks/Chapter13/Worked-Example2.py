import pytest = loads someone's code into this Python script so that we can use to test

@pytest.mark.parametrize("value", [21, 35]) #An automated test that checks if the value is between 21 and 35 inclusive.
def test_youth(value): #Defines a test function called test_youth that value within the parameter
    assert type(value) is int and 21 <= value <= 35