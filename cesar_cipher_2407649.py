'''
Name: Bikash Shrestha
Student Number: 2407649
'''

#Import the os module for operating system-related task.
import os

def welcome():
    """
    Displays a welcome message for the Caesar Cipher program.

    Parameters:
        No parameters.

    Return Value:
        None.

    Algorithm:
        This function prints a welcome message for the user introducing the Casear Cipher program.
        It provides information what Caeser Cipher is used for. 
    """
    #Print a welcome message to the user
    print("Welcome to the Caeser Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")

def enter_message(mode=None, message=None):
    """
    Receive data from the user for the mode, message, and the shift number for the Caeser Cipher.

    Parameters:
        - mode(str, optional): Identify whether to encrypt ('e') or decrypt ('d') the message.
        If not given, the user will be prompted to input the mode.
        - message (str, optional): The text message to be encrypted or decrypted.
        If not given, the user will be prompted to input the message.

    Return Value:
        Tuple: A tuple containing the mode (str), message (str), and shift number (int).

    Algorithm:
        1. If the mode is not given, ask the user to input whether they want to encrypt or decrypt.
        Validate the input to ensure it is either 'e' or 'd'.
        2. If the message is not provided, prompt the user to input the text message.
        3. Prompt the user to input the shift number and validate that it is a digit.
        4. Convert the shift number to an integer.
        5. Return a tuple containing the mode, message, and shift number.
    """
    #Prompt the user to enter the mode if the mode is not given and validate the mode.
    if mode is None:
        mode = input("Would you like to encrypt (e) or decrypt (d)? : ").lower()
        while mode not in ["e","d"]:
            print("Invalid Mode")
            mode = input("Would you like to encrypt (e) or decrypt (d)? : ").lower()
    #Check the user input if it either e or d.
    #Prompt the user for message if not given and the shift number and validate the shift number.
    if mode == "e":
        if message is None:
            message = input("What message would you like to encrypt: ").upper()
        shift = input("What is the shift number: ")
        while not shift.isdigit():
            print("Invalid Shift")
            shift = input("What is the shift number: ")
        shift_number = int(shift)
    else:
        if message is None:
            message = input("What message would you like to decrypt: ").upper()
        shift = input("What is the shift number: ")
        while not shift.isdigit():
            print("Invalid Shift")
            shift = input("What is the shift number: ")
        shift_number = int(shift)

    #Return a tuple containing the mode, message and shift number.
    return mode, message, shift_number

def encrypt(message, shift_number):
    """
    Encrypts a given message using the Caesar Cipher with a specified shift number.
    
    Parameters:
        - message (str): The text message to be encrypted.
        - shift_number (int): The number of positions each letter in the message should be shifted.

    Return Value:
        str: The encrypted message.

    Algorithm:
        1. Iterate through each character in the input message.
        2. Check if the character is an alphabet letter.
        3. If it is, shift the letter by the specified shift number.
        4. Concatenate the shifted character to the encrypted word.
        5. If the character is not an alphabet letter, keep it unchanged.
        6. Return the encrypted message.
        
    """
    #Initialize an empty string to store encrypted words
    encrypted_word = ""
    #Iterating through each character of input message and encrypting or decrypting the charcter.
    #If it is a alphabet shift the character otherwise remains same
    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char)+ int(shift_number) - ord("A"))%26 + ord("A"))
            encrypted_word += shifted_char
        else:
            encrypted_word += char
    #Return the encrypted_word
    return encrypted_word

def decrypt(message, shift_number):
    """
    Decrypts a given message encrypted using the Caesar Cipher with a specified shift number.

    Parameters:
        - message (str): The encrypted text message to be decrypted.
        - shift_number (int): The number of positions each letter in the message was shifted.

    Return Value:
        str: The decrypted message.

    Algorithm:
        1. Iterate through each character in the input encrypted message.
        2. Check if the character is an alphabet letter.
        3. If it is, shift the letter back by the specified shift number.
        4. Concatenate the shifted character to the decrypted word.
        5. If the character is not an alphabet letter, keep it unchanged.
        6. Return the decrypted message.
    """
    #Initialize an empty string to store decrypted words
    decrypted_word = ""
    #Iterating through each character of input message and decrypting the charcter
    #If it is a alphabet shift the character otherwise remains same
    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char)- int(shift_number) - ord("A"))%26 + ord("A"))
            decrypted_word += shifted_char
        else:
            decrypted_word += char
    #Return the decrypted_word
    return decrypted_word

def is_file(file_name):
    """
    Checks if a file with the specified name exists in the current directory.

    Parameters:
        - file_name (str): The name of the file to check for existence.

    Return Value:
        bool: True if the file exists, False otherwise.

    Algorithm:
        1. Use the os.path.exists() function to check if a file with the specified name exists.
        2. Returns True if the file exists, and False otherwise.
    """
    #Use the os.path.exists() function to check if a file with the specified name exists
    #Returns True if the file exists, and False otherwise.
    return os.path.exists(file_name)

def process_file(file_name, mode):
    """
    Reads a file, encrypts or decrypts its contents based on the specified mode and shift number,
    and returns a list of the processed words.
    
    Parameters:
        - file_name (str): The name of the file to be processed.
        - mode (str): Specifies whether to encrypt ('e') or decrypt ('d') the file contents.

    Return Value:
        list: A list containing the processed words (either encrypted or decrypted).

    Algorithm:
        1. Prompt the user for the shift number and validate that it is a digit.
        2. Convert the shift number to an integer.
        3. Open the specified file in read mode ('r').
        4. Iterate through each line in the file.
        5. Make all of the word in the line capitalize.
        6. Encrypt or decrypt each word on the line based on the specified mode and shift number.
        7. Split the processed word into a list of strings.
        8. Extend the result list with the processed word strings.
        9. Return the list of processed words.
    """

    #Prompt the user to input the shift number for the Caesar Cipher and validate the shift number.
    shift = input("What is the shift number: ")
    while not shift.isdigit():
        print("Invalid Shift")
        shift = input("What is the shift number: ")

    #Convert the shift number into an integer
    shift_number = int(shift)

    #Open the specified file in read mode ('r') and encrypt or decrypt according to specified mode.
    with open(file_name,'r', encoding = "utf-8") as file:
        #Initializing an empty list and string to store each words and encrypted words respectively.
        encrypted_word_list = []
        encrypted_word = ""
        for line in file:
            word = line.upper()
            if mode == "e":
                shifted_char = encrypt(word, shift_number)
                encrypted_word += shifted_char
            else:
                shifted_char = decrypt(word, shift_number)
                encrypted_word += shifted_char
        #Split the encrypted word into a list of each words and extend in the empty list
        string_list = encrypted_word.split()
        encrypted_word_list.extend(string_list)

        #Return the list of encrypted words
        return encrypted_word_list

def write_messages(string_list):
    """
    Writes a list of strings to a file, with each string on a new line.

    Parameters:
        - string_list (list): A list of strings to be written to the file.

    Return Value:
        None.

    Algorithm:
        1. Open a file named 'results.txt' in write mode ('w').
        2. Iterate through each string in the input list.
        3. Write each string followed by a newline character to the file.
        4. Close the file after writing.
        
    """
    #Open the file named results.txt in write mode('w').
    with open('results.txt','w', encoding = "utf-8") as file:
        #Iterate each string of the given string list and write each string followed by  new line.
        for string in string_list:
            file.write(f"{string}\n")

def message_or_file():
    """
    Prompts the user to choose between encrypting or decrypting,
    and whether to read input from the console or a file.

    Parameters:
        None.

    Return Value:
        Tuple: A tuple containing the mode (str), message (str), and file_name (str).

    Algorithm:
        1. Prompt the user to choose between encrypting ('e') or decrypting ('d').
           Validate the input to ensure it is either 'e' or 'd'.
        2. Prompt the user to choose between reading input from the console ('c') or a file ('f').
           Validate the input to ensure it is either 'c' or 'f'.
        3. If reading from the console:
            - Set file_name to None
            - Prompt the user to input the message according the the specified mode. 
        4. If reading from a file:
            - If encrypting, set the message to None.
            - Prompt the user for a filename and validate its existence.
        5. Return a tuple containing the  mode, message, and file_name.

    """
    #Prompt the user to enter the mode and validate the mode.
    mode = input("Would you like to encrypt (e) or decrypt (d)? : ").lower()
    while mode not in ["e","d"]:
        print("Invalid Mode")
        mode = (input("Would you like to encrypt (e) or decrypt (d)? : ")).lower()

    #Prompt the user to enter the method and validate the method.
    method = input("Would you like to read from a file (f) or the console (c)? : ")
    while method not in ["f","c"]:
        print("Invalid Method")
        method = input("Would you like to read from a file (f) or the console (c)? : ").lower()

    #Check the user input if it either f or c.
    if method == "c":
        #Set file_name to None
        #Check the user input and prompt the user for encrypt or decrypt message.
        file_name = None
        if mode == "e":
            message = input("What message would you like to encrypt: ").upper()
        else:
            message = input("What message would you like to decrypt: ").upper()
    else:
        #Set message to None and prompt the user to enter the filename and validate the filename.
        message = None
        file_name = input("Enter a filename: ")
        while not is_file(file_name):
            print("Invalid Filename")
            file_name = input("Enter a filename: ")
    #Return a tuple containing the mode, message, file_name
    return mode, message, file_name

def main():
    """
    Executes the logic of the Caesar Cipher program, allowing users to encrypt or decrypt messages,
    either from the console or a file. Outputs the results to the console or a file.

    Parameters:
        None.

    Return Value:
        None.

    Algorithm:
        1. Display a welcome message using the welcome() function.
        2. Enter a loop to repeatedly process user input.
        3. Use message_or_file() to determine whether to read from the console or a file,
           and whether to encrypt or decrypt.
        4. If reading from a file, process the file using process_file(),
           write the results to a file using write_messages(), and tell the user of the output file.
        5. If reading from the console, prompt the user for the shift number using enter_message().
           Encrypt or decrypt the message using encrypt() or decrypt(), and print the result.
        6. Prompt the user if they want to try again.
           If not, exit the loop and display a goodbye message.

    """
    #Display the welcome message for the caeser cipher program.
    welcome()
    while True:
        #Obtain the mode, message, file_name using message_or_file function
        mode, message, file_name = message_or_file()

        #Check whether the file name is given or not
        #If given encrypt or decrypt the file using process_file function
        #Write the encrypted words using write_message function.
        if file_name:
            messages = process_file(file_name, mode)
            write_messages(messages)
            print("Output written to results.txt")

        else:
            #Obtain the mode message, shift_number using enter_message function
            mode, message, shift_number = enter_message(mode, message)

            #Check the user input and use encrypt or decrypt function accordingly.
            if mode == "e":
                print(encrypt(message, shift_number))
            else:
                print(decrypt(message, shift_number))

        #Prompt the user if they want to try another message or file and validate the user input.
        repeat = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        while repeat not in ["y","n"]:
            repeat = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        #If the user don't want to try again then exit the program while displaying goodbye meesage.
        if repeat == "n":
            print("Thanks for using the program, goodbye!")
            break
main()
