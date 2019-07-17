# Use caes2() to encrypt as a caesar shift, with the word you want to encrypt as a parameter within quotes. Only lowercase letters are supported

let = input("enter letter ")

def encryption(letter, shift): 
    num = ord(letter)
    letter = (num-97)
    pt= (letter+shift)%26
    
    pt = pt+97
    pt = chr(pt)
    return pt
    print(chr((letter+100)%122))
      
def caes2(word):
    et = ""
    for x in word:
        et = et.__add__(encryption(x, 3))
    print(et)
def decryption(letter, shift): 
    num = ord(letter)
    letter = (num-97)
    pt= (letter-shift)%26
    
    pt = pt+97
    pt = chr(pt)
    return pt
    print(chr((letter+100)%122))
def bfa(ct):
    for shift in range(1,26):
       
        dle = ""
        for x in ct:
            dl = ((ord(x)-97) - shift)%26
            dle = dle.__add__(chr(dl+97))
        print(dle)
bfa(let)
