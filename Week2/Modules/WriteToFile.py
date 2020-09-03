
def write_list_to_file(output_file, lst):
    myFile = ""
    for value in lst:
        myFile += value + '\n'

    with open(output_file, 'w') as file_object:
        file_object.write(myFile)
