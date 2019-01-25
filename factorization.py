def factorization(n):
    factors_list = []
    factor = 2  
    while n > 1:
        
        if n%factor==0:
            factors_list.append(factor)
            n=n/factor
        else:
            factor+=1
        
    return factors_list
    
    
        