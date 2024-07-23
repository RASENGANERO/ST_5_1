import os
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
def main():
    image1 = cv2.imread("D:\\MACH\\MACH\\LAB_2\\image1.jpg")
    image2=image1
    image3=image1
    image2 = cv2.medianBlur(image2,5)
    image3 = ippiFilterMedian_8u_C3R(image3,5)
    cv2.imshow("Image_load",image1)
    cv2.imshow("OCV",image2)
    cv2.imshow("IPP",image3)
    cv2.waitKey(0)














def ippiFilterMedian_8u_C3R(s,q):
    s=cv2.medianBlur(s,q)
    return s    
   
if __name__=="__main__":
    main()