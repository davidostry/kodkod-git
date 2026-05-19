def sum_all_nums(nums):
    sum=0
    for num in nums:
        sum += num
    return sum

def max_in_nums(nums):
    high_num=0
    for num in nums:
        if num > high_num:
            high_num=num
    return high_num  

def count_appears(value, list):
    count=0
    for i in list:
        if i == value:
            count += 1
    return count

def reverse_list(list):
    new_list=[]
    for i in list:
        new_list.insert(0,i)
    return new_list

def remove_duplicates(list):
    new_list=[]
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

def second_largest(nums):
    high_num=0
    second_num=0
    for num in nums:
        if num > high_num:
            high_num = num
    for j in nums:
        if high_num > num >second_num:
            second_num = num
    if second_num==0:
        return None
    else:
        return second_num

def merge_sorted_lists(list1, list2):
    list1.extend(list2)
    for i in list1:
        for j in range(i+1, len(list1)):
           if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
    return list1
        
                    
                    
def rotate_list(l, k):
    k = k % len(l)
    
    return l[-k:] + l[:-k]
   

 




