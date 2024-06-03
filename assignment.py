
def func1(a, b):
    if a <= 0 or b <= 0:
        return "Error"
    
    sum = a+b

    # # # #
    
    # adding a new line 
    sum += 100

    # # # #

    if sum>100:
        return sum
    elif sum==100:
        return a*b
    elif sum<100:
        return abs(a - b)
    

# print(func1(60, 50))  # Output: 110
# print(func1(50, 50))  # Output: 2500
# print(func1(30, 40))  # Output: 10
# print(func1(-10, 20))  # Output: "Error"
