import os
yol="/media/ademk/EA003CD9003CAE87/pancar_veri/crop_image_resize/test/yabanci/"
def ayristir(path):
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
(klasörler,dosyalar) = ayristir(yol)
os.chdir(yol) 
a=0
for i in dosyalar:
    
    os.rename(i,"yabanci."+str(a)+".jpg")
    a = a+1

