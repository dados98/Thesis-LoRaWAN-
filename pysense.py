from pycoproc import Pycoproc


_version_ = '1.4.0'

class Pysense(Pycoproc):

    def _init_(self,i2c=None,sda='P22', scl='P21'):
        Pycoproc._init_(self,i2c,sda,scl)
