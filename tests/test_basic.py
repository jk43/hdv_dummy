from unittest import TestCase, main

from hdv_dummy import Dummy

class TestDummy(TestCase):
    
    def testMethod(self):
        
        dummy = Dummy()
        dummy.donot().returns().errors()
        
    def testClassVariable(self):
        
        dummy = Dummy()
        dummy.donot.returns.errors
        
    def testMethodWithClassVariable(self):
        
        dummy = Dummy()
        dummy.donot().returns().errors
        dummy.donot.returns().errors()
        

if __name__ == '__main__':
    main()




