#Two coins have probabilities of heads of p1 andd p2
#The probability of selecting the first coin is p0
#Return the probability of a flip landing on heads

# Pick one coin  C1  p(H | C1) = p1
# P(C1) = Po     C2  p(H | C2) = p2
# P(C2) = 1 - Po
# Po = 0.3, 1-Po = .7

def f(p0,p1,p2):
    pc2 = 1-p0
    p_H = (p0 * p1) + (pc2 * p2)
    return p_H



print f(0.1,.9,.8)