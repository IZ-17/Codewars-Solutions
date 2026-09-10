def count_positives_sum_negatives(arr):
    if not arr: 
        return []   
    pos_count = 0
    neg_sum = 0    
    for x in arr:
        if x > 0:
            pos_count += 1
        elif x < 0:
            neg_sum += x            
    return [pos_count, neg_sum]