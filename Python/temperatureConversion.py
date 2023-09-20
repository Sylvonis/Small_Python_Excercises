"""

I won't refactor or put all these functions to another file that
i could import, not yet - 19/09/2023

"""

def c_to_k(c):
    k = float(c) + 273.15
    return float(k)


def k_to_c(k):
    c = float(k) - 273.15
    return float(c)


def f_to_c(f):
    c = (float(f) - 32.00) * (5 / 9)
    return float(c)


def c_to_f(c):
    f = float(c) * (9.00 / 5.00) + 32.00
    return float(f)


def f_to_k(f):
    k = (float(f) - 32.00) * (5.00 / 9.00) + 273.15
    return float(k)


def k_to_f(k):
    f = (float(k) - 273.15) * (9.00 / 5.00) + 32.00
    return float(f)


input_name = None

while input_name is None:
    try:
        input_name = input("Choose a Temperature to Convert:\n Celcius: C\n Kelvin: K\n Fahrenheit: F\n"
                           "or input 'Q' to Quit\n\n").upper()
        temp = None

        if input_name == 'C':
            c_to_ = None
            while c_to_ is None:
                c_to_ = input(
                    "Which temperature you want Celcius to be converted to?\n Kelvin: K\n Fahrenheit: F\n").upper()
                try:
                    if c_to_ == 'K':
                        temp = None
                        while temp is None:
                            try:
                                temp = float(input('Which temperature value you want to convert?'))
                                value = c_to_k(temp)
                                print(str(temp) + ' Celcius converted to Kelvin is:\n' + str(round(value, 2)))
                            except:
                                print('uh oh, this is not a valid number')
                    if c_to_ == 'F':
                        temp = None
                        while temp is None:
                            try:
                                temp = float(input('Which temperature value you want to convert?'))
                                value = c_to_f(temp)
                                print(str(temp) + ' Celcius converted to Fahrenheit is:\n' + str(round(value, 2)))
                            except:
                                print('uh oh, this is not a valid number')
                except:
                    'uh oh, not a valid temperature'


        elif input_name == 'K':
            k_to_ = None
            while k_to_ is None:
                k_to_ = input(
                    "Which temperature you want Kelvin to be converted to?\n Celcius: C\n Fahrenheit: F\n").upper()
                try:
                    if k_to_ == 'C':
                        temp = None
                        while temp is None:
                            try:
                                temp = float(input('Which temperature value you want to convert?'))
                                value = k_to_c(temp)
                                print(str(temp) + ' Kelvin converted to Celcius is:\n' + str(round(value, 2)))
                            except:
                                print('uh oh, this is not a valid number')
                    if k_to_ == 'F':
                        temp = None
                        while temp is None:
                            try:
                                temp = float(input('Which temperature value you want to convert?'))
                                value = k_to_f(temp)
                                print(str(temp) + ' Kenvin converted to Fahrenheit is:\n' + str(round(value, 2)))
                            except:
                                print('uh oh, this is not a valid number')
                except:
                    'uh oh, not a valid temperature'


        elif input_name == 'F':
            f_to_ = None
            while f_to_ is None:
                f_to_ = input(
                    "Which temperature you want Fahrenheit to be converted to?\n Celcius: C\n Kelvin: K\n").upper()
                try:
                    if f_to_ == 'C':
                        temp = None
                        while temp is None:
                            try:
                                temp = float(input('Which temperature value you want to convert?'))
                                value = f_to_c(temp)
                                print(str(temp) + ' Fahrenheit converted to Celcius is:\n' + str(round(value, 2)))
                            except:
                                print('uh oh, this is not a valid number')
                    if f_to_ == 'K':
                        temp = None
                        while temp is None:
                            try:
                                temp = float(input('Which temperature value you want to convert?'))
                                value = f_to_k(temp)
                                print(str(temp) + ' Fahrenheit converted to Kelvin is:\n' + str(round(value, 2)))
                            except:
                                print('uh oh, this is not a valid number')
                except:
                    'uh oh, not a valid temperature'
        elif input_name == 'Q':
            break
        else:
            print("\n\n\n\n\nThis is not a valid temperature\n")

    except:
        continue
