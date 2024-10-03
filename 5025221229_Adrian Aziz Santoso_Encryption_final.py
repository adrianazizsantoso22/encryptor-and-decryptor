import random
import string
import time

# Comparing both the strings.
def compare(a, b):
    return a != b

# Global variables for the public and private keys
publicKey = ""
privateKey = ""

def generatePublicKey(length):
    global publicKey
    possibleChars = string.ascii_letters + string.digits + "!@#$%^&*()"
    
    random.seed(int(time.time()))  # Seed for random number generation
    publicKey = ''.join(random.choice(possibleChars) for _ in range(length))
    
    print(f"The randomly generated public key is: {publicKey}")

def generatePrivateKey(length):
    global privateKey
    possibleChars = string.ascii_letters + string.digits + "!@#$%^&*()"
    
    random.seed(int(time.time()) + 1)  # Use a different seed for private key generation
    privateKey = ''.join(random.choice(possibleChars) for _ in range(length))
    
    print(f"The randomly generated private key is: {privateKey}")

repeat = 'y'

def main():
    global repeat
    while repeat == 'y':
        print("Welcome to Encryptor-Decryptor!")
        print("\nPlease choose one of the following options:")
        print("1 = Encrypt the string.")
        print("2 = Decrypt the string.")
        print("3 = Generate a public key.")
        print("4 = Generate a private key.")
        print("5 = Perform full procedure.")
        print("0 = Exit from the program.")
        
        a = int(input("\nDesired option: "))
        
        if a == 1:
            print("\n-----------------------------------------")
            str_input = input("\nPlease enter a string: ")
            encrypted = ''.join(chr(ord(char) + 3) for char in str_input)
            print(f"\nEncrypted string: {encrypted}")
            print("\n-----------------------------------------\n")
        
        elif a == 2:
            print("\n-----------------------------------------")
            str_input = input("\nPlease enter a string: ")
            decrypted = ''.join(chr(ord(char) - 3) for char in str_input)
            print(f"\nDecrypted string: {decrypted}")
            print("\n-----------------------------------------\n")
        
        elif a == 3:
            print("\n-----------------------------------------")
            generatePublicKey(32)
            print("\n-----------------------------------------\n")
        
        elif a == 4:
            print("\n-----------------------------------------")
            generatePrivateKey(32)
            print("\n-----------------------------------------\n")
        
        elif a == 5:
            print("\n-----------------------------------------\n")
            generatePublicKey(32)
            generatePrivateKey(32)
            
            str_input = input("\nPlease enter a string: ")
            encrypted = ''.join(chr(ord(char) + 3) for char in str_input)
            
            while True:
                pass_input = input("\nPlease enter the public key: ")
                if pass_input == publicKey:
                    break
                print("\nWrong public key! Try again.")
            
            print(f"\nEncrypted string: {encrypted}")
            
            decrypted = ''.join(chr(ord(char) - 3) for char in encrypted)
            
            while True:
                pass_input = input("\nPlease enter the private key: ")
                if pass_input == privateKey:
                    break
                print("\nWrong private key! Try again.")
            
            print(f"\nDecrypted string: {decrypted}")
            print("\n-----------------------------------------\n")
        
        elif a == 0:
            repeat = 'n'
            print("\n-----------------------------------------")
            print("\nThank you for using Encryptor-Decryptor!")
            print('Press "Enter" to exit.')
            return
        
        else:
            print("\nInvalid option. Try again.")

if __name__ == "__main__":
    main()


