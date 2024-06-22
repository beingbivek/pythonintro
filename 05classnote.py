import random # For using random funcitons it is cumpulsary

# Guess a random number between 1 to 10
# random_num = random.randint(1,10)
# user_input = int(input("Guess number between 1 to 10: "))
# print(f"Your number was {user_input} and computer guessed {random_num}")

# Find random number between -20 and -10
# random_num = random.randint(-20,-10)
# print(random_num)

# Random String
# person_names =['Ram','Sita',"Arati"]
# winner = random.choice(person_names)
# print(winner)

# Password Generator
alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
alphabet_upper = alphabet.upper()
number = '1,2,3,4,5,6,7,8,9,0'
symbols = '~,!,@,#,$,%,^,&,*,(,),:,.,?'
password = ""

all_characters = alphabet + "," + alphabet_upper + "," + number + "," + symbols
all_characters = all_characters.split(",")
for i in range(8):
    password = password + random.choice(all_characters)
print(password)
