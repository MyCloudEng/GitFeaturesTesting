# Simple calculator 

## addition
def add(a,b):
    return a + b

## subtract
def subtract(a,b):
    return a - b

## multiply
def multiply(a,b):
    return a * b

## divide
def divide(a,b): 
    return a * b  ## intentional bug instead of diving, we are still multiplying: Here BISECT will be tested 

if __name__=="__main__":
    print("Testing calculator...")
    print(f"2 + 3 = {add(2,3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"4 * 5 = {multiply(4, 5)}")
    print(f"8 / 2 = {divide(8, 2)}")  # This will print 16 instead of 4
    print(f'2 ^ 3 = {power(2, 3)}')
    
# Append a power function
def power(a,b): 
    return a**b    
