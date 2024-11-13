def Maxx(v):
    maxx = v[0]
    for x in v:
        if x > maxx:
            maxx = x
    return maxx


def Minn(v):
    minn = v[0]
    for x in v:
        if x < minn:
            minn = x
    return minn


def sum(v):
    s = 0
    for x in v:
        s = s + x
    return s


def Table(col):
    table = []
    count = []
    for x in col:
        if x not in table:
            table.append(x)
    print(table)
    i = 0
    for y in table:
        c = 0
        for x in col:
            if y == x:
                c = c + 1
        count.append(c)
    print("Table")
    print(table)
    print(count)
    return table, count


def Det_he(vec):
    l = len(vec)
    return (l + 1) * 7

def Mode(col):
    table, count = Table(col)

    mode = []
    i = 0
    for x in count:
        if x == Maxx(count):
            mode.append(table[i])
        i = i + 1
    print("mode")
    print(mode)
    return mode

def MostRare(col):
    table, count = Table(col)

    most_rare = []
    i = 0
    for x in count:
        if x == Minn(count):
            most_rare.append(table[i])
        i = i + 1
    print("most rare")
    print(most_rare)
    return most_rare

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n)

def date_is_quant(col):
    summ = 0
    for t in col:
        if not is_integer(t):
            summ = summ + 1
    if summ != 0:
        return False
    else:
        return True

def len_max(vector, string):
    maximum = len(str(vector[1]))
    if len(string) > maximum:
        maximum = len(string)
    for x in vector:
        if len(str(x)) > maximum:
            maximum = len(str(x))
    if maximum > 40:
        maximum = 40
    if maximum < 10:
        maximum = 10
    return maximum

def is_date(string, fuzzy=False):
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

def Columns(data):
    if data != []:
        n = len(data[0])
        m = len(data)
        columns = []
        for i in range(n):
            icolumn = []
            for j in range(m):
                icolumn.append(data[j][i])
            columns.append(icolumn)
    elif variables != []:
        columns = []
        for x in variables:
            columns.append([])
    else:
        columns = []
    return columns


def auto_options(data):
    n = len(data[0])
    m = len(data)
    columns = Columns(data)
    ops = []
    p = []
    var_type = []

    for j in range(n):
        c = columns[j]
        ifikse = 1
        options = [c[0]]
        for i in range(ifikse, m):
            if c[i] not in options:
                options.append(c[i])
                ifikse = i

        ops.append(options)

    sa = []
    for i in range(len(ops)):
        thvt = []
        o = ops[i]
        for x in o:
            if isinstance(x, str):
                if is_integer(x) or is_date(x):
                    thvt.append(1)
                else:
                    thvt.append(0)
            else:
                if isinstance(x, int):
                    thvt.append(1)
                else:
                    thvt.append(0)
        var_type.append(thvt)
    for i in range(n):
        sh = [0]
        k = 0
        for option in ops[i]:
            for j in range(m):
                if columns[i][j] == option:
                    sh[k] = sh[k] + 1
            k = k + 1
            sh.append(0)
        sa.append(sh)
    for i in range(n):
        if sum(sa[i]) == len(ops[i]) or len(sa[i]) <= 2 or sum(var_type[i]) != 0 or len(sa[i]) >= 0.4 * len(data):
            ops[i] = ['']
    return ops
