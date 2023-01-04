n=int(input("how many emails need to be entered:"))
q=[]
i=1
while i<=n:
    a=input(f"enter email {i}:")
    b=a.split("@")
    q.append(b)
    i+=1
for i in range(0,n):
    print(f"username{i+1}:{q[i][0]} and domain{i+1}:{q[i][1].upper()}")
