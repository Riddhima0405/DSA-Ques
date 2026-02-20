arr.sort()
        n=len(arr)
        max_idx = n - 1
        min_idx = 0
        max_element = arr[n - 1] + 1
    
        for i in range(n):
            if i % 2 == 0:
                arr[i] += (arr[max_idx] % max_element) * max_element
                max_idx -= 1
            else:
                arr[i] += (arr[min_idx] % max_element) * max_element
                min_idx += 1
    
    
        for i in range(n):
            arr[i] = arr[i] // max_element
