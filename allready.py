def salary (*args,**kwargs):
    total=10
    data=kwargs
    for key,value in data.items():
        if isinstance(value,str):
            data*=int(value)
    else:
        total*=value
        return total

result=salary("subiendu","suvo",raja=9000,raju=9000)
print("result",result)
