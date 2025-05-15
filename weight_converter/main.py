# Python weight converter

weight=float(input("Enter your weight: "))
unit=input("kilograms or Pounds?(K or L): ")

if unit=="K"or unit=="k":
    weight=weight*2.205
    unit="Lbs,"
elif unit=="L"or unit=="l":
    weight=weight/2.205
    unit="Kgs."
else:
    print(f"{unit} was not valid:")
    
print(f"Your weight is:{round(weight,3)} { unit}")