print("Here will be the contents of the file:")
num_aliens = 0
with open("x-files.txt", "r") as f:
    #inside here the f file is open for reading
    #print(f.read())
    #f.read is one way of reading all the contents of the file
    for line in f:
        num_aliens += line.low().count("alien")

# once I am out, the file is closed
#f.read()
print("the word alien show up", num_aliens, "times in the file")
