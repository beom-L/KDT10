# 확장자 : Better Comments
## //  
## todo
## ?
## !
## *

arr = [3, 2, 4, 1, 3]
flag = [True, False, True, False, False]

x = []

for i in zip(arr,flag):
    if i[1]:    ## True라면
        for a in range(arr[0]*2):
            x.append(arr[0])
    else:
        for a in range(arr[0]):
            x.pop()
