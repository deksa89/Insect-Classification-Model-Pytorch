import cv2

vidcap = cv2.VideoCapture('C:/Users/User/Desktop/Projekt/slike_video/videos/Blauschwarze Holzbiene - Xylocopa violacea.mp4')
count = 0
success = True
fps = int(vidcap.get(cv2.CAP_PROP_FPS))
print(fps)


while success:
    success, image = vidcap.read()
    print('read a new frame:', success)
    if count % (0.125 * fps) == 1:
        cv2.imwrite('frame%d.jpg' % count, image)
        print('successfully written 10th frame')
    count += 1
print("Done!!!")
