# Solution to Social Distance
import numpy as np  # Library for Arrays
import pandas as pd # Data Analysis Library
import math         # Mathematical Functions
from col_itr import colm_itr

# Case Study Code Start Here**********************************************************************************
N = 20

p1x = np.linspace(2,4,N)
p1y = np.linspace(1,8,N)

p2x = np.linspace(1,6,N)
p2y = np.linspace(6,6,N)

p3x = np.linspace(7,7,N)
p3y = np.linspace(7,7,N)

p4x = np.linspace(7,8,N)
p4y = np.linspace(6,4,N)

p5x = np.linspace(7,10,N)
p5y = np.linspace(0,6,N)

p6x = np.linspace(2.5,4.5,N)
p6y = np.linspace(1,8,N)

p7x = 3+np.array([math.sin(x*(2*math.pi/20)) for x in range(20)])
p7y = 3+np.array([math.cos(x*(2*math.pi/20)) for x in range(20)])

p8x = 6+np.array([1.5*math.sin(x*(2*math.pi/20)) for x in range(20)])
p8y = 6+np.array([math.cos(x*(2*math.pi/20)) for x in range(20)])

p9x = 9+np.array([0.5*math.sin(x*(2*math.pi/40)) for x in range(20)])
p9y = 4+np.array([0.5*math.cos(x*(2*math.pi/40)) for x in range(20)])

p10x = np.linspace(2,8,N)
p = np.array([ 0.02298526, -0.06700119, -1.42741697,  9.93895659])
p10y = np.polyval(p,p10x)

p11x = np.linspace(5,8,N)
p = np.array([  -1.41666667,   27.75      , -179.83333333,  389.        ])
p11y = np.polyval(p,p11x)

p12x = np.linspace(1,9,N)
p = np.array([ 0.02493438, -0.4855643 ,  3.38976378])
p12y = np.polyval(p,p12x)

p1 = np.c_[p1x,p1y]
p2 = np.c_[p2x,p2y]
p3 = np.c_[p3x,p3y]
p4 = np.c_[p4x,p4y]
p5 = np.c_[p5x,p5y]
p6 = np.c_[p6x,p6y]
p7 = np.c_[p7x,p7y]
p8 = np.c_[p8x,p8y]
p9 = np.c_[p9x,p9y]
p10 = np.c_[p10x,p10y]
p11 = np.c_[p11x,p11y]
p12 = np.c_[p12x,p12y]
# Case Study Code End Here***********************************************************************************

people = dict({"p1":p1,"p2":p2,"p3":p3,"p4":p4,"p5":p5,"p6":p6,"p7":p7,"p8":p8,"p9":p9,"p10":p10,"p11":p11,"p12":p12})


def frt(lst):
    a, b = 0 , 1
    
    for i in range(20):
        lstx.append(lst[i][a])
        lsty.append(lst[i][b]) 
        
df = pd.DataFrame(columns=(colm_itr()))
lstx = [] ; lsty = [] ; a, b = 0, 1

for i in range(12):
    q = "p"+str(i+1)+".x" ; w = "p"+str(i+1)+".y"
    
    i += 1
    # Update Lists  
    frt(people[f"p{i}"]) 
    i -= 1
    
    # append column 'x'
    df[q] = pd.Series(lstx)  
    
    # append column 'y'
    df[w] = pd.Series(lsty)  
    
    lstx.clear() ; lsty.clear()
    a += 2 ; b += 2
        
# Saves csv file with given name    
df.to_csv("SDP_Dataset.csv", index=False)

read_csv = pd.read_csv("SDP_Dataset.csv")
print(read_csv)


































'''
cmp_buffer = []

# [Person(0-11)][Position(0-19)], Indexical Notion

# Prints all 20 Positions for a Person
ttl = 0
occurs = [] 

for i in range(20):
    # Prints 1 position per iteration
    pp1 = people[0][i]
    pp2 = people[1][i]
    print("\np1, Position",str(i+1)+':',pp1)
    print("p2, Position",str(i+1)+':',pp2)
    
    
    if (pp1[0] >= pp2[0]-1 and pp1[0] <= pp2[0]+1) and (pp1[1] >= pp2[1]-1 and pp1[1] <= pp2[1]+1):
        print("They are within 2 meters of each other.")
        occurs.append(i)
        ttl += 1
    else:
        print("No")

print()
print("Total Interactions: ",ttl)
print("Positions of Interactions: ",occurs)
print("Infection Rate: %"+ str(ttl/20*100))

'''
























