def main(a):
    return a >= 1 and isinstance(a, int)
print (main(4))
print (main(-2))
print (main(0))
print (main(3.4))
