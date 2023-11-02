# HackerRank-> Prepare -> Algorithms-> Warmup
# Given two arrays same sized with score, compare to find who got better score
# Space and time o(n)


def compareTriplets(a, b):
    a_score = {}
    
    alice = 0
    bob = 0
    
    for idx, i in enumerate(a):
        a_score[idx] =i
    
    for idx in range(len(a)):
        if a_score[idx]>b[idx]:
            alice+=1
        elif a_score[idx]==b[idx]:
            pass
        else:
            bob+=1
    
    return [alice, bob]
