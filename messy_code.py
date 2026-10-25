# BEFORE: messy code (works, but is hard to read, reuse and maintain)
a=[["Riya",78,85,92],["Aman",45,50,38],["Sara",88,91,95],["Karan",60,72,58]]
tt=0
for i in a:
    t=i[1]+i[2]+i[3]
    p=t/3
    if p>=90:
        g="A"
    elif p>=75:
        g="B"
    elif p>=60:
        g="C"
    elif p>=40:
        g="D"
    else:
        g="F"
    print(i[0],t,p,g)
    tt=tt+p
print("avg",tt/len(a))
m=0
n=""
for i in a:
    p=(i[1]+i[2]+i[3])/3
    if p>m:
        m=p
        n=i[0]
print("top",n,m)
