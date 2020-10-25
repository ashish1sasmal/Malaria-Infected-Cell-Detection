# @Author: ASHISH SASMAL <ashish>
# @Date:   22-10-2020
# @Last modified by:   ashish
# @Last modified time: 22-10-2020

import cv2
import os
import sys
import csv

file = open("dataset.csv","a")
c=0
label = ["Uninfected","Parasitized"]

head =["Label","area0","area1","area2","area3","area4"]

l=[]

for j in label:
    listd = os.listdir(f"cell_images/train/{j}")
    for _ in listd:
        img = cv2.imread(f"cell_images/train/{j}/{_}")
        img = cv2.GaussianBlur(img,(5,5),2)

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        thresh = cv2.threshold(gray,127,255,0)[1]
        contours,h = cv2.findContours(thresh,1,2)
        h=[j]
        for i in range(5):
            try:
                area = cv2.contourArea(contours[i])
                h.append(str(area))
            except:
                h.append("0")
        l.append(h)

with open("malaria.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(head)

    # writing the data rows
    csvwriter.writerows(l)
print("[ Dateset Build status: Done]")

#
# img = cv2.imread(f"cell_images/train/Uninfected/C1_thinF_IMG_20150604_104722_cell_15.jpg")
# img = cv2.GaussianBlur(img,(5,5),2)
#
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)[1]
#
# contours,h = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#
# for i in range(len(contours)):
#     print(cv2.contourArea(contours[i]))
