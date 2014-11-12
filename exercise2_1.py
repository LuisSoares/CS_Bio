codon_table=dict(AAA='K',AAC='N',AAG='K',AAU='N',ACA='T',ACC='T',ACG='T',
                 ACU='T',AGA='R',AGC='S',AGG='R',AGU='S',AUA='I',AUC='I',
                 AUG='M',AUU='I',CAA='Q',CAC='H',CAG='Q',CAU='H',CCA='P',
                 CCC='P',CCG='P',CCU='P',CGA='R',CGC='R',CGG='R',CGU='R',
                 CUA='L',CUC='L',CUG='L',CUU='L',GAA='E',GAC='D',GAG='E',
                 GAU='D',GCA='A',GCC='A',GCG='A',GCU='A',GGA='G',GGC='G',
                 GGG='G',GGU='G',GUA='V',GUC='V',GUG='V',GUU='V',UAA='*',
                 UAC='Y',UAG='*',UAU='Y',UCA='S',UCC='S',UCG='S',UCU='S',
                 UGA='*', UGC='C',UGG='W',UGU='C',UUA='L',UUC='F',UUG='L',
                 UUU='F')

def translater(seq,table=codon_table):
	codons=[]
	i=0
	while i+3<len(seq)+1:
		codons.append(seq[i:i+3])
		i+=3
	translation=''
	for item in codons:
		translation=translation+table[item]
	return translation

def translate_reading_frames(seq):
        seq=seq.replace('T','U')
        translation_in_reading_frames=dict()
        for i in [0,1,2]:
                translation_in_reading_frames[i]=translater(seq[i:])
        for i in [3,4,5]:
                translation_in_reading_frames[i]=translater(seq[::-1][i-3:].translate(str.maketrans('AUCG','UAGC'))
)
        return translation_in_reading_frames

def encoding(seq,protein):
        translation=translate_reading_frames(seq)
        #print(translation)
        results=dict()
        for orf,item in enumerate(translation):
                start=0
                indexes=[]
                while True:
                        start=translation[item].find(protein,start)
                        if start==-1:
                                break
                        else:
                                indexes.append(start)
                                start+=1
                results[orf]=indexes
                print(results)
        for item in results:
                if item<3:
                        for value in results[item]:
                                print(seq[item+value*3:item+value*3+(len(protein)*3)])
                else:
                        item=item-3 
                        for value in results[item+3]:
                                stopindex=len(seq)-item-value*3
                                startindex=stopindex-len(protein)*3
                                print(seq[startindex:stopindex])
