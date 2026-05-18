def sum_of_a_tuple(tuple):
    sum = 0
    for num in tuple:
        sum += num
    return sum

def max_num(tuple):
    max = 0
    for num in tuple:
        if num > max:
            max = num
    return max

def count_occurrences(tuple, value):
    count = 0
    for i in tuple:
        if i == value:
            count += 1
    return count

def reverse_a_tuple(t):
    reverse = []
    for i in t:
        reverse.insert(0, i)
    return tuple(reverse)

def swap_pairs(t):
    swap = []
    for i in range(0, len(t), 2):
        swap.append (t[i+1])
        swap.append (t[i])
    return tuple(swap)

def min_and_max(t):
    first, *mid ,last = t
    return first, last

def distance_between_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

def merge_and_sort_tuples(t1, t2):
    merged = list(t1) + list(t2)
    for i in range(len(merged)):
        for j in range(i + 1, len(merged)):
            if merged[i] > merged[j]:
                merged[i], merged[j] = merged[j], merged[i]

    return tuple(merged)


def frequency_table(t):
    table = []
    for i in range(len(t)):
        count = 0
        for j in range(len(t)):
            if t[i]==t[j]:
                count +=1
        for item in table:
            if item[0] == t[i]:
                break
        else:
            table.append((t[i], count))
    return tuple(table)

def rotate_tuple(t, k):
    k = k % len(t)

    return t[-k:] + t[:-k]

                





    


    




