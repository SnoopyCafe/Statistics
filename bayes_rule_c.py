#Return the probability of A conditioned on B given that
#P(A)=p0, P(B|A)=p1, and P(Not B|Not A)=p2

#Calculate the probability of a positive result given that
#p0=P(C)  - prior
#p1=P(Positive|C) - Sensitivity
#p2=P(Negative|Not C)  - Specitivity

def pos(p0,p1,p2):
#Insert your code here
    norm = (p0*p1) + (1-p0)*(1-p2)
    return (p0 * p1) / norm

#Calculate the probability of a positive result given that
#p0=P(C)  - prior
#p1=P(Positive|C) - Sensitivity
#p2=P(Negative|Not C)  - Specitivity

def neg(p0,p1,p2):
#Insert your code here
    norm = (p0*(1-p1) + (1-p0)*p2)
    return p0 * (1- p1) / norm

print neg(.1, .9, .8)