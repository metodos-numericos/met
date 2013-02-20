import numpy as np

# input z, p(x)
# output p(z)

def calhorner(z, pol):
    x = pol
    b = x[x.size-1]
    n = x.size-1
    
    while n > 0:
        n = n -1 
        b = x[n] + z * b
        
    return  b        

def test_calhorner():
    print calhorner(0, np.array([-1, 5, 2, 3])) == -1
    print calhorner(1, np.array([-1, 5, 2, 3])) == 9
    print calhorner(2, np.array([-1, 5, 2, 3])) == 41
    print calhorner(3, np.array([-1, 5, 2, 3])) == 113
    print calhorner(4, np.array([-1, 5, 2, 3])) == 243
    print calhorner(5, np.array([-1, 5, 2, 3])) == 449
    print calhorner(6, np.array([-1, 5, 2, 3])) == 749

if __name__ == '__main__':
    test_calhorner()
    

    