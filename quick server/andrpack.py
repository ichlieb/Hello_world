import quarries as qu

def int_to_bytes(x: int, length = 0) -> bytes:
    if (length != 0): return x.to_bytes(length, 'big')
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')
    
def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')

def header_bytes(list:list) -> bytes:
    line = int_to_bytes(len(list), 2)
    for i in range(len(list)):
        a = bytes(list[i], 'utf-8')
        line += int_to_bytes(len(a), 2)
        line += a
    return line

def header_from_bytes(line:bytes) -> list:
    n = int_from_bytes(line[:2])
    cur = 2
    lst = []
    for i in range(n):
        length = int_from_bytes(line[cur:cur+2]); cur += 2
        lst += [line[cur: cur+length].decode()]; cur += length
    return lst

def line_bytes(list:list) -> bytes:
    line = bytes("", encoding='utf-8')
    for i in range(len(list)):
        a = bytes(list[i], 'utf-8')
        line += int_to_bytes(len(a), 4)
        line += a
    return line

def line_from_bytes(line:bytes, length:int) -> list:
    n = length
    cur = 0
    lst = []
    for i in range(n):
        length = int_from_bytes(line[cur:cur+4]); cur += 4
        lst += [line[cur: cur+length].decode()]; cur += length
    return lst

def table_to_bytes(list:list) -> bytes:
    num_l = len(list)
    if (num_l == 0): 
        return int_to_bytes(0, 4)
    num_c = len(list[0])
    line = int_to_bytes(num_c, 4); line+= int_to_bytes(num_l, 4)

    for i in range(num_l):
        anotherLine = line_bytes(list[i])
        line += int_to_bytes(len(anotherLine), 4)
        line += anotherLine
    return line

def table_from_bytes(line:bytes) -> list:
    lst = []
    cur = 0
    
    num_c = int_from_bytes(line[cur:cur+4]); cur +=4
    num_l = int_from_bytes(line[cur:cur+4]); cur +=4

    for i in range(num_l):
        length = int_from_bytes(line[cur:cur+4]); cur +=4
        anotherList = line_from_bytes(line[cur: cur+length], num_c); cur += length
        lst += [anotherList]
    return lst

def test():
    a = qu.table_to_list("select * from people")
    b = table_to_bytes(a)
    c = table_from_bytes(b)

    for i in c: print(i)

def suggestionFromBytes(line:bytes, size:int):
    return line[:size].decode("utf-8"), line[size:]

#a = ["lam", "kekm ", "ha"]

#print(table_from_bytes(table_to_bytes([a, ["lol"]])))