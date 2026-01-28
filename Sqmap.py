n1=[1,2,3]
n2=[4,5,6]

result=map(lambda x,y: x+y, n1,n2)
print('Addition of 2 lists: ',list(result))

num1=[1,2,3,4,5,6]
def sq(n):
    return n*n

result2=list(map(sq,num1))
print('The square of all numbers are: ',(result2))
