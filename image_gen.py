import cv2
import os
import time
import uuid # For generating unique filenames

IMAGES_PATH = "Tensorflow/workspace/images/collectedimages"
labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15
os.makedirs(IMAGES_PATH)

for label in labels:
    os.makedirs(os.path.join(IMAGES_PATH, label))
    cap = cv2.VideoCapture(0)
    print(f"Collecting images for {label}...")
    time.sleep(5)  
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        image_name = os.path.join(IMAGES_PATH, label, label+'.'+f'{str(uuid.uuid1())}.jpg')
        cv2.imwrite(image_name, frame)
        cv2.imshow("Frame", frame)
        time.sleep(2)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
    cap.release()
