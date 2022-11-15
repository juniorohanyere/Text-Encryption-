import sys
from cryptography.fernet import Fernet

def create_key():
    
    #Generates a key and save it into a file
    
    key = Fernet.generate_key()
    
    # Accepts input to name the file where the generated key will be stored
    
    with open(filename , "wb") as key_file:
        key_file.write(key)
     
def load_key():
    
    # Loads the key from the current directory named `filename.key`
    return open(filename, "rb").read()

def encrypt ():
    
    global encrypted_text
    
    if __name__ == '__main__':
       # the if __name__ == '__main__'
       # is used when the script is called from the command line
       # and not as a module or library 
       
       # text = input ('Some text:\n··· ').encode()
        encrypted_text = f.encrypt(text.encode()) # got a problem with this, the 'text'.encode() method 
        
        return (encrypted_text)
        
    else:
    
        text = input ('Enter the text to encrypt\n··· ').encode()
        encrypted_text = f.encrypt(text)
        
        return (encrypted_text)
    
def decrypt ():
    
    decrypted_text = f.decrypt(encrypted_text)
    
    return (decrypted_text)
    
filename = ('cipher.key')

create_key()

key = load_key()

f = Fernet (key)

if __name__ == '__main__':

    print ('Loading functions...')
    print (' ' * 18 + 'done')
    
    input1 = input ('Welcome \n···')
    
    split_input = input1.split()
    
    no_of_words = len (split_input)
    no_of_index = no_of_words - 1
    
    command = split_input [0]
    commandk = split_input [no_of_index - 1]
    customkey = split_input [no_of_index]
    
    
    if command == ('-e') & commandk == customkey:
        
        command_e = split_input.pop(0)
            
        text = (' ').join (split_input)
            
        create_key ()
            
        key = load_key ()
        
        encryptedtext = f.encrypt (text)
        print (encryptedtext)
        print (text)
        
    elif command == ('-e') & commandk == ('-k'):
            
        command_k = split_input.pop (no_of_index - 1)
        command_e = split_input.pop (0)
        text = (' ').join (split_input)
        key = load_key
            
        encrypt ()
            
    elif command == ('-e') & customkey != ('-k'):
            
        custom_key = split_input.pop (no_of_index)
        command_k = split_input.pop (no_of_index - 1)
        command_e = split_input.pop (0)
        text = (' ').join (split_input)
        key = custom_key
            
        encrypt ()
            
       #ty = encrypt ()
      # print (ty)

