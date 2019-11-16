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


import re
D_ARGUMENT_REGEX = r'(const\s*)?[\w|\d|:{2}]+((\s*&{2}\s*)|(\s*&{1}\s*)|(\s*\*{2}(const)?\s*)|(\s*\*{1}\s*(const)?)|(\s+(const)?))'
D_ATUTO_STD = '__cxx11'
class FunctionPrototype:
    mConstReturn = ""
    mReturnType = ""
    mFunctionName = ""
    mArgList = []
    mPrototype = ""
    mSearcher = None
    def __init__(self, prototype: str):
        self.mConstReturn = ""
        self.mReturnType = ""
        self.mFunctionName = ""
        self.mArgList = []
        self.mPrototype = prototype
        self.mRegrexPrototype = ""
        self.mLastConst = ""
        self.mSearcher = None
        self.__Parse()

    def CheckMatch(self, prototype: str):
        # Preprocess, force only 1 space.
        prototype = re.sub(' +', ' ', prototype)
        ret = re.split(r'\(|\)', prototype)
        # Get argument info
        argListSide = ret[1]
        argInfoList = argListSide.split(',')
        searcher = re.compile(D_ARGUMENT_REGEX)
        # Remove argument variable.
        for arg in argInfoList:
            tmp = searcher.search(arg)
            if tmp:
                prototype = prototype.replace(tmp.string, tmp.group())
        # print("prototype=", prototype)
        return self.mSearcher.search(prototype) != None
        

    def __Parse(self):
        """Parse to get element from prototype
        Ex: 
        const bool DoSomething(const ArgType1& arg1, const ArgType2& arg2) const
        const     bool    DoSomething   (const ArgType1 &arg1, const ArgType2 &arg2     ) const
        const bool DoSomething(const ArgType1 &arg1, const ArgType2 &arg2) const
        const bool DoSomething(const ArgType1 & arg1, const ArgType2 & arg2) const
        const bool DoSomething(const ArgType1 * const arg1, const ArgType2 & arg2) const
        const bool DoSomething(const ArgType1 &, const ArgType2 &) const
        const bool DoSomething(const ArgType1&, const ArgType2&) const
        const bool DoSomething(const std::cxx11::string arg1)
        const bool DoSomething(const std::string arg1)
       """
        # Preprocess, force only 1 space.
        self.mPrototype = re.sub(' +', ' ', self.mPrototype)
        # print(self.mPrototype)
        sections = re.split(r'\(|\)', self.mPrototype)
        functionNameSide = sections[0]
        # print("functionNameSide=", functionNameSide)

        # Process for regex
        functionNameSide = functionNameSide.replace(' ', r'\s+')
        # print("functionNameSide=", functionNameSide)

        # Get argument info
        argListSide = sections[1]
        # In case (void) or ()
        if argListSide == 'void' or not argListSide:
            argListSide = '(void)?'
        else:
            argInfoList = argListSide.split(',')
            searcher = re.compile(D_ARGUMENT_REGEX)

            # Remove argument variable.
            for arg in argInfoList:
                tmp = searcher.search(arg)
                if tmp:
                    argListSide = argListSide.replace(tmp.string, tmp.group())

            # Process for ','. Remove space 
            argListSide = re.sub(r'\s*,\s*', ',', argListSide)

            # fix bug in case (ArgType1 arg1, ArgType2 arg2) -> ArgType1, ArgType2(space)
            argListSide = argListSide.rstrip()

            # Process for '&&'.
            argListSide = re.sub(r'\s*&{2}\s*', r'\\s-&{2}\\s-', argListSide)

            # Process for '&'.
            argListSide = re.sub(r'\s*&{1}\s*', r'\\s-&{1}\\s-', argListSide)

            # Process for '**'
            argListSide = re.sub(r'\s*\*{2}\s*', r'\\s-\\*{2}\\s-', argListSide) # dummy replace '-'

            # Process for '*'
            argListSide = re.sub(r'\s*\*{1}\s*', r'\\s-\\*{1}\\s-', argListSide) # dummy replace '-'

            # Process for regex
            argListSide = argListSide.replace(' ', r'\s+')
            argListSide = argListSide.replace(',', r'\s*,\s*')
            argListSide = argListSide.replace('-', r'*')

            # Process for auto generate std::__cxx
            if 'std::' in argListSide:
                if D_ATUTO_STD not in argListSide:
                    argListSide = argListSide.replace('std::', 'std::(' + D_ATUTO_STD + '::)?')
                else:
                    argListSide = argListSide.replace(D_ATUTO_STD + '::', '(' + D_ATUTO_STD + '::)?')
            

        # Construct regex.
        self.mRegrexPrototype = functionNameSide + r'\s*\(\s*' + argListSide + r'\s*\)\s*'
        if sections[2].strip() == 'const':
            self.mRegrexPrototype += sections[2].strip()
        # print("mRegrexPrototype=", self.mRegrexPrototype)
        self.mSearcher = re.compile(self.mRegrexPrototype)


       