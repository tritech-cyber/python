#random-52.py python3 cwc
# Run this code and keep track of how many time you need to run the code
# to get a '0' as the first integer displayed
import random

def checklist(number,clist):
	# true is 1 and false is 0

def main():
	cardslist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
             21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
             41,42,43,44,45,46,47,48,49,50,51,52]  
             
	for i in range (1,53): 
	 n =  random.randint(1,52)
	 available = checklist(n,cardlist)
	 print(n," ",end="")
	 if(i % 10 == 0):
		 print(" * ")
	print("\n\t\t",i,"<- last i - - - \n\n")
