def girl_age(age): #reusable recipe is created
    if age < 0:
        return "Invalid age"
    elif age < 18:
        return "Underaged"
    elif age >= 18 and age < 35:
        return "Legal can date"
    else:
            return "Too old for dating"
print(girl_age(20)) #function is called and the value is passed to the function
print(girl_age(15)) #function is called and the value is passed to the function
print(girl_age(40)) #function is called and the value is passed to the function