def pair_sum(arr,k):
    lookup = {}
    results = []
    for num in arr:
        if k-num in lookup:
            results.append((k-num,num))
        else:
            lookup[num] = k-num

    
    return len(results)
