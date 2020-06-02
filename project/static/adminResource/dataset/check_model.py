#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 00:34:46 2019

@author: root
"""
import os
import cv2
import tensorflow as tf 



c = ['cancer', 'non_cancer']
img = ''


def prepare(file):
    print(file)
    I_S = 70
    globals()['img'] = cv2.imread(file)
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    print(img_array)
    new_array = cv2.resize(img_array, (I_S, I_S))
    return new_array.reshape(-1, I_S, I_S, 1)

#model = tf.keras.models.load_model('/Thunder/opencv/Dog_vs_Cat.model')
#
#
# for data in tqdm(os.listdir('/Thunder/opencv/test')):
#
#
#    img_data=prepare('/Thunder/opencv/test/'+data)
#
#
#
#    p=model.predict(img_data)
#
#
#
#    cv2.putText(img, c[int(p[0][0])], (50,50),cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
#    cv2.imshow("Cat VS Dog",img)
#    cv2.waitKey()
def main(imgpath):
    model = tf.keras.models.load_model(r'project/static/adminResource/dataset/Cancer.model')
    print(imgpath)

    p = model.predict(prepare(imgpath))

    #cv2.putText(img, c[int(p[0][0])], (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
    #cv2.imshow("Oral_cancer", img)
    #cv2.waitKey()
    print( c[int(p[0][0])])
    return c[int(p[0][0])]
