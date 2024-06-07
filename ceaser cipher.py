import string

##  Ceasor Cipher / Shift Cipher
plain_text = string.ascii_lowercase

mapping = dict()


def assignment():
    '''Creating a container that will be occupied by the key and
    its corresponding number in dictionary'''
    counter = 0

    for letter in plain_text:
        ''' importing each character to the container while skipping
         the null values '''
        mapping[letter] = ""


    for key in mapping:
        '''
            assignment the characters to are key or number
        '''
        mapping[key] = counter
        if counter < 26:
            ''' will iterate not until the index of the characters doesnot 
            go beyond the number of alphabet'''
            counter += 1
    return mapping


def Value_to_key(dict :dict ,key_value):
    '''
        this function is used to connect the corresponding value of the character
        to the corresponding value of the number in the dictionary or container
        '''
    for key, value in dict.items():
        if value == key_value:
            return key


def encryption(plaintext ,key=3):
    plaintext = plaintext.lower()
    cipher_text = error =error_space=""
    global check

    for char in plaintext:

        if char.isalpha():
            ''' incremeting the charater index with  the entered key
            '''
            shift_key = (assignment()[char] % 26) + key
            cipher=Value_to_key(assignment(),shift_key)
            cipher_text = cipher_text + str(Value_to_key(assignment(), shift_key))
            print(cipher,":"+ str(assignment()[cipher]))

        else:
            if char != char.isalpha():
                '''
                eliminating any other data type apart from character
                 present in the inputted text
              '''
                if char.isnumeric():
                    error =(error+char+" ")
                if char.isspace():
                    space=0
                    error_space = (char+error_space)
                    space=+1


    if len(error)>= 1:
        # to determine the number of occurance of the numeric
        print(error.split(), "Coudn't be Encrypted" ,space)
    if len(error_space)>=1:
        # determines the occurance of space in the plain text
        print("with",len(error_space),"space")

    #print(cipher_text.upper())

    return cipher_text.upper()


def decrpytion(cipher:str,key=3):
    ''' reversing the shift ceasor'''
    cipher= cipher.lower()
    plain_text=""
    for char in cipher:
        orginal_shift=(assignment()[char]-key)%26

    plain_text = plain_text+str(Value_to_key(assignment(), orginal_shift))
    return plain_text

def main(text, key=3):
    cipher_text = encryption(text, key=key)

    plain_text = decrpytion(cipher_text)
    print("Plain text: " ,text.upper())
    print("Cipher text: " ,cipher_text)

if __name__ =="__main__":
    while True:

        
        print("\n","#"*70,"\n","  ","*"*25,"Ceasor Cipher","*"*25,"\n","#"*70)
        prompt = input("\nEnter message: _" "_")
        main(prompt)
        print("_"*70,"\n")
