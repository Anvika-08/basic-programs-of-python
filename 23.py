list=['anny',22,7,'pez',78,'den',5.7]

slist=[]
ilist = []
flist =[]

for i in range(len(list)):
    if type(list[i]) ==str:
        slist.append(list[i])
    elif type(list[i]) ==int:
        ilist.append(list[i])
    elif type(list[i]) ==float:
        flist.append(list[i])

print(slist)
print(ilist)
print(flist)
