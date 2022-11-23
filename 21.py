x=[[2,16,9],
   [5,6,18],
   [6,3,11]]
y=[[17,7,12],
   [16,5,18],
   [12,3,13]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]

for r in result:
    print(r)
