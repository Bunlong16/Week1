years = int(input("Enter your yesrs Number is : "))
sex= str(input("Enter your sex is : "))
print(years)
print(sex)
if sex == 'women' :
    if years <= 18 :
        print("You don't can come in ")

    elif years == 19 :
        print("you cam come in ")

    else:
        print("Free you gat a drink")
        
else:
    if years <= 18 :
        print("You don't can come in ")

    elif years == 19 :
        print("you cam come in ")

    else:
        print("Free you gat a drink")        