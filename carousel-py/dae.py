
import casadi as C

class Dae():
    def __init__(self):
        self._frozen = set()
        
        self._xNames = []
        self._zNames = []
        self._uNames = []
        self._pNames = []
        self._outputNames = []

        self._xDict = {}
        self._zDict = {}
        self._uDict = {}
        self._pDict = {}
        self._outputDict = {}

    def _freeze(self,msg):
        self._frozen.add(msg)

    def assertNotFrozen(self):
        if len(self._frozen) > 0:
            raise ValueError("can't perform this operation because Dae has been frozen by: "+str([n for n in self._frozen]))

    def assertUniqueName(self, name):
        allNames = self._xNames + self._zNames + self._uNames + self._pNames + self._outputNames
        if name in allNames:
            raise ValueError('name "'+name+'" is not unique')

    def _getVar(self,name,namelist,namedict):
        if isinstance(name,list):
            return [self._getVar(n,namelist,namedict) for n in name]
                
        assert(isinstance(name,str))

        if name not in namedict:
            raise KeyError(name+' is not in '+str(namelist))
        
        return namedict[name]

    def _addVar(self,name,namelist,namedict):
        self.assertNotFrozen()
        if isinstance(name,list):
            return [self._addVar(n,namelist,namedict) for n in name]

        assert(isinstance(name,str))
        
        if name in namedict:
            raise KeyError(name+' is already in in '+str(namelist))
        
        self.assertUniqueName(name)
        namelist.append(name)
        namedict[name] = C.ssym(name)
        return namedict[name]

    def addX(self,name):
        return self._addVar(name,self._xNames,self._xDict)

    def addZ(self,name):
        return self._addVar(name,self._zNames,self._zDict)

    def addU(self,name):
        return self._addVar(name,self._uNames,self._uDict)

    def addP(self,name):
        return self._addVar(name,self._pNames,self._pDict)
    
    def x(self,name):
        return self._getVar(name,self._xNames,self._xDict)

    def z(self,name):
        return self._getVar(name,self._zNames,self._zDict)

    def u(self,name):
        return self._getVar(name,self._uNames,self._uDict)

    def p(self,name):
        return self._getVar(name,self._pNames,self._pDict)

    def output(self,name):
        return self._getVar(name,self._outputNames,self._outputDict)

    def xVec(self):
        self._freeze('xVec()')
        return C.veccat([self._xDict[n] for n in self._xNames])
    def zVec(self):
        self._freeze('zVec()')
        return C.veccat([self._zDict[n] for n in self._zNames])
    def uVec(self):
        self._freeze('uVec()')
        return C.veccat([self._uDict[n] for n in self._uNames])
    def pVec(self):
        self._freeze('pVec()')
        return C.veccat([self._pDict[n] for n in self._pNames])

    def addOutput(self,name,val):
#        print "adding output name: \""+name+"\", val: "+str(val)
        assert( isinstance(name, str) )
        assert( isinstance(val, C.SXMatrix) )
        if name in self._outputNames:
            raise ValueError('output name "'+name+'" is not unique')
        self._outputNames.append(name)
        self._outputDict[name] = val

    def outputsFun(self):
        self._freeze('outputsFun()')
        inputs = [self.xVec(),C.veccat([self.uVec(),self.pVec()])]
        outputs = [self._outputDict[n] for n in self._outputNames]
        fOutputs = C.SXFunction(inputs,outputs)
        fOutputs.setOption('name','fOutputs')
        return fOutputs


if __name__=='__main__':
    dae = Dae()
    print dae.xNames
    print dae.xDict
    dae.x('x')
    print dae.xNames
    print dae.xDict
    dae.x('y')
    print dae.xNames
    print dae.xDict