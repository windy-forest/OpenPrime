import numpy as np
def euclid(bignum, smanum):
    rem = 1
    while rem != 0:
        rem = bignum % smanum
        bignum = smanum
        smanum = rem
    if bignum == 1:
        return True
    else:
        return False
    

prime_list = [2,3]
num = 3
prod = 6
while num < 1000000:
    num += 2
    if euclid(prod, num) == True:
        prime_list.append(num)
        prod *= num
        print(prime_list[-1])
np.savetxt('prime_list_euclid_1000000.txt', prime_list, delimiter='\r\n', fmt='%d')