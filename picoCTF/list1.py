#python3

listint = [16,9,3,15,3,20,6,20,
8,  
5,
14,
21,
13,
2,
5,
18,
19,
13,
1,
19,
15,
14]

liststr = "* "
print (listint)
for n in range (0,len(listint)):
 print(chr(listint[n]+65)) 
 i = listint[n]
 adj = 64
 liststr = liststr + str(chr(listint[n]+adj))

print(liststr)

