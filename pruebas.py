from numpy import *
from math import sqrt, pi
import es.era

def raizCuadrada():
    print 2.0*sqrt(10.0/pi)

def divisiones():
    x = divmod(+123, -45)
    print +123/-45, +123%-45, x
    print x[0]*-45+x[1]
    print 100+23, abs(-123), abs(+123)
    print pow(2,10), pow(-5,3), pow(5,0)

def formatearNumeros():
    print "%d %d" % (123, 1234567890)
    print "%5d %5d" % (123, 1234567890)

def puntoFlotante():
    print 6.0//1.5
    print +12.3/ --3.4, +12.3// --3.4, +12.3%--3.4, divmod(+12.3,--3.4)
    
    x = 100.0/7.0
    print "%.3f %.5e" % (x, x)
    print "%10.5f %20.3e" % (x, x)
    print "%.0f %.0e" % (x, x)
    
def exceptionalValues():
    print 1.0/0.0    
    
def simpleArrays():
    a = array([[1, 2], [3, 4]])
    b = array([5,6])
    print a
    print b
    
    print dot(a, b)
    a[0,1] = 7
    print a
    
    print a*a
    
if __name__ == '__main__':
    #raizCuadrada()
    #divisiones()
    #formatearNumeros()
    #puntoFlotante()
    #exceptionalValues()
    #simpleArrays()
    