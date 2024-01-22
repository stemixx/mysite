from django.test import TestCase

def function(num):
    def mult(num):
        return num*num
    output = mult(num)
    return output

# mult(3.14)