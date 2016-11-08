#Calculate the probability of a positive result given that
#p0=P(C)  - prior
#p1=P(Positive|C) - Sensitivity
#p2=P(Negative|Not C)  - Specitivity

def f(p0,p1,p2):
#Insert your code here
    return (p0*p1) + (1-p0)*(1-p2)

print f(.1, .9, .8)