import random

DeliveryList = ['Jimmy Johns','Erberts and Gerberts','Southern BBQ','Pizza','Pita Pit','Green Mill']

PickupList = ['Southern BBQ','Noodles','Panda','Smash Burger','Chipotle']

def pickFoodDelivery():
    print(DeliveryList[random.randint(0,5)])

def pickFoodPickup():
    print(PickupList[random.randint(0,4)])
    
    
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
     