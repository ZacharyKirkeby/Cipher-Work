#Domingo Cipher is as follows:
#Z Y X W V U T S R Q P O N
#A B C D E F G H I J K L M

#Currently handles caps, lowercase. Runs until told to stop. The program can encrypt and decrypt as it is a symetrical form of encryption. 

def domingoCipherEncode(text):#encode/decode function
  cipher = ''
  for char in text: #iterates through each char
    if(char.isupper()):
      char = char.lower()
    if char.isalpha(): #checks if char is a letter
      reciVal = 122 - ord(char)
      reciSet = 97 + reciVal
      cipher = cipher + chr(reciSet)
    elif char == ' ': #leaves spaces alone
      cipher = cipher + char
    else:
      cipher = 'Symbols and numbers are not allowed'
      break 
#For obfusecation purposes, symbols and numbers are not allowed  
  print(cipher) 
  
def runner(): #runner function, handles input loop
  while 1==1: #infinite input loop
    print('Would you like to encrypt or decrypt? e/d')
    type = input()
    if type == 'e':
      print('What would you like to encrypt?')
      text = input()
      domingoCipherEncode(text)
    elif type == 'd':
      print('What would you like to decrypt?')
      text = input()
      domingoCipherEncode(text)
    elif type == 'stop': #in console way to end loop
      exit()
    else: #refuses any statement besides e or d
      print('Please try again')
runner()




  
  