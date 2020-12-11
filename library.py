n = int(input())
list = []
list1 = []
import math
for i in range(0,n):
    b = int(input())
    c = math.sqrt(b)
    c = str(c)
    list1 = c.split('.')
    adade_sahih = len(list1[0])
    tedad = adade_sahih + 5
    if len(c) > 5:
        d = c[:tedad]
        list.append(d)
    elif len(c) == 3 or len(c) == 4 or len(c) == 5:
        d = c + '000'
        list.append(d)
for i in list:
    print(i)





        
        

    

