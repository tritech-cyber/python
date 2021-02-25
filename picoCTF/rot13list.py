estr = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm{}_"
astr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{} "

def main():
	print(estr)
	print(astr)
	a = "c"
	b = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
	for i in range (0,len(b)):
		c = b[i]
		n =  estr.find(c)
		print(astr[n],end="")
	print()
if __name__ == "__main__":
   main()

'''
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x) 
'''
