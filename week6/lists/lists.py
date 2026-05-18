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
    for i in list1:
        if list2[0] <= i:
            list1.insert(i, list2[0])
            list2.remove(list2[0])
    return list1
                         

print(merge_sorted_lists([1,3,5], [2,4,6]))
   

 




