'''Exercise x in Coursera Bioinformatics algorithms(Part1)'''

def hamming(seq1,seq2):
    '''Calculates hamming distance between two equally sized sequences'''
    hamming=0
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:hamming+=1
    return hamming

def k_mers(seq,pattern):
    '''Creates a list of all kmers from sequence with the size of pattern'''
    kmers=[]
    for i in range(len(seq)-len(pattern)+1):
        kmers.append(seq[i:i+len(pattern)])
    return kmers

def count(seq,pattern,dist):
    '''Calculates the number o hits of a pattern in the sequence allowing less
    than dist mismatches'''
    kmers=k_mers(seq,pattern)
    counter=0
    for item in kmers:
        if hamming(item,pattern)<=dist:counter+=1
    return counter


