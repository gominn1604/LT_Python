def count(list):
    count = 0
    for num in list:
        if num == 4:
            count +=1
    return count
    
print(count([1,4,2,4,2,1,4]))