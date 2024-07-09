#!usr/bin/env python3

# Open the file in read and append mode. It closes it automatically
with open('my_text_file.txt', 'r+') as f: 
    # Read the file -> by using read() method
    content = f.read()
    
    # Pr
    # int content before append
    print('Content before append: ')
    print(content)
    
    new_text = '\nbut I love elephants.'
    
    # Write on the file
    f.write(new_text)
    
    # Move the file pointer to the beginning of the file before reading the updated content
    f.seek(0)
    
    # Print the content of the file after append the new text
    new_content = f.read()
    print('Content after append: ')
    print(new_content)
    
    # Notas: