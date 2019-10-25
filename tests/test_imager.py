import pytest
from task1 import imager

def test_output():
    '''
    Test the output of the imager module to check if the output is a string
    '''
    assert(type(imager.main() == "str"))












