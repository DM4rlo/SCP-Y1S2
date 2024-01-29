# Important for Case Study

'''
Used to create column names for coordinates of customers, to save time on 
typing, may serve to be more practical on larger datasets (year 2 maybe?)
'''

def colm_itr():
    lst = []
    
    a = 12 # People in dataset
    t = "x"
    q = 1
    
    while True:  
        if q == a+1:
            return lst
    
        x = "p"+str(q)+"."+str(t)
    
        if t == "x":
            t = "y"
            lst.append(x)
        else:
            t = "x"
            q += 1
            lst.append(x)
