# Car Simulator
# 1 - Inting
# 2 - Upper Capitalize Lower Title
# 3 - If Else
# 4 - List
# 5 - double if
# 6 - If In

name = input('Enter Your Name\n') # User Se Input Leta Hai Unka Nam Input() Ki Madd Se Fir Use name Variable Me Store Krta Hai

age = input('Enter Your Age\n') # User Se Input Leta Hai Unki Age Input() Ki Madd Se Fir Use age Variable Me Store Krta Hai

integer_age = int(age) # Int Ki Madd Se Hum Age Variable Jo String Hai Use Integer Bna Te Hai

if integer_age < 18: # Check Krte Hai Ki Integer_Age 18 Se Choti Hai Agar Hai To Ham Ye Print Krte Hai Aur Exit Krte Hai
    print(f'Tu Gadi Nhi Chla Skta {name} Tu {age} Saal Ka Hai Apne Ghar Me Jake Bathh')
    exit()
else: # Agar Int Krne Ke Bad Age 18 Se Zyda Huye To Ye Print Kro Aur Unhe Aage Bhej Do
    print(f"You Can Drive {name}")

print('Highway Pe Gadi Chal Te Huye...') 

user_license = input('Oye License!! De Idh\n') # User Se Input Leta Hai Unka License Input() Ki Madd Se Fir Use user_license Variable Me Store Krta Hai

verified_licenses = ['123FDE'] # Ek List Me Verified License Store Krte Hai

upper_case_licence = user_license.upper() # User_License Ko Upper Case Krte Hai EX- Agar User Ne dfedd2 to upper case vo DFEDD2 Ho Ga

if upper_case_licence == '': # Check Krte Hai Ki Agar User Nhi License Diya To Chalaan
    print('Chal Chalaan Nikal ₹500!')
    exit()
else: # Agar Diya To Niche Vala Code
    if upper_case_licence in verified_licenses: # Yaha Pr Check Krte Hai Ki Agar User Ne Jo License Diya Hai Vo Shi Hai Agar Hai To Use Jaane Do
        print('Haa Chal Jaaa')
    else: # Yaha Pr Check Krte Hai Ki Agar User Ne Jo License Diya Hai Vo Farzi Hai Agar Hai To Usse Chalaan Lo Pir Exit Kr Do
        print('Abe Hume Bewakoof Bna Ta Hai Chal Thane')
        exit()

print('Arree Chalo Finally A Gya') # Finally Me Apne Ghar Puchaygya