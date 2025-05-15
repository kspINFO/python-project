# python calculator

while True:

    opurator=input("Enter an operator(+,-,*,/):")
    num1=float(input("Enter the 1st number: "))
    num2=float(input("Emter the 2nd number: "))

    if opurator=="+":
        result=num1+num2
        print(round(result,3))
    elif opurator=='-':
        result=num1-num2
        print(round(result,3))
    elif opurator=='*':
        result=num1*num2 
        print(round(result,3))
    elif opurator=='/':
        result=num1/num2
        print(round(result,3))
    else:
        print(f"{opurator} this invalied opurator")