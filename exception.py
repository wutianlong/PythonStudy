# python2.7 exception.py

re = iter(range(10))

try:
    for i in range(100):
        print re.next()
except StopIteration:
    print 'except StopIteration'
finally:
    print 'finally process'

