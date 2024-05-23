with open("D:\Programming\Projects\Symbol Deleter\FourBitLogic.txt", "r") as file:
    output = file.read().replace('|', "")
    
with open("D:\Programming\Projects\Symbol Deleter\Output2.txt", "w") as text_file:
    text_file.write(output)