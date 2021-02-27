import cv2
import numpy as np
import os
import pyautogui ,schedule,time
from datetime import datetime
from multiprocessing import Process

# output = "video.avi"
output_1=str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))+'.avi'
# print(output_1)
img = pyautogui.screenshot()
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#get info from img
height, width, channels = img.shape
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_1, fourcc, 20.0, (width, height))

def screen_video(): 
  while(True):
    try:
      img = pyautogui.screenshot()
      image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
      out.write(image)
      StopIteration(0.5)
    except KeyboardInterrupt:
      break

  out.release()
  cv2.destroyAllWindows()
# screen_video()  

def screen_shots():
  i=0
  while True:
    now = datetime.now().replace(second=0) 
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    print(datetime.strptime('21:38','%H:%M').time())
    img = pyautogui.screenshot()
    img.save(str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))+'.jpeg')
    time.sleep(10)
    i+=1
    if current_time==str(datetime.strptime('21:38','%H:%M').time()):
      break 
    # time.sleep(600)
    time.sleep(10)
screen_shots() 
if __name__ == '__main__':

    proc1 = Process(target=screen_video)
    proc1.start()

    proc2 = Process(target=screen_shots)
    proc2.start()
