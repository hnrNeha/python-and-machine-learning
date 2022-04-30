# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:41:11 2022

@author: hnrne
"""
import requests
from flask import*
from fastapi import FastAPI
from fastapi.responses import FileResponse 
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np




# to open the image
image = Image.open(r"C:\Users\hnrne\Downloads\nature.jpg")
# this open the photo viewer
x=image.width
y=image.height
# image watermark

crop_image = Image.open(r"C:\Users\hnrne\Downloads\logo.jpg")
# to keep the aspect ration in intact
size = (crop_image.width/2,crop_image.height/2)
crop_image.thumbnail(size)

# add watermark
copied_image = image.copy()

# base image
def topleft():
    copied_image.paste(crop_image, (0, 0))


def topright():
    copied_image.paste(crop_image, (x-crop_image.width, 0))
    
def center():
    copied_image.paste(crop_image, (int(x/2),int(y/2)))
                       
def bottomleft():
    copied_image.paste(crop_image, (0, y-crop_image.height))
   
   
 
def bottomright():
    copied_image.paste(crop_image, (int(3*x/4),int(3*y/4)))
  
  

def operations():
   
    op=int(input("Choose one of the following option: 1.top left,2.top right ,3.center,4.bottom left,5.bottom right"))
    if(op==1):
        topleft()
        
    elif(op==2):
        topright()
        
    elif(op==3):
        center()
        
    elif(op==4):
        bottomleft()
        
    else:
        bottomright()

app = Flask(__name__)
@app.route('/',methods=["GET"])
def index():      
    operations()
    return copied_image.show()
    

    
    
if __name__=="__main__":
    app.run()
   

# pasted the crop image onto the base image
