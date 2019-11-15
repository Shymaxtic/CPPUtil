# Copyright (C) 2019 Shymaxtic
# 
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
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1& arg1, const ArgType2& arg2) const")
        prototype = "const bool DoSomething(const ArgType1& arg1, const ArgType2& arg2) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)

    def test_Prototype_2(self):
        testObj = FunctionPrototype("const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const")
        prototype = "const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)        

    def test_Prototype_3(self):
        testObj = FunctionPrototype("bool DoSomething(ArgType1 &arg1, ArgType2 &arg2)")
        prototype = "bool DoSomething(ArgType1 &arg1, ArgType2 &arg2)"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True) 

        
    def test_Prototype_4(self):
        testObj = FunctionPrototype("bool DoSomeThing(ArgType1&, ArgType2&)")
        prototype = "bool DoSomeThing(ArgType1&, ArgType2&)"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)         

    def test_Prototype_5(self):
        testObj = FunctionPrototype("void DoSomeThing()")
        prototype = "void DoSomeThing()"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)  

    def test_Prototype_6(self):
        testObj = FunctionPrototype("void DoSomeThing(ArgType1, ArgType2)")
        prototype = "void DoSomeThing(ArgType1, ArgType2)"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)  

    def test_Prototype_7(self):
        testObj = FunctionPrototype("void DoSomeThing(ArgType1 * arg1, ArgType2 * arg2)")
        prototype = "void DoSomeThing(ArgType1 * arg1, ArgType2 * arg2)"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)                          

    def test_Prototype_8(self):
        testObj = FunctionPrototype("void NamepSpace::DoSomeThing(NamepSpace::ArgType1 * arg1, NamepSpace::ArgType2 * arg2)")
        prototype = "void NamepSpace::DoSomeThing(NamepSpace::ArgType1 * arg1, NamepSpace::ArgType2 * arg2)"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)  

if  __name__ == '__main__':
    unittest.main()