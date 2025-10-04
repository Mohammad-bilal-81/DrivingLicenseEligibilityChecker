print('Welcome to Driving License Eligibility Checker, made by Bilal.')
print()

# Collect user input
name = input('Enter your name: ')
age = int(input('Enter your age: '))

print()
print('checking driving license eligibility...')
print()

# Compare age
if age >= 18:
    print(f'{name}, you are Eligible for driving.')
else:
    print(f'{name}, you are not eligible for driving.')
