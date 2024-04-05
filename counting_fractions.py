def count_fractions(dmax,n1,d1,n2,d2):
    #the fractions that count have a numerator and denominator that do not have a common multiple
    #is there an easy to find this?
    #i'm envisioning an algorithm that increases the numerator, denominator gradually for the given range
    #i.e. if we start with 1/3.
    #we increase to 2/3 and it's > 1/2 so we increase 3 to 4 and start with 1
    #1 is too small, increase to 2, we have a common multiple, so next we have 3/4
    #larger than 1/2 so we increase to 5
    #1/5 too small. 2/5 is valid. 3/5 too large.
    #let's do it dumbly first
    n = 1
    d = d1
    f1 = (n1/d1)
    f2 = (n2/d2)
    count  = 0
    d_factors = factors(d)
    while d <= dmax:
        #need to find a way of finding common denoms
        #for each d we can list the multiples
        #then we can skip these in the n's
        
        skip = False
        for f in d_factors:
            if n%f == 0:
                skip = True
                break

        if (n/d) <= f1 or d%n == 0 or skip:
            n += 1
            continue
        if (n/d) >= f2:
            d += 1
            d_factors = factors(d)
            n = int(d/3) + 1
            continue
        n+=1
        count += 1
    return count

def factors(a):
    num = 2
    facts = []
    counters = []
    remainder = a
    while num <= remainder:
        skip = False
        for i in range(len(facts)):
            counters[i] -=1
            if counters[i] == 0:
                skip = True
                counters[i] = facts[i]
        if remainder %num == 0 and not skip:
            remainder = remainder/num
            facts.append(num)
            counters.append(num)
        num +=1
    return facts



if __name__ == "__main__":
    print(factors(1250214))

def next_prime(a):
    pass

