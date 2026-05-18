def safe_int(s):
    try:
        return int(s)
    except:
        Exception
        return None 
    
def safe_divide(a, b):
    try:
        return a / b
    except:
        ZeroDivisionError
        print("some error")

def get_value(d, key):
    try:
        return d[key]
    except:
        KeyError
        print("mising")

def parse_ints(values):
    for str in values:
        try:
            int(values[str])
        except:
            TypeError
print(parse_ints(["1", "2", "x", "3", "y"] )
            

        



    


