value = 0
print(value is None) #Is this strictly missing data? The answer is False because the value is 0, not None  
print(not value) #This is a shortcutthat may work but risky as it may cause bugs in the future. The answer is True because the value is 0, which is considered False in Python
print(optional is None) #Is this strictly missing data? The answer is True because the value is None    