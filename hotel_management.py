menu= {
    'Pizza' : 12.95,
    'Coffee' : 4.95,
    'Brownie' : 6.45,
    'Fruits' : 2.60,
    'Salad' : 8.20,
}

print('Welcome to Cafeteria, What would you like to have?')
print('Pizza : 12.95,\nCoffee : 4.95,\nBrownie : 6.45,\nFruits : 2.60,\nSalad : 8.20,')

total= 0
def order ( item ):
    global total
    if item in menu :
        total= total + menu[item]
        print(f"Your order {item} has been added")
    else:
        print(f"Ordered item {item} is not available")
2
no_of_items= int(input('how many items you want to order - '))
for i in range(no_of_items):
    item1= input("Choose the items you want to order - ")
    order(item1)
    
print("Your order is finalized and the total is ", total)