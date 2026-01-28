zip1={1,2,3}
zip2={"a","b","c"}
zip3=list(zip(zip1,zip2))
print(zip3,'\n')

s1=[1,2,3,4,5]
s2=[6,7,8,9,0]
for x,y in zip(s1,s2[::-1]):
    print(x,y)