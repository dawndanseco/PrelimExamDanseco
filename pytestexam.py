import math

def test_obese():
    weight = 80
    assert weight >=80
    
def test_temp():
    kelvin = 10
    convert = kelvin + 32
    fahrenheight = (convert * 9/5) + 32
    assert fahrenheight == 107

def test_rectangle():
    width = 5
    length = 5
    area = width * length
    assert area == 20

if __name__=='__main__':
    math.main()

#DANSECO, DAWN ALYSSA B.
#CPE41S6