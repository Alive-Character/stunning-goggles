a= []
b = 1
d = 0
out = []
for i in range(4):
   l = int(input())
   a.append(l)
   if (l != 0):
       b = b*l
   else :
       c = i
       d += 1
if(d == 0):
    for i in range(4):
        out.append(int((b / a[i])))

if(d == 1):
    for i in range(4):
        if(i != c):
            out.append(0)
        else:
            out.append(b)

else:
    for i in range(4):
        out.append(0)
print(out)


