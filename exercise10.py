'''Exercise x in Coursera Bioinformatics algorithms(Part1)'''

def hamming(seq1,seq2,dist):
	'''Calculates hamming distance between two equally sized sequences'''
	hamming=0
	for i in range(len(seq1)):
		if seq1[i]!=seq2[i]:
				hamming+=1
				if hamming>dist:return False
	return True

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
        if hamming(item,pattern,dist):counter+=1
    return counter

def search(seq,dist,size):
	dna=['ATCG']
	positive_patterns=dict()
	from itertools import product
	kmers=k_mers(seq,'a'*size)
	i=0
	for item in product(*(dna*size)):
		item="".join(item)
		positive_patterns[item]=0
		if i%10000==0:
			print(i)
		item=''.join(item)
		for kmer in kmers:
			if hamming(item,kmer,dist):
				positive_patterns[item]=positive_patterns.get(item,0)+1
			if hamming(RevComp(item),kmer,dist):
				positive_patterns[item]=positive_patterns.get(item,0)+1
		i+=1
	return positive_patterns

def RevComp(seq):
    """Takes a seq and return the reverse completment"""
    return seq[::-1].translate(str.maketrans('ATCG','TAGC'))

def most_common(seq,dist,size):
	maximized=[]
	positive_patterns=search(seq,dist,size)
	maximum=max(positive_patterns.values())
	for key,value in positive_patterns.items():
		if value==maximum:
			print("".join(key),end=' ')
			
seq='CTCATCCTCGGATCGTTAAAATCATCCTCAAAGTTCTCAAAAAAATCAAAATCGGGTTGTTATCAAAGGAAAAAAGGCTCGGCTCATCAAAGTTGTTATCAAAGGCTCAAACTCATCGTTGGGTTGTTGGGTTAAAAAAGGGTTATCATCGTTATCGTTGGATCGTTCTCATCAAAGGGGCTCCTCGGGGGTTGTTAAAAAAAAAGGATCCTCCTCCTCGGCTCAAAATCCTCGTT'
dist=3
size=8
from time import clock
def timing(seq,dist,size):
    start=clock()
    most_common(seq=seq,dist=dist,size=size)
    print((clock()-start)/60)
