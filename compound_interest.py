def compound_interest(p,r,t): 
    Amount=p*(pow((1 + r / 100), t)) 
    CI = Amount - p
    print("Compound interest is", CI) 
p,t,r=[1200,2,5.4]
compound_interest(p,t,r) 