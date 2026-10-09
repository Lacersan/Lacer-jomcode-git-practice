def validate_capacity(capacity): #def means you are defining the reusable recipe, if not you have to copy/paste 1-5 eveytime
        if type(capacity) is int and 1 <= capacity <= 500:
                return "Valid Capacity"
        else:
                return "Invalid capacity" 
print(validate_capacity(1)) #indentation or tab is super important!!!!
print(validate_capacity(500))
print(validate_capacity(0))
print(validate_capacity(500.5))
print(validate_capacity("true"))