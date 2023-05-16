import cv2,time # CV (open CV) - Image Detection Task

from datetime import datetime # to get the exact time at which face is present
import argparse # to combine all the the images and create a video of the action
import os # for file handling

# face Cascade - For the Identification of human face (Haar Casacade Classifier)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Video Capturing - input from webcam
# video = cv2.VideoCapture(0) # 0 for webcam
frame = cv2.imread("screenshots\\2023-Apr-27_09-06-27\\face detected_2023-Apr-27_09-06-58-525610.jpg")
# making new directories
# currentTime = datetime.now().strftime('%Y-%b-%d_%H-%M-%S')
# os.mkdir('screenshots/' + currentTime)

face_detect = False

# Alert Function
def alert():
    print("Alert: Someone is at your home")
    # -> we can send the text message to the owner of the house.
    # -> Also we can send the image of the person

while True:
    # check,frame=video.read() # actual data is present in Frame (Screenshots)
    
    if frame is not None:
        # convert image into grey scale (Blue Green Red to Gray)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detecting faces in the Grey Image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10) 
        
        ## Green Rectangle
        for x, y, w, h in faces: # x, y, width, height  
            # Making a Green Rectangle around the face
            img = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3) 
            # exact_time = datetime.now().strftime('%Y-%b-%d_%H-%M-%S-%f')
            # cv2.imwrite("screenshots/" + currentTime + "/face detected_" + str(exact_time) + ".jpg", img) # saving the images
            cv2.imshow("detected faces",img) # saving the images
            key = cv2.waitKey(1)
            

        ## For Alert Message
        if face_detect is False:
            if len(faces) > 0:
                alert()
                
                
        if len(faces) > 0:
            face_detect = True
        else:
            face_detect = False
        
        
        # cv2.imshow("home survelence", frame) # to show the video (Conti.Images - Frames)
        # key = cv2.waitKey(1)

        # if key == ord('q'):
        #     ap = argparse.ArgumentParser()
        #     ap.add_argument("-ext","--extension", required=False, default='jpg')
        #     ap.add_argument("-o","--output", required=False, default='Recordings/output_' + currentTime + '.mp4')
        #     args=vars(ap.parse_args())

            
        #     dir_path = 'screenshots/' + currentTime + '/'
        #     ext = args['extension']
        #     output = args['output']


        #     images = []

        #     for f in os.listdir(dir_path):
        #         if f.endswith(ext):
        #             images.append(f)



        #     image_path = os.path.join(dir_path, images[0])
        #     frame = cv2.imread(image_path)
        #     height, width, channels = frame.shape


        #     forcc = cv2.VideoWriter_fourcc(*'mp4v')
        #     out = cv2.VideoWriter(output, forcc, 5.0, (width, height))


        #     for image in images:
        #         image_path = os.path.join(dir_path, image)
        #         frame = cv2.imread(image_path)
        #         out.write(frame)

        
        p =input()

        break


# video.release()
# cv2.destroyAllWindows