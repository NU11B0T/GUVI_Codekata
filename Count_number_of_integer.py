a=[1,2,3,4,57,88,2,"a",'as']
count=0
for i in a:
    if isinstance(i,int)== True:
        count+=1


print(count)