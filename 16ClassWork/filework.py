# File Handling: Important
# r - Read
# w - Write
# a - Append
# x - Create

# f = open('bivek.csv','r') # Doesn't work this deep
f = open('./16StudentSoftware/bivek.csv','r')
# f = open('E:/Pythonclass/16StudentSoftware/bivek.csv','r') # Works
print(f.read())