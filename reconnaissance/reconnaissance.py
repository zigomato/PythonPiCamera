#!/usr/bin/env python
# coding: utf-8

import picamera

import os, sys
import cv2
from time import sleep

camera = picamera.PiCamera()
camera.rotation = 180
camera.start_preview()
sleep(3)
for i in range(0,5) :
	camera.capture("base_photo/moi/moi_"+str(i)+".png")
camera.stop_preview()
