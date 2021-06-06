print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
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
Unicorn Tears """)

i=0
orderArr=[]
menu=['wings','cookies','spring rolls','salmon','steak','meat tornado','a literal garden','ice cream','cake','pie','coffee','tea','unicorn tears']
while i>=0 :
    order= input("""
    ***********************************
    ** What would you like to order? **
    ***********************************
    > """)
    if order.lower() in menu:
        i+=1
        print('** %d order of %s have been added to your meal **' %(i,order))
        orderArr.append(order)
    elif order == 'quit':
        break      
    else:
        print('** Your Order is not in the menu! Please choose from the above menu **')
        
print('your orders are ')
for j in range(0,len(orderArr)) :
    print(orderArr[j])
    

    
