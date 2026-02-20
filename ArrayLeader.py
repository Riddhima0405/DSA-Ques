max_so_far = float('-inf')
        result = []
    
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] >= max_so_far:
                result.append(arr[i])
                max_so_far = arr[i]
    
        return result[::-1]
