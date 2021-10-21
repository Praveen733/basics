def simple_interest(p,t,r):
    print("The principal is",p)
    print("The time period is",t)
    print("The rate of interest is",r)
    si=(p*t*r)/100
    print("The simple interest is",si)
    return si
p,t,r=[8,6,8]
simple_interest(p,t,r)