
try:

    
    with open("test.txt", "w") as my_file:
        my_file.write("This is a test file.\n")
        my_file.write("It contains some sample text.\n")
        my_file.write("This is the third lines.\n")
        
    with open("test.txt", "r") as my_file:
        # content = my_file.read()
        # print(content)
        print(my_file.readlines()) # returns a list
        
    with open("test.txt", "r+") as my_file:
        content = my_file.read()
        print(content)
        my_file.write("\nThis is a new line.")
        
    with open("test.txt", "a+") as my_file:
        my_file.write("\nThis is an appended line.")
        print(my_file.read()) # returns an empty string because the cursor is at the end of the file
        my_file.seek(0) # move the cursor to the beginning of the file
        print(my_file.read()) # returns the content of the file
        my_file.seek(0)
        print(my_file.readlines())  # returns a list

    # with open("test.txt", "r") as my_file:
    #     content = my_file.read()
    #     print(content)
        
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error has occurred: {e}")
    