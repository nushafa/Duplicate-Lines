#Program to eliminate duplicate lines from a file

#creating the output file
outputFile = open('UpdatedFile.txt', 'w')

#reading the input file
inputFile = open('Repeated.txt', 'r')

#hold lines already seen
line_seen_so_far = set()
print("Eliminating duplicate lines....")
#iterating each line in the file
for line in inputFile:

    # checking if line is unique
    if line not in line_seen_so_far:

        #write unique lines in output file
        outputFile.write(line)

        #adds uniqe lines to line_seen_so_far
        line_seen_so_far.add(line)

#closing the file
inputFile.close()
outputFile.close()    