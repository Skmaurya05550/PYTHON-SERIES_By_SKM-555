# Writing to a file
# Explanation : File handling allow us to read froi mm and write to file . 


with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
