"""First exercise in Coursera Bioinformatics Algorithms(Part1)"""


def count(seq,pattern):
    '''Takes a sequence and a pattern and returns number
    of occurences of pattern in the sequence including overlapping
    this is importat beCause python string count method doesn't Count overlaps'''
    count=0
    for i in range(0,len(seq)-len(pattern)):
        if seq[i:i+len(pattern)]==pattern:
            count+=1
    return count


