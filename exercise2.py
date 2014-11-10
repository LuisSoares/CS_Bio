"""Second exercise in Coursera Bioinformatics Algorithms(Part1)"""


def count(seq,pattern):
    '''Takes a sequence and a pattern and returns number
    of occurences of pattern in the sequence including overlapping'''
    count=0
    for i in range(0,len(seq)-len(pattern)):
        if seq[i:i+len(pattern)]==pattern:
            count+=1
    return count

def FrequentWords(Seq,k):
    '''Takes a Sequence and an int(k) finds
    all k-mers in the sequence and prints the more frequent
    #Attention:does not return anything just prints
    #count function is from exercise 1
    '''
    FrequentPatterns=dict()
    for i in range(0,len(Seq)-k):
        Pattern=Seq[i:i+k]
        FrequentPatterns[Pattern]=count(Seq,Pattern)
    maxCount=max(FrequentPatterns.values())
    MaxFreqPatt=[key for key,value in FrequentPatterns.items() if value==maxCount]
    for item in MaxFreqPatt:print(item, end=' ')
