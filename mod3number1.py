def fac(number):
    if number <1:
        return 1
    else:
        return number * fac(number - 1)
print(fac(n))
    
