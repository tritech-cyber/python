#useradd -m -d /home/users/zoey zoey -s /bin/bash;
#echo "zoey:password" | chpasswd


def string_concat_users(a):
    b = "useradd -m -d /z/users/"+a+" "+a+" -s /bin/bash;"
    #zoey -s /bin/bash;"
    #b = b + a
    #b = b +"?tab=repositories\" target =\"_blank\" >"+a+"</a><br />"
    # b = b +"?tab=repositories\" target ="+ '"'+"_blank"+'"'+">"+a+"</a><br />"
    return b

def string_concat_passwords(a):
    b = "<a href = "+'"'+"https://"
    b = b + a + ".github.io"
    b = b +'"' + " target ="+ '"'+"_blank"+'"'+">"+a+"</a><br />"
    return b

def main():
	users = [['user1','abc123'],
	['user2','asd432'],
	['user3','spa124']
	]
	for n in range (0,len(users)):
		a = users[n]
		b = string_concat_users(a)
		print(b)

	print("\n\n * * * * * * * * \n\n")
	for n in range (0,len(users)):
		a = users[n]
		b = string_concat_passwords(a)
		print(b)

if __name__ == '__main__':
    main()

'''



def string_concat_repos(a):
	b = "<a href = "+'"'+"https://github.com/"
	b = b + str(a[1])
	b = b +"?tab=repositories\" target =\"_blank\" >"+a[0]+"-"+a[1]+"</a><br />"
	return b

def string_concat_io(a):
    b = "<a href = "+'"'+"https://"
    b = b + a + ".github.io"
    b = b +'"' + " target ="+ '"'+"_blank"+'"'+">"+a[0]+"</a><br />"
    return b

def main():
	users = [['A,Ulises','ulises-aguilar']
,	['A,Miguel A','MiguelAlcalan2020']
,	['B,Christopher Logan','Logan-Benner']
,	['B,Daniel S','danielbrogan26']
icebowl
ThatGuyJuan
Bouncyskoda
Bennythejet16
ulises-aguilar
ShawnR7305
Warghost13
jkiik
StrawberryIdiot
Osvaldoolivera
Axel-2002
MagickalWiz
danielbrogan26
taj-s
IrishPotato101
Logan-Benner
AwkwardPossum
Bennythejet16
DemonDrew0508
Calebpro22
MiguelAlcalan2020
NoorAlrubai
GerardoAmezcua092
cplusplusnewb
'''



'''
    users = ("Masoninja", "ElonMusk2018", "Delgado0001","junior-delatorre","JorgeFernandezJr",
            "Braeden42","Ngrade7","EvanIsakson00","Erduin17","NoahMcGe",
            "tylersul02","esperanzavillasenor","42silasweis","ObadiahBorms02",
            "S3thBr0wn","devonchen42","bcooper58","nathanhigley","EvanRichard2",
            "Aces14","bulletghost1","jadenbrewer","InfiniteGeo","masonguinn",
            "pedro-1970","HavensRyan","Jony-5","CyberCrypter2810","cmtthomas",
            "Treyster509v2","Bryan1998","trihstonmadden")
    for n in range (0,len(users)):
        a = users[n]
        b = string_concat(a)
        print(b)
'''


"""
# b = '"' + a + '"'
b = b + "target ="+'"'+"blank"+'"'+">"+a"</a><br />"
<a href = "https://github.com/Masoninja?tab=repositories" class = "link" target = "_blank"> Mason	A </a><br />
AMPM  = ("Masoninja", "ElonMusk2018", "Delgado0001","junior-delatorre","JorgeFernandezJr",
        "Braeden42","Ngrade7","EvanIsakson00","Erduin17","NoahMcGe",
        "tylersul02","esperanzavillasenor","42silasweis","ObadiahBorms02",
        "S3thBr0wn","devonchen42","bcooper58","nathanhigley","EvanRichard2",
        "Aces14","bulletghost1","jadenbrewer","InfiniteGeo","masonguinn",
        "pedro-1970","HavensRyan","Jony-5","CyberCrypter2810","cmtthomas",
        "Treyster509v2","Bryan1998","trihstonmadden")
"""
