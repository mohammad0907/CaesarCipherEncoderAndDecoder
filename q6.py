

print("Hello World")

cipher = ""
plain = ""
f = open('Independence.txt', 'r')
o = open('Independence2.txt', 'a')
read = open('Independence2.txt', 'r')
dec = open('Independence3.txt', 'a')

print(read.name)

def encode(f):
    for line in f:
        cipher = ""
        for char in line:
            if(char.isupper()):
                if(ord(char) + 3 <= 90):
                    cipher = cipher + chr(ord(char) + 3)
                else:
                    x = ((ord(char) + 3) - 90) -1
                    cipher = cipher + chr(97+x)
            else:
                if(ord(char) + 3 <=122 ):
                    if(char.isalpha()):
                        cipher = cipher + chr(ord(char) + 3)
                    else:
                        cipher = cipher + char
                else:
                    y = ((ord(char) + 3) - 122) -1 
                    cipher = cipher + chr(65+ y)
        


def decode(o):
  
    for line in o:
        plain = ""
        for char in line:
            if(char.isupper()):
                if(ord(char) - 3 >= 65):
                    plain = plain + chr(ord(char) - 3)
                else:
                    x = (65 - (ord(char) - 3)) -1 
                    plain = plain + chr(122 - x)
            else:
                if(ord(char) -3 >= 97 ):
                    if(char.isalpha()):
                        plain = plain + chr(ord(char) -3)
                    else:
                        plain = plain + char 
                else:
                    if(char.isalpha()):
                        y = (97 - (ord(char) -3 )) - 1
                        plain = plain + chr(90 - y)
                    else:
                        plain = plain + char 

        dec.write(plain)
        print(plain)
        
    


encode(f)
decode(read)
   
        



