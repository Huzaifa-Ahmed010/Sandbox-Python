print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
bill = 0
if size == 's':
    bill += 15
elif size == 'm':
    bill +=  20
elif size == 'l':
    bill += 25
if pepperoni == 'y' and size == 's' and extra_cheese == 'y':
    bill += 2 + 1
    print(f"Your final bill is: ${bill}")
elif pepperoni == 'y' and size == 's' and extra_cheese == 'n':
    bill += 2
    print(f"Your final bill is: ${bill}")
elif pepperoni == 'n' and size == 's' and extra_cheese == 'y':
    bill += 1
    print(f"Your final bill is: ${bill}")
elif pepperoni == 'n' and size == 's' and extra_cheese == 'n':
    bill += 0
    print(f"Your final bill is: ${bill}")
#    For medium pizza.................
elif pepperoni == 'y' and size == 'm' and extra_cheese == 'y':
    bill += 2 + 1
    print(f"Your final bill is: ${bill}")
elif pepperoni == 'n' and size == 'm' and extra_cheese == 'y':
    bill += 1
    print(f"Your final bill is: ${bill}")
elif pepperoni == 'y' and size == 'm' and extra_cheese == 'n':
    bill += 2
    print(f"Your final bill is: ${bill}")
elif pepperoni == 'n' and size == 'm' and extra_cheese == 'n':
    bill += 0
    print(f"Your final bill is: ${bill}")
# for large pizza......................
elif pepperoni == 'y' and size == 'l' and extra_cheese == 'y':
    bill += 2 + 1
    print(f"Your final bill is: ${bill}")
elif pepperoni == 'n' and size == 'l' and extra_cheese == 'y':
    bill += 1
    print(f"Your final bill is: ${bill}")
elif pepperoni == 'y' and size == 'l' and extra_cheese == 'n':
    bill += 2
    print(f"Your final bill is: ${bill}")
elif pepperoni == 'n' and size == 'l' and extra_cheese == 'n':
    bill += 0
    print(f"Your final bill is: ${bill}")
else:
    print("You Entered wrong Input!!")