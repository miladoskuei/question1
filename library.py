n = int(input())
list = []
import math
for i in range(0,n):
    b = int(input())
    c = math.sqrt(b)
    c = str(c)
    if len(c) > 5:
        d = c[:6]
        list.append(d)
    elif len(c) == 3:
        d = c + '000'
        list.append(d)
        
    
print(list)








        
        

    

