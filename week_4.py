
'''
try:
    #File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
    #Read the contents of input.txt.
    file =open("input.txt", "r")
    contents = file.read()
    print(contents)
    #modify to new file
    new_file = open("output.txt", "w")
    new_file.write(contents)
    print("File created successfully.")
    new_file.close()
except FileNotFoundError:
    print("The file input.txt does not exist.")

'''




'''
try:
    #Read the contents of input.txt.
    file = open("input.txt", "r")
    contents = file.read()
    #Count the number of words in the file.
    count = len(contents.split())
    print(f"Word Count: {count}")
    #Convert all text to uppercase.
    convert = contents.upper()
    print("Upper : ",convert)
    #Write the processed text and the word count to a new file called output.txt
    output_file = open("output.txt", "w")
    output_file.write(f"Word Count: {count}\n")
    #Print a success message once the new file is created.
    output_file.write(convert)
    print("File created successfully.")
except FileNotFoundError:
    print("The file input.txt does not exist.")

'''

class animal:
    def __init__(self, tyape, name):
        self.tyape = tyape
        self.name = name    
class dog(animal):
    pass

d = dog("dog", "Write")
print(d.tyape)
print(d.name)