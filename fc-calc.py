import sys

playing = True
while playing:

    while True:
        # get user input
        user_choice = input("Enter '1' for Fahrenheit to Celsius, '2' for Celsius to Fahrenheit, or 'Q' for Quit: ")

        # check if user input is in this list
        if user_choice.upper() not in ['1', '2', 'Q']:
            print(f'Sorry, choice not valid. Please enter 1 or 2.')
        elif user_choice.upper() == 'Q':
            sys.exit()
        else:
            break

    # calculate based on choice
    if user_choice == '1':
        enter_fahrenheit = float(input("Enter a number in Fahrenheit: "))
        calc_celsisus = (enter_fahrenheit - 32) // (9/5)
        print(f'{enter_fahrenheit} Fahrenheit is equal to {calc_celsisus} Celsius!')
    else:
        enter_celsisus = float(input("Enter a number in Celsius: "))
        calc_fahrenheit = (enter_celsisus * 9/5) + 32
        print(f'{enter_celsisus} Celsius is equal to {calc_fahrenheit} Fahrenheit!')