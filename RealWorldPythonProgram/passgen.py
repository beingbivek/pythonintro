import random

# Password Generator
alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
alphabet_upper = alphabet.upper()
number = '1,2,3,4,5,6,7,8,9,0'
symbols = '~,!,@,#,$,%,^,&,*,(,),:,.,?'
password = ""

all_characters = alphabet + "," + alphabet_upper + "," + number + "," + symbols
all_characters = all_characters.split(",")
for i in range(16):
    password = password + random.choice(all_characters)
print(password)