from collections import Counter
from dateutil.parser import parse

def Maxx(v):
    return max(v)

def Minn(v):
    return min(v)

def sum(v):
    return sum(v)

def Table(col):
    counts = Counter(col)
    table, count = list(counts.keys()), list(counts.values())
    print("Table")
    print(table)
    print(count)
    return table, count

def Det_he(vec):
    l = len(vec)
    return (l + 1) * 7

def Mode(col):
    table, count = Table(col)
    max_count = max(count)
    mode = [table[i] for i, c in enumerate(count) if c == max_count]
    print("Mode")
    print(mode)
    return mode

def MostRare(col):
    table, count = Table(col)
    min_count = min(count)
    most_rare = [table[i] for i, c in enumerate(count) if c == min_count]
    print("Most Rare")
    print(most_rare)
    return most_rare

def is_integer(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def date_is_quant(col):
    return all(is_integer(t) for t in col)

def len_max(vector, string):
    maximum = max(len(str(x)) for x in vector)
    maximum = max(maximum, len(string))
    return min(max(10, maximum), 40)

def is_date(string, fuzzy=False):
    try:
        parse(string, fuzzy=fuzzy)
        return True
    except ValueError:
        return False

def Columns(data):
    if data:
        return [list(col) for col in zip(*data)]
    return []

def auto_options(data):
    columns = Columns(data)
    ops = []
    for col in columns:
        unique_vals = list(set(col))
        ops.append(unique_vals if len(unique_vals) > 1 else [''])
    return ops
