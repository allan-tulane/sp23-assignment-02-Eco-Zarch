"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
    # pad with leading 0 if not even number of bits
    x_vec, y_vec = pad(x.binary_vec,y.binary_vec)
    n = max(len(x_vec), len(y_vec))

    # base case
    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return x.decimal_val * y.decimal_val

    # split x, y into high and low halves
    a, b = split_number(x_vec)
    c, d = split_number(y_vec)

    # recursive steps
    ac = BinaryNumber(subquadratic_multiply(a, c))
    bd = BinaryNumber(subquadratic_multiply(b, d))
   
    ad_bc = bit_shift(BinaryNumber(subquadratic_multiply(BinaryNumber(a.decimal_val + b.decimal_val), BinaryNumber(c.decimal_val + d.decimal_val))), n//2).decimal_val
    ac = bit_shift(ac, n).decimal_val - bit_shift(ac, n//2).decimal_val
    bd = bd.decimal_val - bit_shift(bd ,n//2).decimal_val

    # combine results
    return ad_bc + ac + bd
   
    


## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(3), BinaryNumber(16000)) == 3*16000
    assert subquadratic_multiply(BinaryNumber(110000), BinaryNumber(40)) == 110000*40

def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000

    
   
test_multiply()




