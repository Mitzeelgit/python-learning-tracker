def unitconverter():

    print("----------------UNIT-CONVERTER----------------")
    print("LENGTH : TYPE LENGTH")
    print("WEIGHT : TYPE WEIGHT")
    print("TEMPERATURE : TYPE TEMPERATURE")
    print("VOLUME : TYPE VOLUME")

    converter_ask = ''
    converter_options = ['LENGTH', 'WEIGHT', 'TEMPERATURE', 'VOLUME']

    while converter_ask not in converter_options:
        converter_ask = input("Which unit do you want to convert? \n").strip().upper()

        if converter_ask not in converter_options:
            print("Please enter a valid unit")

    if converter_ask == 'LENGTH':

        to_meters = {
            'MILLIMETERS': 0.001,
            'CENTIMETERS': 0.01,
            'METERS': 1.0,
            'KILOMETERS': 1000.0,
            'INCHES': 0.0254,
            'FEET': 0.3048,
            'YARDS': 0.9144,
            'MILES': 1609.344,
            'NAUTICAL-MILES': 1852.0,
            'LIGHT-YEARS': 9.4607304725808e15
        }

        print("----------------LENGTH----------------")
        for unit in to_meters:
            print(unit)

        len_ask1 = ''
        len_ask2 = ''

        while len_ask1 not in to_meters:
            len_ask1 = input("Enter your first unit (from): \n").strip().upper()
            if len_ask1 not in to_meters:
                print("CHOOSE A VALID UNIT FROM ABOVE")

        while len_ask2 not in to_meters:
            len_ask2 = input("Enter your second unit (to): \n").strip().upper()
            if len_ask2 not in to_meters:
                print("CHOOSE A VALID UNIT FROM ABOVE")

        val = float(input("Enter the value of {}: ".format(len_ask1)))

        
        val_in_meters = val * to_meters[len_ask1]

        result = val_in_meters / to_meters[len_ask2]

        print("{} {} in {} is {}".format(val, len_ask1, len_ask2, result))

unitconverter()