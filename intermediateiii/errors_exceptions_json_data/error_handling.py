# with open("non_existent_file.txt") as f:
#    f.read() -> output: error FileNotFoundError .

try:
    f = open("non_existent_file.txt") # This line will throw the error
    # If try statement is True, do:
except FileNotFoundError as error: # define the error type
    
    print(f"ERROR WARMING: {error}")
    file = open("any_file.txt", "w")
    file.write(f"HELLO! Data goes here.\n In this case, an error statement: \n{error}")

else:
    content = f.read()
    print(content)

finally:
    file.close()
    print("File closed")
    raise UnboundLocalError("fucking looser loool")