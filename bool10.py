from math import sqrt
def main(a):
    return a >= 0 and sqrt(a)**2 == a
print (main(9))
print (main(15))
print (main(121))
print (main(111))