
# coding: utf-8

# In[18]:

import math
def mean_function(slist): 
    
    sum = 0 
    for a in slist: 
         sum += a
    
    mean = sum / len(slist)
    nsum = 0 
    for b in slist: 
        nsum += (b - mean) * (b - mean)
    
    var = nsum / (len(slist) - 1) 
    dev = math.sqrt(var)
    result = {"mean":mean, "variance":var, "deviation":dev}
    return result
    #return var
    
    
    #return mean
This_list = [1, 2, 3, 5, 20]
Ans = mean_function(This_list)
print(Ans)  


# In[17]:

def my_function ():
    x = 0
    slist = []
    while True :
        x = input("Enter any number to compute mean: ")
        if x == "STOP!":
            break
        else:
            
            slist.append(int(x)) 
    sum = 0 
    for a in slist: 
         sum = sum +a
    
    mean = sum / len(slist)
    
    
        
    return mean
Ans = my_function()
print(Ans)


# In[ ]:



