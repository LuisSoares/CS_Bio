#Exercise 6 for Coursera Bioinformatic algorithms (partI)

def skew(seq):
	'''takes a seq and prints skew number for each position'''
	ccount=0
	gcount=0
	skew=[0]
	print(skew,end=' ')
	for i in seq:
		if i=='C':
			ccount+=1
		elif i=='G':
			gcount+=1
		skew.append(gcount-ccount)
	return skew


