n=len(arr)
        k=k%n
        
        def reverse(arr,left,right):
            while left<right:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1
        reverse(arr,0,n-1)
        reverse(arr,0,k-1)
        reverse(arr,k,n-1)
        
