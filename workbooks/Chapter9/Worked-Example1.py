def remaining(capacity, registered):
    return capacity - registered

value = remaining(20, 8) #For dev to check the value of remaining seats in a class with 20 capacity and 8 registered students
print(value)
print(remaining(20, 8))
print(remaining(registered=3, capacity=5)) #print is only for dev stage, later need to add a # then indent to the left
print(remaining(registered=5, capacity=10))
print(remaining(registered=8, capacity=10))