"""Third exercise of CourSera Bioinformatics Algorithms(Part2)"""

def RevComp(seq):
    """Takes a seq and return the reverse completment"""
    return seq[::-1].translate(str.maketrans('ATCG','TAGC'))
