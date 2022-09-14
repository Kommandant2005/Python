'''a = tuple({1,3,5,7,9,2,4,6,8,0,3})
b = list((1,3,5,7,9,2,4,6,8,0,3))
c = set([1,3,5,7,9,2,4,6,8,0,3])
c.discard(3)
c.pop()
print(a)
print(b)
print(c)
'''
a={1,3,5,7,9,2,4,6,8,0,3}
b={1,3,4,6,8,4}
print(a & b)
print(a or b)
print(a-b)
