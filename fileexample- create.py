# a is amend the file that you already have and w is to write a new thing or delete what you have
f = open("x-files.txt" , "a" )
while True:
    line = input("give me some text to input into the file: ")
    if line.lower() == "stop":
        break
    f.write(line + "\n")

# we need to close the file at the end
f.close()




