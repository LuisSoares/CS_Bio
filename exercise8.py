#Exercise 8 for Coursera Bioinformatic algorithms (partI)

def hamming_dist(seq1,seq2):
	hamming=0
	for i in range(len(seq1)):
    if seq1[i]!=seq2[i]:
        hamming+=1
	return hamming
	



