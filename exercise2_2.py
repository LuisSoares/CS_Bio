mw=dict(G=57,A=71,S=87,P=97,V=99,T=101,C=103,I=113,L=113,
        N=114,D=115,K=128,Q=128,E=129,M=131,H=137,F=147,
        R=156,Y=163,W=186)

def get_all_substrings_1(input_string):
    length = len(input_string)
    return len( [input_string[i:j] for i in range(length-1) for j in range(i+1,length)])
