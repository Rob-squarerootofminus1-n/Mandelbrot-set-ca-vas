# Créé par Eleve, le 28/11/2022 en Python 3.7
def per(n):
    
    digits = [int(i) for i in str(n)] 
    result = 1
    for j in digits :
        result = result*j 
    return result 



n = 277777788888899
while len(str(n))!=1:
    print(per(n))
    n = per(n)