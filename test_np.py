# -*- coding: utf-8 -*-
import numpy as np

def roots2poly():
    pol1 = np.poly([-1, 1, 1, 10])
    print pol1
    
def basicArrayOps():
    a = np.array([2, 4, 3], float)
    print a
    print 'Array sum: ', a.sum()
    print 'Array product: ', a.prod()
    
    print '------------------------------------------------------'
    print 'Computation of statistical quantities in array dataset'
    a = np.array([2, 1, 9], float)
    print a
    print 'Mean (average): ', a.mean()
    print 'Variance: ', a.var()
    print 'Std. deviation: ', a.std()
    print 'min value: ', a.min()
    print 'max value: ', a.max()
    print 'min value array index: ', a.argmin()
    print 'max value array index: ', a.argmax()
    
    print ''
    print sorted(a)
    print a
    a.sort()
    print a

    print 'Extraccion de valores únicos de un array'
    a = np.array([7, 3, 4, 5, 3, 2, 8, 2 ,7, 3])
    print a
    print np.unique(a)
    
    
# Mathematical constants in numpy
print 'pi value: ', np.pi
print 'e value: ', np.e

# test functions numpy
# Given a set of roots, show the polynomial coefficients
#roots2poly()

# Basic array operations 
basicArrayOps()
