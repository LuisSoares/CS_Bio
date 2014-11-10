"""Fourth exercise in Coursera Bioinformatics algorithms(Part1)"""

def PatternMatch(pattern,seq):
    '''Takes a pattern and a seq and prints the indexes
    where the pattern is found
    #Attention returns none'''
    positions=[]
    for i in range(0,len(seq)-len(pattern)):
        if seq[i:i+len(pattern)]==pattern:
            positions.append(i)
    for item in positions:print(item,end=' ')
