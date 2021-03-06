# 
# Copyright (C) 2019 Shymaxtic
# This file is part of CPPUtil.
# 
# CPPUtil is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# CPPUtil is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with CPPUtil.  If not, see <http://www.gnu.org/licenses/>.

import unittest
import sys
sys.path.append("../CppUtil")
from FunctionPrototype import FunctionPrototype

class TestCppUtil(unittest.TestCase):
    def setUp(self):
        pass

    def test_Prototype_1(self):
        testObj = FunctionPrototype("const bool DoSomething(const NameSpace::ArgType1& arg1, const NameSpace::ArgType2& arg2) const")
        prototype = "const bool DoSomething(const NameSpace::ArgType1& arg1, const NameSpace::ArgType2& arg2) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)

    def test_Prototype_2(self):
        testObj = FunctionPrototype("const bool DoSomething(const NameSpace::NameSpace1::ArgType1& arg1, const NameSpace::NameSpace1::ArgType2& arg2) const")
        prototype = "const bool DoSomething(const NameSpace::NameSpace1::ArgType1&, const NameSpace::NameSpace1::ArgType2&) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)        

    def test_Prototype_3(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1& arg1, const ArgType2& arg2) const")
        prototype = "const bool DoSomething(const ArgType1 &, const ArgType2 &) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)          

    def test_Prototype_4(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1& arg1, const ArgType2& arg2) const")
        prototype = "const bool DoSomething(const ArgType1 &arg1, const ArgType2 &arg2) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)  

    def test_Prototype_5(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1& arg1, const ArgType2& arg2) const")
        prototype = "const bool DoSomething(const ArgType1&arg1,const ArgType2&arg2) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)          
        
    def test_Prototype_6(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1& arg1, const ArgType2& arg2) const")
        prototype = "const bool DoSomething(const ArgType1 &&arg1, const ArgType2 &&arg2) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, False)  

    def test_Prototype_7(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1& arg1, const ArgType2& arg2) const")
        prototype = "const bool DoSomething(const ArgType1&& arg1, const ArgType2&& arg1) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, False)         

    def test_Prototype_8(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1& arg1, const ArgType2& arg2) const")
        prototype = "const bool DoSomething(const ArgType1** arg1, const ArgType2** arg1) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, False)  

    def test_Prototype_9(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1& arg1, const ArgType2& arg2) const")
        prototype = "const bool DoSomething(const ArgType1* arg1, const ArgType2* arg1) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, False)  

    def test_Prototype_10(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const")
        prototype = "const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)     

    def test_Prototype_11(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const")
        prototype = "const bool DoSomething(const ArgType1* const, const ArgType2* const) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)              

    def test_Prototype_12(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const")
        prototype = "const bool DoSomething(const ArgType1*const, const ArgType2*const) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)  

    def test_Prototype_13(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const")
        prototype = "const bool DoSomething(const ArgType1 * const a, const ArgType2 * const b) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)        

    def test_Prototype_14(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const")
        prototype = "const bool DoSomething(const ArgType1 *const a, const ArgType2 *const b) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)     

    def test_Prototype_15(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const")
        prototype = "const bool DoSomething(const ArgType1 const a, const ArgType2 const b) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, False)   

    def test_Prototype_16(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const")
        prototype = "bool DoSomething(const ArgType1* const a, const ArgType2* const b)"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, False)   

    def test_Prototype_17(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const")
        prototype = "const bool DoSomething(const ArgType1* const a, const ArgType2* const b)"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, False)        

    def test_Prototype_18(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const std::string& arg2) const")
        prototype = "const bool DoSomething(const ArgType1* const a, const std::__cxx11::string& b) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)      

    def test_Prototype_19(self):
        testObj = FunctionPrototype("const bool DoSomething(std::vector& arg1, const std::string& arg2) const")
        prototype = "const bool DoSomething(std::__cxx11::vector& a, const std::__cxx11::string& b) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)        

    def test_Prototype_20(self):
        testObj = FunctionPrototype("const bool DoSomething(std::__cxx11::vector& arg1, const std::__cxx11::string& arg2) const")
        prototype = "const bool DoSomething(std::vector& a, const std::string& b) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)                     

    def test_Prototype_21(self):
        testObj = FunctionPrototype("void NameSpace::DoSomeThing(NameSpace::ArgType1 a, NameSpace::ArgType2 b)")
        prototype = "void NameSpace::DoSomeThing(NameSpace::ArgType1, NameSpace::ArgType2)"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)  

    def test_Prototype_22(self):
        testObj = FunctionPrototype("void DoSomeThing(ArgType1 a)")
        prototype = "void DoSomeThing(ArgType1)"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)       

    def test_Prototype_23(self):
        testObj = FunctionPrototype("void DoSomeThing(void)")
        prototype = "void DoSomeThing()"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)     

    def test_Prototype_24(self):
        testObj = FunctionPrototype("void DoSomeThing()")
        prototype = "void DoSomeThing(void)"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)     

    def test_Prototype_25(self):
        testObj = FunctionPrototype("void DoSomeThing() const")
        prototype = "void DoSomeThing(void) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)   

    def test_Prototype_26(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1** const arg1, const ArgType2** const arg2) const")
        prototype = "const bool DoSomething(const ArgType1** const arg1, const ArgType2** const arg2) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)     

    def test_Prototype_27(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1** const arg1, const ArgType2** const arg2) const")
        prototype = "const bool DoSomething(const ArgType1** const, const ArgType2** const) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)              

    def test_Prototype_28(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1** const arg1, const ArgType2** const arg2) const")
        prototype = "const bool DoSomething(const ArgType1**const, const ArgType2**const) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)  

    def test_Prototype_29(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1** const arg1, const ArgType2** const arg2) const")
        prototype = "const bool DoSomething(const ArgType1 ** const a, const ArgType2 ** const b) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)        

    def test_Prototype_30(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1** const arg1, const ArgType2** const arg2) const")
        prototype = "const bool DoSomething(const ArgType1 **const a, const ArgType2 **const b) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)            

    def test_Prototype_31(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const")
        prototype = "const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)     

    def test_Prototype_32(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const")
        prototype = "const bool DoSomething(const ArgType1* const, const ArgType2* const) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)              

    def test_Prototype_33(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const")
        prototype = "const bool DoSomething(const ArgType1*const, const ArgType2*const) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)  

    def test_Prototype_34(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const")
        prototype = "const bool DoSomething(const ArgType1 * const a, const ArgType2 * const b) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)        

    def test_Prototype_35(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const")
        prototype = "const bool DoSomething(const ArgType1 *const a, const ArgType2 *const b) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)   

    # TODO: fix bug here.
    def test_Prototype_36(self):
        testObj = FunctionPrototype("DoSomething(const ArgType1* const arg1, const ArgType2* const arg2)")
        prototype = "const bool DoSomething(const ArgType1 *const a, const ArgType2 *const b) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)                                      

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


    # def test_Prototype_7(self):
    #     testObj = FunctionPrototype("void DoSomeThing(ArgType1 * arg1, ArgType2 * arg2)")
    #     prototype = "void DoSomeThing(ArgType1 * arg1, ArgType2 * arg2)"
    #     ret = testObj.CheckMatch(prototype)
    #     self.assertEqual(ret, True)                          

    # def test_Prototype_8(self):
    #     testObj = FunctionPrototype("void NamepSpace::DoSomeThing(NamepSpace::ArgType1 * arg1, NamepSpace::ArgType2 * arg2)")
    #     prototype = "void NamepSpace::DoSomeThing(NamepSpace::ArgType1 * arg1, NamepSpace::ArgType2 * arg2)"
    #     ret = testObj.CheckMatch(prototype)
    #     self.assertEqual(ret, True)  

if  __name__ == '__main__':
    unittest.main()