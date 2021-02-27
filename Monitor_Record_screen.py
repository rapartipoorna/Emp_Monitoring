import cv2
import numpy as np
import os
import pyautogui ,schedule,time
from datetime import datetime
from multiprocessing import Process
import time
import schedule

# output = "video.avi"
output_1='Video-screen-shots'+'\\'+str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))+'.avi'
# print(output_1)
img = pyautogui.screenshot()
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#get info from img
height, width, channels = img.shape
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_1, fourcc, 20.0, (width, height))

def screen_video(): 
  timeout = time.time() + 30*1
  print(timeout)
  while(True):
    print(time.time())
    if time.time()>=timeout:
      break
    try:
      img = pyautogui.screenshot()
      image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
      out.write(image)
      StopIteration(0.5)
    except KeyboardInterrupt:
      break
    

  out.release()
  cv2.destroyAllWindows()

def schedule_Record_video():
    schedule.every(60).seconds.do(screen_video)
    # schedule.every().day.at("18:00").do(history)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    schedule_Record_video()