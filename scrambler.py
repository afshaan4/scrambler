#Scrambler



#This program is based on a program by the raspberry pi foundation
#which can be found here: https://github.com/raspberrypilearning/secret-agent-chat

#THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import random #import the random generator

#establish the alphabet
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

#save yourself from typing out a full sentence everytime you want to generate a random number
r = random.SystemRandom()

#the key range
keyrange = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

#OTP generator
#generates files with the OTPs in it
#makes the otp & puts it in the files
def generate_otp(sheets, length):
    for sheet in range(sheets):
        with open("otp" + str(sheet) + ".txt","w") as f:
            for i in range(length):
                f.write(str(r.choice(keyrange))+"\n")

#reads the otp file specified
def load_sheet(filename):
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents

#reads user input & formats it as lowercase(for simplicity)
def get_plain_text():
    plain_text = input('Please type your message ')
    return plain_text.lower()

#loads the encrypted messages
def load_file(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents

#saves encrypted stuff as a file
def save_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

#encrypts stuff
def encrypt(plaintext, sheet):
    ciphertext = ''
    for position, character in enumerate(plaintext):
        if character not in ALPHABET:
            ciphertext += character
        else:
            encrypted = (ALPHABET.index(character) + int(sheet[position])) % 26
            ciphertext += ALPHABET[encrypted]
    return ciphertext

#decrypts stuff
def decrypt(ciphertext, sheet):
    plaintext = ''
    for position, character in enumerate(ciphertext):
        if character not in ALPHABET:
            plaintext += character
        else:
            decrypted = (ALPHABET.index(character) - int(sheet[position])) % 26
            plaintext += ALPHABET[decrypted]
    return plaintext


#startup menu (this is the UI that the user interacts with)
def menu():
    choices = ['1', '2', '3', '4']
    choice = '0'
    #set the password here
    passwd = 'hebi'
    check = input('Enter password ')
    #password verification happens here
    if check != passwd:
        print('Invalid password')
        quit()

    if check == passwd:
        print('Authentication sucessful')

    #UI "mainpage"
    while True:
        while choice not in choices:
            print('Welcome to Scrambler 2.1')
            print('1. generate encryption keys')
            print('2. Encrypt a message')
            print('3. Decrypt a message')
            print('4. encrypt a file')
            print('5. exit the program')
            #the UI "subpages"
            choice = input('Type in 1, 2, 3, 4 or 5 and press Enter ')
            if choice == '1':
                sheets = int(input('How many encyption keys would you like to generate? '))
                lenght = int(input('What will your message lenght be? '))
                generate_otp(sheets, lenght)
            elif choice == '2':
                filename = input('Type the filename of the encryption key to use ')
                sheet = load_sheet(filename)
                plaintext = get_plain_text()
                ciphertext = encrypt(plaintext, sheet)
                filename = input('Enter the name of the file  ')
                save_file(filename, ciphertext)
            elif choice == '3':
                filename = input('Type in the filename of the decryption key ')
                sheet = load_sheet(filename)
                filename = input('Type in the name of the file to decrypt ')
                ciphertext =load_file(filename)
                plaintext = decrypt(ciphertext, sheet)
                print('The message reads:')
                print('')
                print(plaintext)
                print('')
            elif choice == '4':
                print('# make sure the encryption key is long enough #')
                filename = input('Type in the filename of the encryption key to use ')
                sheet = load_sheet(filename)
                filename1 = input('Type in the filename of the file to encrypt ')
                plaintext = load_file(filename1)
                ciphertext = encrypt(plaintext, sheet)
                filename = input('To save the encrypted file seperatley give it a filename, or to save it as the same file type N ')
                if filename == 'N':
                    filename = filename1
                save_file(filename, ciphertext)
            elif choice == '5':
                exit()
            choice = '0'


menu()#trigger the menu (start the program)
