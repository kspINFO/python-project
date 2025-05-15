# Temperature in Cesisu Or Fahrenheit

unit=input("Is this temperature in celsius or fahrenheit (C/F): ")
temp=float(input("Enter the temperature: "))
if unit=="C" or unit=="c":
    temp=round((9*temp)/5+32,1)
    print(f"The temperature in Fahrenheit is : {temp}0F")
elif unit=="F"or unit=="f":
    temp=round((temp-32)*5/9,1)
    print(f"The temperature in Celsius is :{temp} C")
else:
    print(f"{unit} is an invalid unit of measurement")
    
    
    
# Finding username And Domain


print("\nYou calsulate the Username and Domain")
email=input("Enter you email: ")
index=email.index("@")

username=email[:index]
domain=email[index+1:]

print(f"Your username is {username} and domain is {domain}")