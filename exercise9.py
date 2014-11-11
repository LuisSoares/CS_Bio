#Exercise 8 for Coursera Bioinformatic algorithms (partI)

def hamming_dist(seq1,seq2):
	hamming=0
	for i in range(len(seq1)):
		if seq1[i]!=seq2[i]:
			hamming+=1
	return hamming
	
def kmers(seq,pattern):
    kmers=[]
    for i in range(len(seq)-len(pattern)):
        kmers.append(seq[i:i+len(pattern)])
    return kmers
	
def PatternMatching(seq,pattern,mismatch):
    k_mers=kmers(seq,pattern)
    for index,item in enumerate(k_mers):
        if hamming_dist(item,pattern)<=mismatch:print(index, end=' ')




