#random-52-list.py python3 cwc
# Run this code and keep track of how many time you need to run the code
# to get a '0' as the first integer displayed
import random

	
def main():
	nlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
             21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
             41,42,43,44,45,46,47,48,49,50,51,52] 
             
	zlist =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	print(" 0 TO 51 ",nlist)
	count = 0
	done = 0 # 0 is false
	while (count < 53):
		while (done == 0):
			n =  random.randint(0,51)
			if (nlist[n] == 0):
				done == 0
			else:
				zlist[count] = n
				nlist[n] = 0
				count = count + 1
				
	print(nlist)
	print("*****")
	print(zlist)

		

main()
