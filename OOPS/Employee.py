import requests


class Employee(object):
    
    raise_amount = 1.1
    
    def __init__(self,first, last, pay):
        self.first  = first
        self.last =last
        self.pay = pay
            
    @property
    def email(self):
        return self.first +"."+ self.last +"@gmail.com"

              
    @property  
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def pay_raise(self):
        
        return round(float(self.pay *self.raise_amount),2)
    
    
    def request_method(self,month):
        res = requests.get(f"https://www.google.com/search?q={self.last}/{month}")
        
        if res.ok:
            return res.text
        else:
            return "Bad Request !"