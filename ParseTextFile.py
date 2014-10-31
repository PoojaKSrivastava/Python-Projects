##Pooja Srivastava 
#September 25, 2014
#!/usr/bin/python

import string

#Open input and output files
f = open("data.txt", "r")
g = open("newdata.txt", "w")

#Create a list to store each token in
tlist = []

# Loop over each line in the file
for line in f.readlines():

    #Pare the lines that don't begin with comments or new line characters
    if not line.startswith("//") and not line.startswith("\n"):
        # Strip the line to remove whitespace.
        line = line.strip(' \t\r')

        #Parse each line according to proper syntax
        line = line.replace("=", " = ")
        line = line.replace("+", " + ")
        line = line.replace("<<", " << ")
        line = line.replace(";", " ;")
        line = line.replace(" ,", ", ")
        line = line.replace(",", ", ")

        #Split line by space or ;
        tlist = line.split(" " or ";")

        #Traverse through each token in list
        for token in tlist:
            #Write tokens into output file
            if token.startswith("//"):
                g.write("\n")
                break
            if not token == '':
                if not token.endswith('\n'):
                    g.write(token + " ")
                else:
                    g.write(token)
#Close all files
f.close()
g.close()
