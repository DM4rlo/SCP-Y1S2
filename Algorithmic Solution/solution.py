from csv2dct import infect_dt # imports dictionary data
import numpy as np
overall = []

def stats(h,c):
    t_infc = 0 # stores positional length
    
    for i in range(1,13): # Person 1 name str
     
     for v in range(2,13): # Person 2 name str
         
         # If there was no interaction
         x = "p"+str(i)+"-p"+str(v) ; rx = "p"+str(v)+"-p"+str(i) # rx = x but reversed 
         if infect_dt.get(x) == None:
             continue
        
         r = len(infect_dt.get(x)) # gets length of interaction
        
         # Prints peoples names & positions of interactions
         if i == h:    
            if c == "n":
                print(x+":",infect_dt.get(x),"occurences: ",r)
                t_infc += r
            elif c == "y":
                t_infc += r
            
         # Handles data buffering, as data has to be name must be reversed
         if h == v:
            if c == "n": # performs addition with an output
                print(rx+":",infect_dt.get(x),"occurences: ",r)
                t_infc += r
            elif c == "y": # performs addition without printing out
                t_infc += r
            
    if c == "n":    
        print("\nTotal Amount of Interactions: ",t_infc)
        t_infc = 0
    else:
        overall.append(t_infc)
        t_infc = 0
    
def stats_options():
    result = np.array([]) 
    # Ask user for options
    c = str(input("\nDo you want to see a statistical summary? [y/n]: "))
    
    # Prints in-depth data for a person's interactions
    if c == "n":
        print("\nSyntax for stats| p1 to p2:[position], occurences:")
        for i in range(1, 13):    
            print()
            print("\nPerson",i, "Statistics")
            print("-"*50)
            stats(i,c)
    
    
    # Prints summary of data
    elif c == "y":
        for i in range(1, 13): 
            stats(i,c)
        result = np.append(result, overall) # puts lst into array for data access
        print("\n---------------------------------------------------------#")
        print("Summary of Infection Rate Statistics                     #")
        print("---------------------------------------------------------#")
        # Prints all interactions
        for i in range(1,13):
            print("p"+str(i)+", Interactions: ",result[i-1])
        
        # Sorted array, using timsort, as alternative to merge sort, because best case
        srted_arr = sorted(result)
        
        # Prints Risk Analysis of Highest to Lowest Infection
        print("\n---------------------------------------------------------#")
        print("Risk Analyst Assessment                                  #")
        print("---------------------------------------------------------#")
    
        # Get the highest and lowest values from array returning their indexes
        # +1 is to equal corresponding person as the result follows a stack structure
        mx = (np.where(result == np.max(srted_arr))[0])+1 
        mn = (np.where(result == np.min(srted_arr))[0])+1
        
        # Print everyone with highest risk 
        print("People with lowest infection rate below at: ", np.min(srted_arr))       
        for i in mn:
            print("- p"+str(i))
        
        # Prints every else at moderate risk
        print("\nModerate risk below: Acending Gradient")
        tmp = None
        for i in srted_arr:
            if (i == np.max(srted_arr)) or (i == np.min(srted_arr)):
                continue
            # stop duplicates from printing (could have used set, but unneccessary)
            if tmp == i:
                continue
            tmp = i
            print("- p"+str(np.where(result == i)[0]+1))
            print(i,"")
        
        # If more than one person has the highest infection rate
        print("\nPeople with highest infection rate below at: ", np.max(srted_arr))
        for i in mx:    
            print("- p"+str(i))
         
    # Handles input error
    else:
        print("Input must be either 'y' or 'n'")
    
stats_options()






















