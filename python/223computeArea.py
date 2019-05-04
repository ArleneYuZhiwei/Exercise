
def computeArea(A, B, C, D, E, F, G, H):
    HA=C-A
    SA=D-B
    HB=G-E
    SB=H-F
    S1=HA*SA
    S2=HB*SB
    h=0
    s=0
    if ((G<=C and G>=A) or (E<=C and E>=A) or (A<=G and A>=E) or (C<=G and C>=E) ) and ((H<=D and H>=B) or (F<=D and F>=B) or (D<=H and D>=F) or (B<=H and B>=F)):
        h=min(C,G)-max(A,E)
        s=min(H,D)-max(B,F)
        S3=h*s
    else:
        S3=0
    res=S1+S2-S3

    return res

print (computeArea(-2,-2,2,2,-3,-3,3,-1)) 