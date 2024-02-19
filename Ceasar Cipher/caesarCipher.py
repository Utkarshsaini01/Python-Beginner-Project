import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text. 

def encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        index = (alphabet.index(char) + shift) % 26
        letter = alphabet[index]
        encrypted_text += letter
    
    print(f"plain text = {text}")
    print(f"shift = {shift}")
    print(f"cipher text = {encrypted_text}")
  
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
  
def decrypt(cipher_text, shift):
    plain_text = ""
    
    for char in cipher_text:
        index = (alphabet.index(char) - shift) % 26
        letter = alphabet[index]
        plain_text += letter
    
    print(f"The decoded text is: {plain_text}")
    

 #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
 #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
 
def caesar(text, shift, direction):
    
    result = ""
     
    for char in text:
        index = alphabet.index(char)
        if direction == "encode":
            index = (index + shift)%26
        else:
            index = (index - shift)%26
        
        letter = alphabet[index]
        result += letter
    
    print(f"The {direction}d text is: {result}")
            

end_of_program = False

while not end_of_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# if direction == "encode":
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)

    shift = shift % 26
    caesar(text, shift, direction)
    
    end = input("Type 'yes' if you want to go again. Otherwise type 'no': ")

    if end == "no":
        end_of_program = True
        print("Bye")



