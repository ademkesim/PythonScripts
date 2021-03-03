# Improting Image class from PIL module 
from PIL import Image 
import pandas as pd  
# Opens a image in RGB mode 
import os
import numpy as np

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

    text=open(os.path.join(labels_path,i),"r")

    image_name = i.replace("txt","png")

    texts = text.readline()
    image_number = 0
    for rows in texts:
        row = rows.replace("\n","").split(" ")

        im = Image.open(os.path.join(images_path,image_name))
        frame_width,frame_height=im.size

        imx = int(round(frame_width * float(row[3])))
        imy = int(round(frame_height * float(row[4]))) 

        xmin = int(round(frame_width * float(row[1])) - (imx/2))
        ymin = int(round(frame_height * float(row[2])) - (imy/2))

        xmax = int(round(xmin + imx))
        ymax = int(round(ymin + imy))


        crop_box = (xmin,ymin,xmax,ymax)

        print(crop_box)
        im = im.crop(crop_box)

        newsize = (250,250) 
        im_crop = im.resize(newsize)
        im_crop.show()

        try:
            os.mkdir(new_image_path+label_names[int(row[0])-1])
            print("folder created")
        except FileExistsError:
            print("file already exists.")

        im_crop.save(new_image_path+label_names[int(row[0])-1]+'/'+image_name+'-'+image_number, quality=95)
        image_number += 1
