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
from FunctionPrototype2 import FunctionPrototype2

class TestCppUtil(unittest.TestCase):
    def setUp(self):
        pass

    def test_Prototype_1(self):
        testObj = FunctionPrototype2("NameSpace::DoSomething(const NameSpace::ArgType1& , const NameSpace::ArgType2& )")
        prototype = "bool DoSomething(const ArgType1& arg1, const ArgType2& arg2)"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)

    def test_Prototype_2(self):
        testObj = FunctionPrototype2("NameSpace::NameSpace1::DoSomething(const NameSpace::NameSpace1::ArgType1& , const NameSpace::NameSpace1::ArgType2& )")
        prototype = "bool DoSomething(const ArgType1& arg1, const ArgType2& arg2)"
        ret = testObj.CheckMatch(prototype)
        self.assertEqual(ret, True)

if  __name__ == '__main__':
    unittest.main()