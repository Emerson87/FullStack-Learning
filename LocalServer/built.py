def compare(x,y):
    a = cmp(x,y)
    if a == 1:
        return x
    else:
        if a == -1:
            return y
        else:
            return "equals"
        
print compare(4,2)
print compare(2,2)
print compare(2,4)

