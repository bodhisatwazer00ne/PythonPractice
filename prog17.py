
import pytest


def square(n):
    return n**2

def test_square():
    assert square(5)==25
    
def test_str():
    with pytest.raises(TypeError):
        square("cat")    
   #pytest raises a type error when a string is passed to the square function, as it expects a number
    
#run using pytest prog18.py in terminal for testing     
#pytest is a testing framework for Python. It allows you to write test cases for your code and run them easily. 
# It provides a simple and easy-to-use interface for writing tests, and it can automatically discover and run tests in your codebase.