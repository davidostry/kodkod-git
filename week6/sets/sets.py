def remove_duplicates(l):
    new = list(set(l))
    return new

def count_unique_elements(l):
    elements = []
    for item in l:
        if item not in elements:
            elements.append (item)
    return len (elements)

def common_elements(l1, l2):
    s1 =set(l1)
    s2 = set(l2)
    return list(s1.intersection(s2))
    
def element_is_only_one(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    return list(s1.symmetric_difference(s2))

def is_subset(a, b):
    return set(a) <= set(b)

def unique_characters(str):
    return len(str) == len(set(str))

def first_repeated_element(list):
    seen = set()
    for item in list:
        if item in seen:
            return item
        seen.add(item)
    return None

def distinct_word(str):
    words = str.lower().split()
    return len(set(words))

def pair_sum_exists(list, target):
    seen = set()
    for num in list:
        needed = target - num
        if needed in seen:
            return True
        seen.add(num)
    return False

def symmetric_difference(a, b):
    set_a = set(a)
    set_b = set(b)
    result = []
    for item in set_a:
        if item not in set_b:
            result.append(item)
    for item in set_b:
        if item not in set_a:
            result.append(item)
    return sorted(result)







