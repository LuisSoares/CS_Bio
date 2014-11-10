#Exercise 7 for Coursera Bioinformatic algorithms (partI)

def skew(seq):
	'''takes a seq and returns skew number for each position'''
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
	
def minskew(seq):
	skewlist=skew(seq)
	minskew=min(skewlist)
	for i in range(len(a)):
    if a[i]==minskew:
        print (i, end=' ')



