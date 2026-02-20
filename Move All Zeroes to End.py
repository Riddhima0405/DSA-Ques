count=0
        for i in range (len(arr)):
            if arr[i]!=0:
                arr[i],arr[count]=arr[count],arr[i]
                count+=1
if __name__=="main":
    arr=[1,2,0,4,3,0,5,0]
    pushZerosToEnd(arr)
    for num in arr:
        print(num,end="")
