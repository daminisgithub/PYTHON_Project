class Bike:
    print("\n  **WELCOME** \nTo Bike rental Department")
    def __init__(self,a):
    
        self.a=a
    def display_quantity(self):
        print("THE BIKES AVAILABLE IS:-",self.a)
    def rental(self,q):
        print("THE PRICE FOR PER BIKE IS :-",100)
        print("THE PRICE FOR GIVEN QUANTITY:-",q*100)
        print("NOW AVAILABILITY IS :-",self.a-q)
    


while True:
    b=Bike(201)
    c=(int(input("PRESS\n 1.Display Quantity of Bike's\n 2.For Rent\n 3.Exit\n")))
    if c==1:
        b.display_quantity()
    elif c==2:
        d=int(input("Enter a Quantity:-"))
        if d<0 :
            print("PLS \n Enter a positive Valid Quantity")
        elif d>201:
            print("OOPS!!AVAILABITY IS : 201 only\npls Enter a quanty within availabilty")
        else:
           b.rental(d)
    else:
        c==3
        print("Thanks!FOR VISITING\nPLS DO COME AGAIN")
        break
      
