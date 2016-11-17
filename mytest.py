from functools import reduce

input = [[1,2,3,4],[2,3,4,5],[1,2]]

# output should be [2]

#print(reduce(lambda x,y:[i for i in x for j in y if i == j], input))
'''
def merge(a,b):
    bigger = len(a) if len(a)>len(b) else len(b)
    acount,bcount = 0,0

    for i in range(len(a)+len(b)):
        if(acount == len(a)):
            yield b[bcount]
            bcount += 1
        elif (bcount == len(b)):
            yield a[acount]
            acount += 1
        elif a[acount] < b[bcount]:
            yield a[acount]
            acount += 1
        else:
            yield b[bcount]
            bcount += 1
        #print('After iter')

        for i in merge([1,5,10],[2,3,4,5,6]):
    print (i)
'''

somelist = [1,2,3]

somelist[2] = 10
somelist[10] = 100

for i in somelist:
    print(i)




