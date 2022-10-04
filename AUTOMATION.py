import cv2
import dropbox
import time
import random 

start_time=time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame= videoCaptureObject.read()
        image_name="img"+str(number)+"png"
        cv2.inwrite(image_name,frame)
        start_time=time.time
        result=False
    return image_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindow()
    
take_snapshot()

def  upload_file(image_name):
    access_token ="sl.BQgHewQcIiiAbA_jmkxYIX_kXV1-iNMT4P56HVnpX_yP3ix9scfirpQ1Omx3VPo4-kUW-TJ9PwjBEnZDMkktmAR1NxM2hnHFXdMdzdPRob4aVeIYAxbQuUp1p3KNMkY27Z-kPm0"
    file = image_name
    file_from = file
    file_to = "/newfolder"+(image_name)
    dbx = dropbox.Dropbox(access_token) 