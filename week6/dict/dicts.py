def sum_of_values(d):
    count = 0
    for v in d.values():
        count += v
    return count

def key_with_maximum_value(d):
    max_k = None
    max_v = None
    for k, v in d.items():
        if max_v is None or v > max_v:
            max_v = v
            max_k = k
    return max_k

def count_characters(str):
    characters ={}
    for char in str:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

def invert_a_dictionary(d):
    new = {}
    for k, v in d.items():
        new[v] = k
    return new

def merge_two_dictionaries(d1, d2):
    new = {}
    for k, v in d1.items():
        new[k] = v
    for k, v in d2.items():
        new[k] = v
    return new

def filter_by_value(d, threshold):
    new ={}
    for k, v in d.items():
        if v > threshold:
            new[k] = v
    return new

def group_by_first_letter(words):
    new ={}
    for word in words:
        letter = word[0]
        if letter not in new:
            new [letter] = []
        new[letter].append(word)
    return new

def word_frequency(str):
    new = {}
    words = str.split()
    for word in words:
        if word not in new:
            new[word] = 1
        else:
            new[word] += 1
    return new

def common_keys(d1, d2):
    result = []
    for k in d1:
        if k in d2:
            result.append(k)
    result.sort()
    return result

def most_frequent(d):
    new = {}
    for v in d.values():
        if v in new:
            new[v] += 1
        else:
            new[v] = 1
    most_v = None
    most_count = 0
    for k, v in new.items():
        if v > most_count:
            most_count = v
            most_v = k
        
    return most_v
    
print(most_frequent( {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2} ))
    
    








        


