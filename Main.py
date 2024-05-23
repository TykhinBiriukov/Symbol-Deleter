inputFile = input("Please enter way to the file you want to read: ")
symbolToDelete = input("Please enter symbol to delete: ")
symbolToReplace = input("Please enter with what to replace deleted symbol: ")
#D:\Programming\Projects\Symbol Deleter\FourBitLogic.txt
with open(inputFile, "r") as file:
    output = file.read().replace(symbolToDelete, symbolToReplace)

outputFile = input("Please enter way to the file in which you want to save output: ")
#D:\Programming\Projects\Symbol Deleter\Output2.txt
with open(outputFile, "w") as text_file:
    text_file.write(output)