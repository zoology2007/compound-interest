def compound_interest (p, t, r):
    print("principle:",p)
    print("time:",t)
    print("rate of interest:",r)
    
    Amount = p * (pow((1 + r / 100), t))
    ci= Amount - p
    print("The simple interest is:",ci)
    return ci

p=float(input("Enter the principle "))
t=float(input("Enter the time "))
r=float(input("Enter the rate of interest "))
compound_interest (p,t,r)