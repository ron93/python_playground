import itertools
keypad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["_", "0", "_"]]

def get_pins(observed):
    keys = []

    indexes = []


def key_index(n, keypad):
    e = []
    for x in keypad:
        for y in x:
            if y == n:
                #                     print(keypad.index(x),x.index(y))
                row = keypad.index(x)
                column = x.index(y)
                # e.append([keypad.index(x),x.index(y)])
                # coordinates = keypad.index(x),keypad.index[y]
    
                return row, column
observed = '11'

n = [n.strip() for n in observed]
def get_possible_keys(i,keypad):
    e =[]
    # print(f"i {i}")

    row, col = key_index(i, keypad)
    # print(f" row {row} col {col}")
        
    e.append(i)
    if row > 0: 
          e.append(keypad[row-1][col])
    if row < 2 or i == '8':
        # print(f"here{keypad[row+1][col]}")
        e.append(keypad[row+1][col])
    if col > 0 and i != '0':
        e.append(keypad[row][col-1])
        if col < 2 and i != '0':
            e.append(keypad[row][col+1])
    return e
keys  = []
for i in n:
    keys.append(get_possible_keys(str(i),keypad))
    

# print(n)
# res = list(map(key_index, n, keypad))
print(keys)
# for element in itertools.product(*keys):
#     print("".join(element))

print(list(map(lambda x : itertools.product(*x),keys)))