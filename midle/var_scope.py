a = 1
print(a)

def vartest():
    global a
    print(a)
    a = a + 10
    return a
    
a = vartest()
print(a)

if a ==13:
    pass   # 오류가 일어났지만 pass로 넘길 수 있음. 
           # (python만 있는기능)