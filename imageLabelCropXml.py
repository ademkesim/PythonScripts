# Improting Image class from PIL module 
from PIL import Image 
import pandas as pd  
# Opens a image in RGB mode 
import os
import numpy as np
import pandas_read_xml as pdx

def ayristir(path):
    dirList=os.listdir(path)
    #np.array(dirList)



    fnames = []
    dnames = []

    for fname in dirList:

        if os.path.isdir(os.path.join(path,fname)):
            dnames.append(fname)

        if os.path.isfile(os.path.join(path,fname)):
            fnames.append(fname)


    return dnames,fnames
    
images_path = "C:\\Users\\hsnyt\\Desktop\\trafic\\azami hız 30"
labels_path = "C:\\Users\\hsnyt\\Desktop\\trafic\\txtdosya"
#kırpılmış dosyaların olacağı klasör
new_image_path = 'C:\\Users\\hsnyt\\Desktop\\hazır\\'

(klasorler,dosyalar) = ayristir(labels_path)




# github repodaki 0,1 formatında hazırlandı
label_names = ["Sol","Sag","IleriSol","IleriSag","SolaDonulmez","SagaDonulmez","Girilmez","TrafikKapalı","Dur","ParkYapılmaz","ParkYeri","HizSiniri30","HizSiniri40","HizSiniri20Bitti","Durak"]
for i in dosyalar:

    df=pdx.read_xml(os.path.join(labels_path,i))

    image_name = df.loc['object'].loc['filename']

    image_number = 0
    
    xmin=int(df.loc['object'].loc['annotation'][0]['bndbox']['xmin'])
    ymin=int(df.loc['object'].loc['annotation'][0]['bndbox']['ymin'])
    xmax=int(df.loc['object'].loc['annotation'][0]['bndbox']['xmax'])
    ymax=int(df.loc['object'].loc['annotation'][0]['bndbox']['ymax'])


    crop_box = (xmin,ymin,xmax,ymax)

    print(crop_box)
    im = im.crop(crop_box)

    newsize = (250,250) 
    im_crop = im.resize(newsize)
    im_crop.show()

    try:
        os.mkdir(new_image_path+df.loc['object'].loc['annotation']['name'])
        print("folder created")
    except FileExistsError:
        print("file already exists.")

    im_crop.save(new_image_path+df.loc['object'].loc['annotation']['name']+'/'+image_name+'-'+image_number, quality=95)
    image_number += 1
