from keras.applications.mobilenet_v2 import preprocess_input
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from imutils.video import VideoStream

import numpy
import argparse
import imutils
import time
import cv2
import os
