import pandas,cv2
from datetime import datetime 

def setup_dataframe():
    dataframe=pandas.DataFrame({'Start': pandas.to_datetime([]), 'End': pandas.to_datetime([])})
    return dataframe

def start_vid():
    video=cv2.VideoCapture(0)
    return video

def vid_readnblur(vid):
    check, frame=vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    return gray,frame

def compare_frames(frame1,frames):
    delta=cv2.absdiff(frame1,frames)
    threshold=cv2.threshold(delta,30,255,cv2.THRESH_BINARY)[1]
    threshold=cv2.dilate(threshold,None,iterations=2)
    return delta,threshold

def get_contour(threshold,frame):
    status=0
    (cnts,_)=cv2.findContours(threshold.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in cnts:
        if cv2.contourArea(cnt) < 5000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    return status

def statuslist(status,status_list,time_list):
    status_list.append(status)
    status_list=status_list[-2:]

    if status_list[-1]==1 and status_list[-2]==0 :
        time_list.append(datetime.now())
    elif status_list[-1]==0 and status_list[-2]==1:
        time_list.append(datetime.now())
    return

def uploadto_csv(time_list,dataframe):
    for i in range(0,len(time_list),2):
        new=pandas.DataFrame([{'Start':time_list[i],'End':time_list[i+1]}])
        dataframe=pandas.concat([new,dataframe],ignore_index=True)
    dataframe.to_csv('Times.csv',index=False,date_format='%d-%m-%Y %H:%M:%S')
    return

first_frame= None
status_list=[None,None]
time_list=[]
dataFrame=setup_dataframe()
video=start_vid()
while True:
    gray_frame,colorFrame=vid_readnblur(video)
    if first_frame is None:
        first_frame=gray_frame
        continue
    delta_frame,threshold_frame=compare_frames(first_frame,gray_frame)
    status=get_contour(threshold_frame,colorFrame)
    statuslist(status,status_list,time_list)

    cv2.imshow('Gray',gray_frame)
    cv2.imshow('Deltya',delta_frame)
    cv2.imshow('Threshold',threshold_frame)
    cv2.imshow('Color',colorFrame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        if status==1:
            time_list.append(datetime.now())
        break

uploadto_csv(time_list,dataFrame)
video.release()
cv2.destroyAllWindows()
