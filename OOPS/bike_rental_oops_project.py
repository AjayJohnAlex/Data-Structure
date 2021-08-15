'''
A Bike Rental System
A full fledged bike rental system implemented in Python using object oriented programming.

Customers can
    1.See available bikes on the shop
    2.Rent bikes on hourly basis $5 per hour.
    3.Rent bikes on daily basis $20 per day.
    4.Rent bikes on weekly basis $60 per week.
    5.Family Rental, a promotion that can include from 3 to 5 Rentals (of any type) with 
        a discount of 30% of the total price

The bike rental shop can

    1.issue a bill when customer decides to return the bike.
    2.display available inventory
    3.take requests on hourly, daily and weekly basis by cross verifying stock
    
For simplicity we assume that
    1.Any customer requests rentals of only one type i.e hourly, monthly or weekly
    2.Is free to chose the number of bikes he/she wants
    3.Requested bikes should be less than available stock.
    
'''
import datetime

class Customers(object):
    
    total_available_bikes = 15
    
    def __init__(self, duration_type="hourly",duration_time=1, quantity=1):
        self.duration_type = str(duration_type).lower()
        self.duration_time = duration_time
        self.quantity = quantity
    

        
    def available_bike(self):
        return f"\nAvailable bikes in stock: {self.total_available_bikes}"
        

class BikeRental(Customers):
    
    def __init__(self,duration_type,duration_time,quantity):
        super().__init__(duration_type,duration_time,quantity)
        self.rate_dict = {"hourly":5,"daily":20, "weekly":60}

    def inventory_check(self):
        
        self.total_available_bikes -= self.quantity
        
        if self.total_available_bikes<=0:
            return True
        return False
    
    def Bill(self):
        
        dt = datetime.datetime.now()
        
        if not self.inventory_check():
                
            bill_amount = self.rate_dict[self.duration_type]*self.duration_time*self.quantity

            if (self.quantity>=3) and (self.quantity<=5):
                discounted_amount = bill_amount  - (0.3*bill_amount)
                final_bill_amount =  discounted_amount
            
            else:
                final_bill_amount =  bill_amount
            
            return f"\nBill Date: {dt}\nBill Amount: $ {float(final_bill_amount)}"
        
        return f"\nCannot Book {self.quantity} bikes."    
        
    

Cust_1 = BikeRental(duration_type="hourly",duration_time=1, quantity=1)
print(Cust_1.available_bike())
print(Cust_1.Bill())
print(Cust_1.available_bike())
Cust_2 = BikeRental(duration_type="hourly",duration_time=1, quantity=12) 
print(Cust_2.Bill())
print(Cust_2.available_bike())
Cust_3 = BikeRental(duration_type="hourly",duration_time=1, quantity=5) 
print(Cust_3.Bill())
print(Cust_3.available_bike())
    