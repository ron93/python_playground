import input
def trib():
    next_num = 0
    num = input.u_range()

    output=[0,0,1]

    while next_num < num:
        next_num = int(output[len(output)-3]) + int(output[len(output)-2]) + int(output[len(output)-1])
        output.append(next_num)
    return  output
print trib()














