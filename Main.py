cd /content/drive/MyDrive
cd darknet
#!mkdir backup_data
import os
import numpy as np
list_file = os.listdir("data/obj/")
list_img = []
for file in list_file:
  if (".txt") not in file:
    list_img.append(file)
random_idx = np.random.randint(0, len(list_img), 200)
#T?o file train.txt ???c ??t trong th? m?c darknet/data
with open("data/train.txt","w") as f:
  for idx in range(len(list_img)):
    if idx not in random_idx:
     f.write("data/obj/"+list_img[idx]+"\n")
#T?o file valid.txt ???c ??t trong th? m?c darknet/data
with open("data/valid.txt","w") as f:
  for idx in random_idx:
   f.write("data/obj/"+list_img[idx]+"\n")
!make
!chmod +x ./darknet
!./darknet detector train data/obj.data cfg/yolo-tinyv4-obj.cfg yolov4-tiny.conv.29 -map -dont_show > yolotinv4_lisenceplate.log
!./darknet detector test data/obj.data cfg/yolo-tinyv4-obj.cfg \
backup_data/yolo-tinyv4-obj_last.weights csgt.jpg
path = "predictions.jpg"
import cv2
import matplotlib.pyplot as plt
image = cv2.imread(path)
original_width, original_height = image.shape[1], image.shape[0]
resized_image = cv2.resize(image, (2*original_width, 2*original_height)\
, interpolation = cv2.INTER_CUBIC)
resized_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(20,10))
plt.axis("on")
plt.imshow(resized_image)
plt.show()