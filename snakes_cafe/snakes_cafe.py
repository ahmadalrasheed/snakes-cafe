
print(""" **************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
""")
print('')
print('')

print("""Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
""")

print('')

print("""***********************************
** What would you like to order? **
***********************************
""")

Appetizers={
    "Wings":0,
    "Cookies":0,
    "Spring Rolls":0
}
Entrees={
    "Salmon":0,
    "Steak":0,
    "Meat Tornado":0,
    "A Literal Garden":0
}
Desserts={
    "Ice Cream":0,
    "Cake":0,
    "Pie":0
}
Drinks={
    "Coffee":0,
    "Tea":0,
    "Unicorn Tears":0  
}
user_order=input('>')
while(user_order != 'quit'):
    if(user_order in Appetizers.keys()):
        Appetizers[user_order]+=1
        print('')
        print(f'** {Appetizers[user_order]} order of {user_order} have been added to your meal **')
        print('')
        user_order=input('>')
    
    elif(user_order in Entrees.keys()):
        Entrees[user_order]+=1
        print('')
        print(f'** {Entrees[user_order]} order of {user_order} have been added to your meal **')
        print('')
        user_order=input('>')
    elif(user_order in Desserts.keys()):
            Desserts[user_order]+=1
            print('')
            print(f'** {Desserts[user_order]} order of {user_order} have been added to your meal **')
            print('')
            user_order=input('>')
    elif(user_order in Drinks.keys()):
            Drinks[user_order]+=1
            print('')
            print(f'** {Drinks[user_order]} order of {user_order} have been added to your meal **')
            print('')
            user_order=input('>')

    else:
        print('No such order in the menu ! please check the name of the order to be exactly the same name in the menu including capital letters')
        user_order=input('>')

