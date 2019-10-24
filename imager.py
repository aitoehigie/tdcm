#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A short Python script that given an image, will OCR the image and output the following:
MTBF in months
MTBF in years
Warranty in months
Warranty in days
Number of days till MTBF after Warranty finishes
*****************************************************************************************

Created on Wed October 24 15:05:49 2019

@author: Ehigie Aito https://twitter.com/pystar

'''
import re
import os
import cv2
import numpy as np
import pytesseract
from PIL import Image
from pytesseract import image_to_string

SRC_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))
)

def get_string(img_path):
    # Read the image
    img = cv2.imread(img_path)
    
    # Convert to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply dilation and erosion to remove image noise if any exists
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations = 1)
    img = cv2.erode(img, kernel, iterations = 1)

    # Write image after noise removal
    cv2.imwrite(SRC_PATH + "removed_noise.png", img)

    cv2.imwrite(SRC_PATH + "thres.png", img)

    # Recognize text with tesseract 
    result = pytesseract.image_to_string(Image.open(SRC_PATH + "thres.png"))
    
    #Parse the result for MTBF and Warranty values
    MTBF = re.findall(r"...........MTBF?", result)[0].split("M")[0]
    MTBF = float(MTBF) * 1000000
    warranty = re.findall(r"Warranty........", result)
    if MTBF:
        MTBF_in_months = MTBF/730.001
        MTBF_in_years =  MTBF/8760
    if warranty:
        warranty_in_months = int(warranty[0][-1]) * 12
        warranty_in_days = int(warranty[0][-1]) * 365
    days_left_after_warranty_ends = (MTBF/24) - warranty_in_days
    return (MTBF_in_months, MTBF_in_years, warranty_in_months, warranty_in_days, days_left_after_warranty_ends)



print("========== Starting Image Recognition =================")
MTBF_in_months, MTBF_in_years, warranty_in_months, warranty_in_days, days_left_after_warranty_ends = get_string(os.path.join(SRC_PATH + "/tdcm/task1/hc510.png"))
print(f" MTBF in months: {round(MTBF_in_months)}\n MTBF in years: {round(MTBF_in_years)}\n Warranty in months: {round(warranty_in_months)}\n Warranty in days: {round(warranty_in_days)}\n Number of days till MTBF after Warranty finishes: {round(days_left_after_warranty_ends)} ")
print("=========== Image Recognition Ended ==================")

