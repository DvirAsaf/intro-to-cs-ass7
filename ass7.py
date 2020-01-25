##########################################
# Name: Dvir Asaf
# ID: 313531113
# Group: 01
# Assignment: ass7
##########################################

import csv
# Create an empty dictionary
d = dict()

def parser(fileName):
    # Open the file in read mode
    text = open(fileName, "r")

    files = []
    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Split the line into words
        words = line.split(" ")

        # Iterate over each word in line

        for word in words:
            if (word[:5] == "href="):
                w_by_quotes = word.split("\"")
                file_name = w_by_quotes[1]
                files.append(file_name)
                # print(file_name)
    # print(files)
    d[fileName] = files
    # print(d)
    for f in files:
        if f not in d:
            parser(f)

# parser("1.html")

def Crawler():
    source_file = input("enter source file:\n")
    parser(source_file)
    # print(d)
    with open('results.csv', 'w') as f:
        for key in d.keys():
            f.write("%s" % key)
            for link in d[key]:
                f.write(",%s" % link)
            f.write("\n")

    file_name = input("enter file name:\n")
    # print(file_name)
    # print(d[file_name])
    list = d[file_name]
    # list.append(d[file_name])
    list.sort()

    print(list)



Crawler()