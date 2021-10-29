SI_mass = {'mg': 0.001, 'g': 1, 'kg': 1000, 't': 1000000}
British_American_mass = {'gr': 64.79891, 'dr': 1.7718451953125,
                         'oz': 28.349523125, 'lb': 453.59237,
                         'st': 6350.29318, 'short ton': 907185,
                         'long ton': 1016000}


def main():
    welcoming_message = '''
    Welcome to converter of units.
    By using it you can convert mass and density.
    Short guideline
    \n:
    1) To start with print needed type of measurements:
        * mass
        * density
    \n
    2) To exit the tool you can print:
        * exit
        * finish
        * done
    '''
    exiting_messages = ['exit', 'finish', 'done']
    commands = ['mass', 'density']
    print(welcoming_message)
    while True:
        command = input()
        if command not in commands and command not in exiting_messages:
            print('Please check spelling of the command and try again.')
        else:
            if command == 'mass':
                mass_converter()
            elif command == 'density':
                print('We are very sorry. Currently this function is in'
                      'development, try our mass converter.')
            elif command in exiting_messages:
                print('Thank you for using our tool.')
                break


def mass_converter():
    print('You can convert mass from/to:\n'
          '\n'
          '     * SI units: mg <-> g <-> kg <-> t\n'
          '\n'
          '     * British/American units: gr <-> dr <->oz <-\n '
          '     -> lb <-> short ton <-> long ton <-> st\n')
    unit_type_from = input('Please write unit type to be converted:')
    while unit_type_from not in SI_mass.keys() and unit_type_from not in British_American_mass.keys():
        print('Please check your spelling and try again:\n')
        unit_type_from = input()
    value = input('Please write value of interest:\n')
    error = 'TRUE'
    while error == 'TRUE':
        try:
            value = float(value)
            error = 'FALSE'
        except ValueError:
            error = 'TRUE'
            value = input('Input has to be a number. Try again:\n')
    unit_type_to = input('Please fill in unit type to which would like to convert:\n')
    while unit_type_to not in SI_mass.keys() and unit_type_to not in British_American_mass.keys():
        unit_type_to = input('Please check your spelling and try again:\n')
    if unit_type_from in SI_mass.keys():
        g_value = value * SI_mass[unit_type_from]
    else:
        g_value = value * British_American_mass[unit_type_from]
    if unit_type_to in SI_mass.keys():
        result_value = g_value / SI_mass[unit_type_to]
    else:
        result_value = g_value / British_American_mass[unit_type_to]

    print(value, unit_type_from, '=', result_value, unit_type_to)
    print('Try other values to convert.\n'
          'Print needed type of measurements. Choose:\n'
          '     * mass\n'
          '\n'
          '     * density\n')


if __name__ == "__main__":
    main()
