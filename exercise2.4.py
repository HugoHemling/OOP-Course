def factorials(n: int):
    fact_dict = {}
    fact = 1
    
    for i in range(1, n + 1):
        fact *= i  
        fact_dict[i] = fact  
    
    return fact_dict


k = factorials(5)
print(k[1])  
print(k[3])  
print(k[5])  
