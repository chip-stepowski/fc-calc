# get user input
user_choice = input("Would you like to calculate fahrenit to celsius or celsius to fahrenheit? Enter 1 for F to C or 2 for C to F: ")

print(user_choice)

if user_choice == '1':
    enter_fahrenheit = int(input("Enter a number in fahrenheit: "))
    print(enter_fahrenheit)
    calc_celsisus = (enter_fahrenheit - 32) // (9/5)
    print(f'{enter_fahrenheit} fahrenheit is equal to {calc_celsisus} celsius!')