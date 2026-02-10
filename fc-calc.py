while True:
    # get user input
    user_choice = input("Enter '1' for Fahrenheit to Celsius, or '2' for Celsius to Fahrenheit: > ")

    # check user input is only or 2
    if user_choice not in ['1', '2']:
        print(f'Sorry, choice not valid. Please enter 1 or 2.')
    else:
        break
        

# calculate based on choice
if user_choice == '1':
    enter_fahrenheit = int(input("Enter a number in Fahrenheit: > "))
    calc_celsisus = (enter_fahrenheit - 32) // (9/5)
    print(f'{enter_fahrenheit} Fahrenheit is equal to {calc_celsisus} Celsius!')
else:
    enter_celsisus = int(input("Enter a number in Celsius: > "))
    calc_fahrenheit = (enter_celsisus * 9/5) + 32
    print(f'{enter_celsisus} Celsius is equal to {calc_fahrenheit} Fahrenheit!')