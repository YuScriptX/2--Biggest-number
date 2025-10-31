# Biggest Number

a = int(input("Enter a number?: "))
b = int(input("Enter a number?: "))

def max_of_two():
    if a > b:
        return a
    else:
        return b
    
print(max_of_two())