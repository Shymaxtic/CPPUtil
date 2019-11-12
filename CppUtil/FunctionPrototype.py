import re

class FunctionPrototype:
    mConstReturn = ""
    mReturnType = ""
    mFunctionName = ""
    mArgList = []
    mPrototype = ""
    def __init__(self, prototype: str):
        self.mPrototype = prototype
        self.__Parse()

    def CheckMatch(self, prototype: str):
        pass
    
    def __Parse(self):
        """Parse to get element from protype
        Ex: 
        const bool DoSomething(const ArgType1& arg1, const ArgType2& arg2) const
        const bool DoSomething(const ArgType1** arg1, const ArgType2** arg2) const
        const bool DoSomething(const ArgType1&& arg1, const ArgType2&& arg2) const
        const bool DoSomething(const ArgType1* const arg1, const ArgType2* const arg2) const
        const bool DoSomething(const ArgType1 * const, const ArgType2 * const) const
        bool DoSomething(ArgType1 &arg1, ArgType2 &arg2)
        bool DoSomeThing(ArgType1&, ArgType2&)
        void DoSomeThing()
       """
        ret = re.split('\(|\)', self.mPrototype)
    #    print(ret)
        functionNameSide = ret[0].split(" ")
        self.mFunctionName = functionNameSide[-1]
        self.mReturnType = functionNameSide[-2]
        if len(functionNameSide) == 3:
            self.mConstReturn = functionNameSide[-3]
        argListSide = ret[1].split(",")
        specificChar = ['**', '&&', '&', '*']
        for arg in argListSide:
            argInfo = []
            for ele in arg.split(" "):
                doNext = False
                for speChar in specificChar:
                    if speChar in ele:
                        for e in ele.split(speChar):
                            if e:
                                argInfo.append(e)
                        argInfo.append(speChar)
                        doNext = True
                        break
                if doNext == False and ele:
                    argInfo.append(ele)
            print(argInfo)                    
            if argInfo != []:
                self.mArgList.append(argInfo)                        
            
    
        print("Parsed:{} {} {}".format(self.mConstReturn, self.mReturnType, self.mFunctionName))
        # print("Arguments:", self.mArgList)
        for arg in self.mArgList:
            print(arg)


       