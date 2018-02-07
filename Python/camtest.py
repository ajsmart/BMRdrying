import datetime, cv2, time, os
current_time = datetime.datetime.now()
endtime = current_time + datetime.timedelta(seconds = 30)
print(current_time,endtime)
cap = cv2.VideoCapture(0)
while datetime.datetime.now() < endtime:    
    img = cap.read()[1]
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('image\img_{}.png'.format(int(time.time())), gray)
    time.sleep(1)

#make into video
image_folder = 'image'
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, -1, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()