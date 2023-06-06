# Number Saver

user = input('Enter Your Name: ')
age = int(input('Enter Your Age: '))
state = input('In Which State Do You Live: ')

Registered_Number_Plate = {}

def license_generator(user_state):
    import random
    import string
    states = {"Delhi": "DL", "Uttarpradesh": "UP"}
    if user_state in states:
        state_num = states[user_state]
    else:
        state_num = random.choice(list(states.values()))
    random_text_upper = ''.join(random.choices(string.ascii_uppercase, k=10))
    number_plate = state_num + ''.join(random_text_upper)
    return number_plate

if user not in Registered_Number_Plate:
    if age > 18:
        Registered_Number_Plate[user] = {"Name": user, "Age": age, "License": license_generator(state)}
        print(Registered_Number_Plate)
    else:
        print('You Are Not Old Enough To Drive')
else:
    print(f'{user} is already registered.')


