try:
import sys
fh = open("testfile", "r")
fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
finally:
    print("Error: can\'t find file or read data")

# raise an exception
x = 10
if x > 5:
    raise Exception('x should not exceed 5.  The value of x was: {}'.format(x))

# assert an error
assert('linux' in sys.platform), "This code runs on Linux Only"
