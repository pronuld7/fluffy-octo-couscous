import cv2

image_path = 'cat.jpeg'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)

cv2.imshow('Cat', image)
cv2.waitKey()