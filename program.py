f=open('17_2.txt'
a=[]
c=[]
d=160
p=7
for s in f.readlines():
    a.append(int(s))
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]%d!=a[j]%d and (a[i]%p==0 or a[j]%p==0):
            c.append(a[i]+a[j])
print(len(c),max(c))