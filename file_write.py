my_letters = input("File content input : ")
max_index = len(my_letters)
output_file = "alpha.txt"
filewriter = open(output_file, 'a')
for index_value in range(max_index):
    if index_value < (max_index-1):
        filewriter.write(my_letters[index_value]+'t')
    else:
        filewriter.write(my_letters[index_value]+'n')
print("Output written to write")
