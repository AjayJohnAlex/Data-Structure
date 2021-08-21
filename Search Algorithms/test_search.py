import unittest
import Searches
import numpy as np

class Test_searches(unittest.TestCase):
    
    @classmethod
    def setUpclasses(cls):
        print("Setting up the class instances")
        
    @classmethod
    def tearDownclasses(cls):
        print("Setting Tear down classes")
    
    def setUp(self):
        self.array_list = np.arange(20)

    def tearDown(self):
        pass

    def test_linear_search(self):
        
        target = 9    
        self.assertEqual(Searches.linear_search(self.array_list,target),f"Located target at index: 9 ")
        
        target = 16
        self.assertEqual(Searches.linear_search(self.array_list,target),f"Located target at index: 16 ")  
              
        target = 25
        self.assertEqual(Searches.linear_search(self.array_list,target),f"Target not in list")
        
    def test_binary_search(self):
        
        target = 9    
        self.assertEqual(Searches.binary_search(self.array_list,target),f"Located target at index: 9 ")
        
        target = 16
        self.assertEqual(Searches.binary_search(self.array_list,target),f"Located target at index: 16 ")  
              
        target = 25
        self.assertEqual(Searches.binary_search(self.array_list,target),f"Target not in list")
        
    def test_recursive_binary_search(self):
        
        target = 9    
        self.assertEqual(Searches.recursion_binary_search(self.array_list,target),"Target found in the list")
        
        target = 16
        self.assertEqual(Searches.recursion_binary_search(self.array_list,target),"Target found in the list")  
              
        target = 25
        self.assertEqual(Searches.recursion_binary_search(self.array_list,target),f"Target not in list")
        


if __name__ == '__main__':
    unittest.main()



