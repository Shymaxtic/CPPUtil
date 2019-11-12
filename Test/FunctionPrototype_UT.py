import unittest
import sys
sys.path.append("../CppUtil")
from FunctionPrototype import FunctionPrototype

class TestCppUtil(unittest.TestCase):
    def setUp(self):
        pass

    def test_Prototype_1(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1& arg1, const ArgType2& arg2) const")
        prototype = "const bool DoSomething(const ArgType1& arg1, const ArgType2& arg2) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)

    # def test_Prototype_2(self):
    #     testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const")
    #     prototype = "const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const"
    #     ret = testObj.CheckMatch(prototype)
    #     self.assertEqual(ret, True)        

    # def test_Prototype_3(self):
    #     testObj = FunctionPrototype("bool DoSomething(ArgType1 &arg1, ArgType2 &arg2)")
    #     prototype = "bool DoSomething(ArgType1 &arg1, ArgType2 &arg2)"
    #     ret = testObj.CheckMatch(prototype)
    #     self.assertEqual(ret, True) 

        
    # def test_Prototype_4(self):
    #     testObj = FunctionPrototype("bool DoSomeThing(ArgType1&, ArgType2&)")
    #     prototype = "bool DoSomeThing(ArgType1&, ArgType2&)"
    #     ret = testObj.CheckMatch(prototype)
    #     self.assertEqual(ret, True)         

    # def test_Prototype_5(self):
    #     testObj = FunctionPrototype("void DoSomeThing()")
    #     prototype = "void DoSomeThing()"
    #     ret = testObj.CheckMatch(prototype)
    #     self.assertEqual(ret, True)     
if  __name__ == '__main__':
    unittest.main()