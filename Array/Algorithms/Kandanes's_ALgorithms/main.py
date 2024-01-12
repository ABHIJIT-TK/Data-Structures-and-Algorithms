a = [-2, -3, 4, -1, -2, 1, 5, -3]
maxi=float('-inf')
maax=0
for i in range(len(a)):
    maax+=a[i]
    if maxi<maax:
        maxi=maax
    if maax<0:
        maax=0
print(maxi)
