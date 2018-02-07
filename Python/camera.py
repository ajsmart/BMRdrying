import cv2
camera = cv2.VideoCapture(0)
for x in range(1,10):
    image = camera.read()[1]
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',gray)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('test.jpg',image)
        break
camera.release()
cv2.destroyAllWindows()