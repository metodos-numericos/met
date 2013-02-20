from numpy import *


def test2DArray():
    x = arange(0.,5.1)
    y = arange(0.,3.1)
    
    (X,Y) = meshgrid(x,y)
    print X
    
    
test2DArray() 