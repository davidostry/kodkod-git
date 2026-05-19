def sum_values(d):
    total = 0
    for value in d.values():
        total += value
    return total

def max_key(d):
    max_k = None
    max_v = None
    for key, value in d.items():
        if max_v is None or value > max_v:
            max_v = value
            max_k = key
    return max_k

def count_characters(s):
    result = {}

    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def invert_dict(d):
    new_dict = {}
    for key, value in d.items():
        new_dict[value] = key
    return new_dict

def merge_dicts(d1, d2):
    result = {}
    for key, value in d1.items():
        result[key] = value
    for key, value in d2.items():
        result[key] = value
    return result

def filter_by_value(d, threshold):
    result = {}
    for key, value in d.items():
        if value > threshold:
            result[key] = value
    return result

def group_by_first_letter(words):
    result = {}
    for word in words:
        first = word[0]
        if first not in result:
            result[first] = []
        result[first].append(word)
    return result

def word_frequency(text):
    result = {}
    words = text.split()
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

def common_keys(d1, d2):
    result = []
    for key in d1:
        if key in d2:
            result.append(key)
    result.sort()
    return result

def most_frequent_value(d):
    counts = {}
    for value in d.values():
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    most_value = None
    most_count = 0
    for value, count in counts.items():
        if count > most_count:
            most_count = count
            most_value = value
    return most_value
