import pandas as pd
df = pd.read_csv("SDP_Dataset.csv") # <-------- Input CSV File Here
infect_dt = {} #  To be used for sorting the data 
intr = [] # stors interations

def dct_c(z,s): # Create Dictionary for data 
    if intr == []:
        intr.append("p"+str(s)) ; intr.append("p"+str(z))
    
    for i in range(1, 20): # For positions
         
        x1 = df.loc[i, "p"+str(s)+".x"]   
        y1 = df.loc[i, "p"+str(s)+".y"]  

        x2 = df.loc[i, "p"+str(z)+".x"]
        y2 = df.loc[i, "p"+str(z)+".y"]
    
        if (x1 >= x2-1 and x1 <= x2+1) and (y1 >= y2-1 and y1 <= y2+1):    
            intr.append(i+1)
        else:
            pass
        
    if intr != []:
        if len(intr) != 2:
            # print(intr)
            infect_dt.update({"p"+str(s)+"-"+"p"+str(z): intr[2:]})
    intr.clear()
        

for s in range(1, 13):    
    for i in range(s+1,13):
        dct_c(i, s)
    