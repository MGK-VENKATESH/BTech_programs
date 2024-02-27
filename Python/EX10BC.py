x=[[12,7,3],[4,5,6],[7,8,9]]
y=[[5,8,1,2],[6,7,3,0],[4,5,9,1]]
result=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j]+=x[i][k]*y[k][j]
for r in result:
    print(r)



#ex10b
import numpy as np
a=[[1,2,3],[3,4,5],[4,5,6]]
b=[[1,2,3],[3,4,5],[4,5,6]]
result=np.array(x)+np.array(y)
print(result)