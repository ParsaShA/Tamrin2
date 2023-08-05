lst = [1,2,3,'a',3,'a',2,4,9,3,32,2,2]
j = -1
for i in lst:
    j+=1
    key = lst[j]
    if key == lst[j+1]: 
         print(i)
         break