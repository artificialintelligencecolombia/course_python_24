#!usr/bin/env python3

# Set the filepaths and the modes
blueprint_filepath = './Input/Letters/starting_letter.txt'
blpnt_mode = 'r+'
list_of_invitees_filepath = './Input/Names/invited_names.txt'
invt_mode = 'r'
list_of_names = []

# Created a fn that reads the files and returns the content -> str.
def read_file(filename, mode):
    with open(filename, mode) as file:
        # If blueprint file, we need to edit it.
        if mode == 'r+':
            content = file.read()
            return content
        # If the file is the name list, only read.
        if mode == 'r':
            lines = file.readlines()
            return [line.strip() for line in lines]       

# store the elements in variables
file = read_file(blueprint_filepath, blpnt_mode)
list = read_file(list_of_invitees_filepath, invt_mode)

# Set the counter of the letters 
tk = 0
for name in list:
    invitation_letter = file.replace('[name]', name)
    print(f"INVITEE N.{tk}")
    print(invitation_letter)
    
    tk += 1




#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp