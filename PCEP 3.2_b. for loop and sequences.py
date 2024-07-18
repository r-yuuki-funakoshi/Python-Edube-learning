#Geometric
a0=3
r=-2
n=20

geo_seq=[a0*r**(n-1) for n in range(1, n+1)] #REMEMBER just put n for the variable to be consistent
print(geo_seq)
print("Position of  -24: ", geo_seq.index(-24))

#Geometric2
b0=1
r=2
n=10

geo_seq2=[b0*r**(n-1) for n in range(1, n+1)]
print(geo_seq2)
geo_reverse=geo_seq2.reverse()
print(geo_reverse)

#Arithmistic
c0=1
d=2
n=10

ari_seq=[c0+d*(n-1) for n in range(1, n+1)]
print(ari_seq)

for i in range(len(ari_seq)):
    if ari_seq[i]%2!=0:
        ari_seq[i]="odd"
    else:
        ari_seq[i]="even"
print(ari_seq)
