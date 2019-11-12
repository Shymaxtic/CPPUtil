import unittest
import sys
sys.path.append("../CppUtil")
from FunctionPrototype import FunctionPrototype

testPrototype1 = "const bool GetResult(const ClassType&) const"
class TestCppUtil(unittest.TestCase):
    def setUp(self):
        pass

    def test_Prototype_1(self):
        testObj = FunctionPrototype(testPrototype1)
        prototype = "const bool GetResult(const ClassType&) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)

if  __name__ == '__main__':
    unittest.main()