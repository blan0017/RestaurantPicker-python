import random

DeliveryList = ['Jimmy Johns','Erberts and Gerberts','Southern BBQ','Pizza','Pita Pit','Green Mill']

PickupList = ['Southern BBQ','Noodles','Panda','Smash Burger','Chipotle' , 'Leann Chins']

def pickFoodDelivery():
    print((DeliveryList[random.randint(0,len(DeliveryList)-1)]) + ' can be delivered!')

def pickFoodPickup():
    print((PickupList[random.randint(0,len(PickupList)-1)]) + ' can be picked up!')
    
    
while True:
    print('''
          
          [1] - We Want Delivery 
          [2] - We Want to Pick Up
          [3] - Exit
          
          ''')
    selection = input('Please Select an Option: ')
    
    if selection == '1':
        pickFoodDelivery()
    elif selection  == '2':
        pickFoodPickup()
    elif selection == '3':
        break
    else:
          print('\nError: Please select one of the options above')
     