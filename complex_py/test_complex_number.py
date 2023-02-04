from complex_number import ComplexNumber
from math import pi,sqrt
import pytest

def test_complex():
    n1 = ComplexNumber(2,2)
    n2 = ComplexNumber(2*sqrt(2),pi/4,'polar')
    assert n1.real == 2
    assert n1.img == 2
    assert n1.abs == 2*sqrt(2)
    assert n1.phase == pi/4
    assert abs(n1.real - n2.real) < 1e-12
    assert abs(n1.img - n2.img) < 1e-12
    assert abs(n1.abs - n2.abs) < 1e-12
    assert abs(n1.phase - n2.phase) < 1e-12

def test_eq():
    n1 = ComplexNumber(1,1)
    n2 = ComplexNumber(1,1)
    assert n1==n2


    n1 = ComplexNumber(1,0)
    n2 = 1
    assert n1==n2


    n1 = ComplexNumber(1,1)
    n2 = ComplexNumber(1,2)
    n3 = ComplexNumber(2,1)
    n4 = ComplexNumber(2,2)
    assert not n1 == n2
    assert not n1 == n3
    assert not n2 == n3
    assert not n1 == n4


    n1 = ComplexNumber(1.5,0)
    n2 = 2
    assert not n1==n2    

def test_complex_add():
    n1 = ComplexNumber(3,4)
    n2 = ComplexNumber(1,1)
    n3 = ComplexNumber(-1,-2)
    expected = ComplexNumber(4,5)
    assert expected == (n1+n2)
    assert not n3 == (n1+n2)

    n1 = ComplexNumber(1,pi/2,'polar')
    n2 = ComplexNumber(1,0,'polar')
    n3 = ComplexNumber(1,-1)
    expected = ComplexNumber(1,1)
    assert expected == (n1+n2)
    assert not n3 == (n1+n2)

def test_complex_sub():
    n1 = ComplexNumber(3,4)
    n2 = ComplexNumber(1,1)
    n3 = ComplexNumber(5.123,2)
    expected = ComplexNumber(2,3)
    assert expected == (n1-n2)
    assert not n3 == (n1-n2)

    n1 = ComplexNumber(1,pi/2,'polar')
    n2 = ComplexNumber(1,0,'polar')
    n3 = ComplexNumber(1,-1)
    expected = ComplexNumber(-1,1)
    assert expected == (n1-n2)
    assert not n3 == (n1-n2)

def test_complex_div():
    n1 = ComplexNumber(6,8)
    n2 = ComplexNumber(3,4)
    n3 = ComplexNumber(2,3)
    expected = ComplexNumber(2,0)
    assert expected == (n1/n2)
    assert not n3 == (n1/n2)

    n1 = ComplexNumber(2,pi,'polar')
    n2 = ComplexNumber(1,3*pi/4,'polar')
    n3 = ComplexNumber(1,-1)
    expected = ComplexNumber(sqrt(2),sqrt(2))
    assert expected == (n1/n2)
    assert not n3 == (n1/n2)
    with pytest.raises(ZeroDivisionError):
        n1 = ComplexNumber(123,789)
        n2 = ComplexNumber(0,0)
        n3 = n1/n2

def test_complex_mul():
    n1 = ComplexNumber(1,1)
    n2 = ComplexNumber(-1,1)
    n3 = ComplexNumber(123.123,532)
    expected = ComplexNumber(2,pi,'polar')

    assert expected == (n1*n2)
    assert not n3 == (n1*n2)

    n1 = ComplexNumber(2,pi,'polar')
    n2 = ComplexNumber(1,3*pi/4,'polar')

    expected = ComplexNumber(sqrt(2),-sqrt(2))
    assert expected == (n1*n2)


def test_complex_pow():
    n1 = ComplexNumber(6,0.5,'polar')
    excepted = ComplexNumber(36,1,'polar')
    assert excepted == n1**2

    n1 = ComplexNumber(2,2)
    excepted = ComplexNumber(-64,0)
    assert excepted == n1**4

def test_complex_conjugation():
    n1 = ComplexNumber(1,1)
    excepted = ComplexNumber(1,-1)
    assert excepted == ~n1

    n1 = ComplexNumber(5,2,'polar')
    excepted = ComplexNumber(5,2*pi-2,'polar')
    assert excepted == ~n1

def test_complex_errors():
    with pytest.raises(AssertionError):
        n1=ComplexNumber('1','2')
    with pytest.raises(AssertionError):
        n2=ComplexNumber(1,2,'new_coordinates')
    with pytest.raises(TypeError):
        n3=ComplexNumber(1,2) + 'test'
    with pytest.raises(TypeError):
        n3=ComplexNumber(1,2) / 'test'
    with pytest.raises(TypeError):
        n3=ComplexNumber(1,2) * 'test'
    with pytest.raises(TypeError):
        n3=ComplexNumber(1,2) - 'test'
    with pytest.raises(TypeError):
        n3=ComplexNumber(1,2) ** 'test'   