import sys
import os
from github import Github
import tkinter as tk
from tkinter import filedialog
import shutil

# Code can be run as: 
#python GithubRepoCreation.py R Folder

# Path to Projects in Github
Defaultpath = "E:\\FINAL_PYTHON_PROGRAMS\\"
# Path to R_Code Folder in Defaultpath
pathforR = os.path.join(Defaultpath, "R_Codes")
# Path to Python_Code Folder in Defaultpath
pathforPython = os.path.join(Defaultpath, "Python_Codes")
# Type of codes in Arguments that can be "R" or "Python" as 1st Argument
TypeofCode = str(sys.argv[1])
# 2nd Argument will be directory name 
DirecName= str(sys.argv[2])
# Final fate/Path for the files or folders at last
FinalPath=''


# For making folder according to the type of language
def create_folder(path,folder):
    global FinalPath
    FinalPath=os.path.join(path, folder)
    if not os.path.exists(os.path.join(path, folder)):
        os.mkdir(os.path.join(path, folder))
        print("Folder " , FinalPath ,  " Created ")
    else:    
        print("Folder " , FinalPath ,  " already exists")


#Function for making for folders for files and not for moving folders
def type_of_code(makefolder):
    global FinalPath
    # Check Whether for R
    if TypeofCode =="R":
        if not os.path.exists(pathforR):
            os.mkdir(pathforR)
            print("Folder " , pathforR ,  " Created ")
        else:    
            print("Folder " , pathforR ,  " already exists")
        if makefolder==1:
            create_folder(pathforR,DirecName)
            print("you have made another ##R## folder Successfully !!!")
        else: 
            FinalPath=pathforR

    # Check Whether for Python
    if TypeofCode =="Python":
        if not os.path.exists(pathforPython):
            os.mkdir(pathforPython)
            print("Folder " , pathforPython ,  " Created ")
        else:    
            print("Folder " , pathforPython ,  " already exists")
        if makefolder==1:
            create_folder(pathforPython,DirecName)
            print("you have made another ##Python## folder Successfully !!!")
        else:
            FinalPath=pathforPython


# Function for moving the file/folder
def move_myfolder(folderpath):
    type_of_code(0)
    shutil.move(os.path.abspath(folderpath),FinalPath)
def move_myfile(filepath):
    type_of_code(1)
    shutil.move(os.path.abspath(filepath),FinalPath)

# Make a dialogue for asking that whther you want files or Folders to import to your folder.
root = tk.Tk()
v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python
Save = [
    ("Folder",1),
    ("File",2)#,
    #("Java",3),
    #("C++",4),
    #("C",5)
]

def ShowChoice(val):
    if val == 0:
        root.withdraw()
        folder_path = filedialog.askdirectory()
        print(folder_path)
        move_myfolder(folder_path)
    if val == 1:
        root.withdraw()
        file_path = filedialog.askopenfilename()
        print(file_path)
        move_myfile(file_path)
    root.destroy()

tk.Label(root, text="""Do you want to save a folder or file?""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, btext in enumerate(Save):
    tk.Button(root, 
                  text=btext[0],
                  width = 20,
                  padx = 20,  
                  command=lambda val=val: ShowChoice(val)).pack(anchor=tk.W)
    print(val)

root.mainloop()

#root.withdraw()
#file_path = filedialog.askopenfilename()

'''
username = "rehanzfr" #Insert your github username here
password = "*yaAllahtu1hai*" #Insert your github password here

def new_repository():
    #folderName = str(sys.argv[1])
    #os.makedirs(path + str(folderName))
    #print(str(sys.argv[1]))
    g = Github(username, password)
    user= g.get_user()
    print(user)
    #repo = user.create_repo(folderName)
    #print("Succesfully created repository {}".format(folderName))
    for repo in g.get_user().get_repos():
        for i in repo:
            if i =="Rbook":
                print(repo.name)
        #repo.edit(has_wiki=False)
        # to see all the available attributes and methods
        #print(dir(repo))


if __name__ == "__main__":
    create()
'''
