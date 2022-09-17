import numpy as np
def prime_discrim(tested, prime_list):
    flag = False
    n = 0
    for i in prime_list:
        n += 1
        if tested % i == 0:
            flag = True
    if flag == False:
        return True
    else:
        return False

prime_list = [2,3]
num = 3
while num < 1000000:
    num += 2
    if prime_discrim(num, prime_list) == True:
        prime_list.append(num)

np.savetxt('prime_list_1000000.txt', prime_list, delimiter='\r\n', fmt='%d')