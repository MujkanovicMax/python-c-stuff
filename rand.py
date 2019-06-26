import numpy as np

def fillarray(arr,out1=False,out2=False):

    mat = np.zeros((np.max(arr),len(arr)))
    mat2 = mat*1
    for i in range(len(arr)):
        mat[mat.shape[0]-arr[i]:mat.shape[0],i] = 1


    i = mat.shape[0]-1
    j= 0

    while i>=0:
      #  print("i = ",i,"\n")
        while j<len(arr)-1:
           # print("j = ",j,"\n")
            j=j+1
            if mat[i,j]<mat[i,j-1]:
                
                
                while j<len(arr) and mat[i,j] == 0:
                    mat2[i,j] = 5
                    
                    if j>=len(arr)-1:
                        
                       # print("reverse time")
                        while mat[i,j] == 0:
                            mat2[i,j] = 0
                            j=j-1
                        j=j+1
                        break

                    j=j+1
      
        i=i-1
        j=0
    if out1 == True:
        print(mat2,"\n\n")
    if out2 == True:
        print(mat2+mat,"\n\n")
    return np.sum(mat2)/5
count =0
r = 1000
z = 10
s = 15

arr = np.random.randint(z,size=s)

fillarray(arr,out1=True,out2=True)








