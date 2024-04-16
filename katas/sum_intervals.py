from operator import itemgetter
import math

def sum_of_intervals(intervals):
    dgts = []
    print(f"un_sorted {intervals} \n")
    
    intervals = sorted(intervals, key=itemgetter(0))
    print(f"sorted {intervals}")
    length = 0
    last = 0
    
    for count, i in enumerate(intervals):
        # print(i)        
        start, end = abs(i[0]), abs(i[1])
        # print(f"start {start} end {end}")
        
        start_sign, end_sign = math.copysign(1,i[0]), math.copysign(1,i[1])
        # print("signs \n",start_sign, end_sign)
        last_sign = 1.0
        
        if (last_sign*last > start_sign*start and last_sign*last < end_sign*end) and count != 0:
            start = last
            start_sign = last_sign
            # print(" if 1",start, end)
            length += end_sign*end - (start_sign*start)
            last = end
            last_sign = end_sign
            # print(f"length {length} last{last}\n")
            
        elif start_sign*start <= last_sign*last and end_sign*end <= last_sign*last:
            # print(f"< : last {last} start {start} end {end}")
            continue
        
#         elif start_sign*start == end_sign*end:
#             print(f"== :last {last} start {start} end {end}")
            
        else:
            # print("3",start, end)
            length += end_sign*end - start_sign*start
            last = end
            last_sign = end_sign
            # print(f"length {length} last {last}\n")
            
    # print(length)
    return length
