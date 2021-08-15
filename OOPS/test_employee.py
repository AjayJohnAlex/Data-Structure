import unittest
from Employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):
    
    '''In case we want to run a function before and after the entire the test cases:
    like build a Db connection till the test cases are running. Then we can create class methods for this'''
    
    @classmethod
    def setUpClass(self):
        print("Set Up Class is being executed \n")
        
    @classmethod
    def tearDownClass(self):
        print("Tear Down Class is being executed\n")
    
    '''as the object creation is repetative in each test case we can use setUp &
    tearDown to add & remove such code lines'''
    
    def setUp(self):
        print("\nSetting up class objects")
        self.Emp_1 = Employee("Ajay", "Alex",100)
        self.Emp_2 = Employee("Asha", "Alex",200)        
    
    def tearDown(self):
        print("Tearing Down Class objects\n")
        pass
    
    def test_email(self):
        print("Testing email functionality")
        self.assertEqual(self.Emp_1.email,"Ajay.Alex@gmail.com")
        self.assertEqual(self.Emp_2.email,"Asha.Alex@gmail.com")
        
        self.Emp_1.first = "John"
        self.Emp_2.last  = "Mary"
        
        self.assertEqual(self.Emp_1.email,"John.Alex@gmail.com")
        self.assertEqual(self.Emp_2.email,"Asha.Mary@gmail.com")
    
    
    def test_fullname(self):
        print("Testing full name functionality")
        
        self.assertEqual(self.Emp_1.full_name,"Ajay Alex")
        self.assertEqual(self.Emp_2.full_name,"Asha Alex")
        
        self.Emp_1.first = "John"
        self.Emp_2.last  = "Mary"
        
        self.assertEqual(self.Emp_1.full_name,"John Alex")
        self.assertEqual(self.Emp_2.full_name,"Asha Mary")        

    def test_pay_raise(self):
        print("Testing pay raise functionality")
        
        self.assertEqual(self.Emp_1.pay_raise(),110.00)
        self.assertEqual(self.Emp_2.pay_raise(),220.00)

    def test_request_method(self):
        '''Using mocks patch to check if the requests module is sending back the results as expected'''
        
        print("testing the request method")
        self.Emp_2.last  = "Mary"
        
        with patch('Employee.requests.get') as mock_req:
            
            mock_req.return_value.ok = True
            # mock_req.return_value.text  = "Success"
            
            schedule = self.Emp_1.request_method("July")
            mock_req.assert_called_with("https://www.google.com/search?q=Alex/July")
            # self.assertEqual(schedule,"Success")

            
            mock_req.return_value.ok = False
            
            schedule = self.Emp_2.request_method("August")
            mock_req.assert_called_with("https://www.google.com/search?q=Mary/August")
            self.assertEqual(schedule,"Bad Request !")
            
            
        pass

if __name__ == "__main__":
    
    unittest.main()