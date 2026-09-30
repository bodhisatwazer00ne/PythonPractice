# assert keyword is used to assert tat the boolean expression is true. If it is false, an AssertionError exception is raised.
#it is used in unit testing etc. to check if the output of a function is as expected
#assert square(5)==25, "Test failed"  #if the expression is false, the message will be printed

def square(n):
    return n**2

def test_square():
    assert square(5)==25, "Test failed"
    
    try:
        assert square(-5)==25
        assert square(0)==0
        print("All tests passed")
    except AssertionError:
        print(f"Test faile")

def main(): 
    print(square(5))
    test_square()
    
if __name__ == "__main__":
    main()    