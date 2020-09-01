import os

path="file_path"

def parse(path):
    dirList=os.listdir(path)
    dirList.sort()

    fnames = []
    dnames = []

    for fname in dirList:
        if os.path.isdir(path + fname):
            
            dnames.append(fname)
        if os.path.isfile(path + fname):
            fnames.append(fname)

    return dnames,fnames

(files,folders) = parse(yol)
os.chdir(path) 

a=0
for i in folders:
    
    os.rename(i,"file_name."+str(a)+".jpg")
    a = a+1

