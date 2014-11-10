"""Second exercise in Coursera Bioinformatics Algorithms(Part1)"""


def count(seq,pattern):
    '''Takes a sequence and a pattern and returns number
    of occurences of pattern in the sequence including overlapping'''
    count=0
    for i in range(0,len(seq)-len(pattern)):
        if seq[i:i+len(pattern)]==pattern:
            count+=1
    return count
	
def PatternMatch(pattern,seq):
    '''Takes a pattern and a seq and returns list the indexes
    where the pattern is found'''
    positions=[]
    for i in range(0,len(seq)-len(pattern)):
        if seq[i:i+len(pattern)]==pattern:
            positions.append(i)
    return positions

def FrequentWords(Seq,k):
	'''Takes a Sequence and an int(k) finds
    all k-mers in the sequence and returns dict with Pattern->Freq
	'''
	FrequentPatterns=dict()
	for i in range(0,len(Seq)-k):
		Pattern=Seq[i:i+k]
		FrequentPatterns[Pattern]=count(Seq,Pattern)
	return FrequentPatterns
	
	
def PatternFrequencies(FrequentPatterns,freq):
	'''Take a dict of Pattern->Freq and returns list of patterns with more
	than Freq occurences'''
	a=[key for key,value in FrequentPatterns.items() if value>=freq]
	return a
	
def PositivePatterns(seq,k,freq):
	'''Finds sequences of k size in seq that are repeated at least
	freq times, returns dict of Pattern->positions in seq
	'''
	FrequentPatterns=FrequentWords(seq,k)
	PositivePatterns=PatternFrequencies(FrequentPatterns,freq)
	PositivePatternsPositions=dict()
	for item in PositivePatterns:
		PositivePatternsPositions[item]=PatternMatch(item,seq)
	return PositivePatternsPositions

def PositivePatternsWindow(seq,freq,window,k):
	'''Finds sequences of k size in seq that are repeated at least
	freq times, returns patterns that are repeated at least freq times 
	in window
	'''
	PositivePatternsPositions=PositivePatterns(seq,k,freq)
	Positives=set()
	for item,value in PositivePatternsPositions.items():
		i=0
		while True:
			try:
				if value[i+(freq-1)]-value[i]<=window:
					Positives.add(item)
					break
				i=i+1
			except:break
	return Positives
	
def main(seq,freq,window,k):
	'''prints results of PositivePatternWindows in nice format
	'''
	a=PositivePatternsWindow(seq,freq,window,k)
	for item in a:
		print(item, end=' ')
		

