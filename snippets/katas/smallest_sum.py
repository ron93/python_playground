def solution(a):
    length = len(a) # example: a = [6, 9, 12]
    print(a)
    mx = [] # mx = [a[idx], idx] -> idx = 1, 2, 3
    n = 0
    checkList = [a[i] != a[n] for i in range(length)] # checkList = [False, True, True]
    check = any(checkList) # check = True

    print(f"checkList: n: {n} {checkList}")
    print(f"check: n:{n} {check} \n")

    while(check):
        for idx in range(length): # idx = 0, 1, 2
            if not mx: # 1st iter empty list -> mx
                mx = [a[idx], idx] # mx = [6,0] 
                print(f"{a[idx]} mx at init {idx} {mx} \n")
            elif a[idx] > mx[0]: # 2nd iter -> 9 > 6. 
                a[idx] -= mx[0] #  2nd iter-> a[idx] = 9 - 6 => 3
                mx = [a[idx], idx] if a[idx] > mx[0] else mx # mx = 3 < 6 => mx = [6, 0]
                print(f" {a[idx]}mx at > {idx} {mx}")
                if idx == n: 
                    n = (idx+1)%length 
                    checkList = [a[i] != a[n] for i in range(length)] 
                    print(f"checkList: n {n} idx {idx} {checkList}")
                    check = any(checkList) 
                    print(f"check: n {n} idx:{idx} {check} \n")
                else:
                    prev = checkList[idx] 
                    checkList[idx] = a[idx] != a[n] 
                    print(f"checkList: n {n} idx {idx} {checkList} \n")
                    if (not checkList[idx] and prev):
                        check = any(checkList)
                        print(f"check: n {n} idx {idx} {check} \n")
            
            elif a[idx] < mx[0]:
                a[mx[1]] -=a[idx]
                mx = [a[idx],idx] if a[idx] > a[mx[1]] else [a[mx[1]], mx[1]]
                print(f"{a[idx]} mx at < {idx} {mx}")
                if mx[1] == n:
                    n = (mx[1]+1)%length
                    checkList = [a[i] != a[n] for i in range(length)]
                    check = any(checkList)
                    print(f"checkList:  {idx} {checkList}")
                    print(f"check: n{n} idx {idx} {check} \n")
                else:
                    prev = checkList[mx[1]]
                    checkList[mx[1]] = a[mx[1]] != a[n]
                    print(f"checkList: n {n} idx {idx} {checkList} \n")
                    if (not checkList[mx[1]]) and prev:
                        check =  any(checkList)
                        print(f"check: n {n} idx {idx} {check} \n")
    print(f"a {a}")
    return sum(a)
                
            

print(solution([6, 9, 12]))