import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"/Users/Emerson/Documents/workspace/Python/prank")
    #print(file_list)
    saved_path = os.getcwd();
    os.chdir(r"/Users/Emerson/Documents/workspace/Python/prank")
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
    #(2) for each file, rename filename
    
rename_files()

