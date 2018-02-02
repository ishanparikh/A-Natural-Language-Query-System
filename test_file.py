toppings=[]
ch=input("Do you want to add toppings? (y/n)")
while(ch == 'y'):
    top=input(("Enter topping: "))
    toppings.append(top)
    ch = input("Do you want to add more toppings? (y/n)")

print("The toppings are:")
for item in toppings:
    print(item)


