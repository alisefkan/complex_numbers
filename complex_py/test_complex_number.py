from complex_number import ComplexNumber
from math import pi

def test_eq_true():
    n1 = ComplexNumber(1,1)
    n2 = ComplexNumber(1,1)
    assert n1==n2

def test_eq_true_with_float():
    n1 = ComplexNumber(1,0)
    n2 = 1
    assert n1==n2

def test_eq_false():
    n1 = ComplexNumber(1,1)
    n2 = ComplexNumber(1,2)
    n3 = ComplexNumber(2,1)
    n4 = ComplexNumber(2,2)
    assert not n1 == n2
    assert not n1 == n3
    assert not n2 == n3
    assert not n1 == n4

def test_eq_false_with_float():
    n1 = ComplexNumber(1,0)
    n2 = 2
    assert not n1==n2    

def test_complex_add_cartesian():
    n1 = ComplexNumber(3,4)
    n2 = ComplexNumber(1,1)
    n3 = ComplexNumber(-1,-2)
    expected = ComplexNumber(4,5)
    assert expected == (n1+n2)
    assert not n3 == (n1+n2)

def test_complex_add_polar():
    n1 = ComplexNumber(1,pi/2,'polar')
    n2 = ComplexNumber(1,0,'polar')
    n3 = ComplexNumber(1,-1)
    expected = ComplexNumber(1,1)
    assert expected == (n1+n2)
    assert not n3 == (n1+n2)

def test_complex_sub_cartesian():
    n1 = ComplexNumber(3,4)
    n2 = ComplexNumber(1,1)
    n3 = ComplexNumber(5,2)
    expected = ComplexNumber(2,3)
    assert expected == (n1-n2)
    assert not n3 == (n1-n2)

def test_complex_sub_polar():
    n1 = ComplexNumber(1,pi/2,'polar')
    n2 = ComplexNumber(1,0,'polar')
    n3 = ComplexNumber(1,-1)
    expected = ComplexNumber(-1,1)
    assert expected == (n1-n2)
    assert not n3 == (n1-n2)

def test_complex_div_cartesian():
    n1 = ComplexNumber(6,8)
    n2 = ComplexNumber(3,4)
    n3 = ComplexNumber(2,3)
    expected = ComplexNumber(2,0)
    assert expected == (n1/n2)
    assert not n3 == (n1/n2)

def test_complex_div_polar():
    n1 = ComplexNumber(2,pi,'polar')
    n2 = ComplexNumber(1,3*pi/2,'polar')
    n3 = ComplexNumber(1,-1)
    expected = ComplexNumber(-1,1)
    assert expected == (n1-n2)
    assert not n3 == (n1-n2)
