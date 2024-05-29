A=int(input())
B=int(input())
for i in range(A,B):
    for j in range(A,B):
        N=(i**2)+(j**2)
        if (N**0.5)>=A and (N**0.5)<=B and (N**0.5)%1==0 and i<j:
            print(str(i),str(j),str(int(N**0.5)))
