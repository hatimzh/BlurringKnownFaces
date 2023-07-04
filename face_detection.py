import face_recognition as fr 
import cv2 
import os 


faces_dir = "known_faces" #faces directory name

# Function to get faces names, as well as face encodings
def get_face_encodings():
    face_names = os.listdir(faces_dir)
    face_encodings = []

    for i, name in enumerate(face_names):
        image_file=os.listdir(faces_dir+"/"+name)
        for photo in image_file:
            face = fr.load_image_file(f"{faces_dir}\\{name}\\{photo}")
            face_encodings.append(fr.face_encodings(face)[0])

        face_names[i] = name
    
    return face_encodings,face_names

# Retrieving face encodings and storing them in the face_encodings variable, along with the names
face_encodings, face_names = get_face_encodings()

print("waiting a few seconds...")
video = cv2.VideoCapture(0) #open the cam, you can change the 0 to 1 if you have an external webcam

#video = cv2.VideoCapture("./Test/your_test_GIF_or_Video")
#output = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'XVID')
#, int(video.get(cv2.CAP_PROP_FPS))
#, (int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
#, int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#)

print("Cam opened succefully\n press Q to exit.")

# Setting variable which will be used to scale size of image
scl = 2

while True:
    x, image = video.read()

    if x :
    
        # Making current frame smaller so program runs faster
        resized_image = cv2.resize(image, (int(image.shape[1]/scl), int(image.shape[0]/scl)))
    
        # Converting current frame to RGB, since that's what the face recognition module uses
        rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
    
        # Retrieving face location coordinates and unknown encodings
        face_locations = fr.face_locations(rgb_image)
        unknown_encodings = fr.face_encodings(rgb_image, face_locations)
    
        # Iterating through each encoding, as well as the face's location
        for face_encoding, face_location in zip(unknown_encodings, face_locations):
            # Comparing known faces with unknown faces
            result = fr.compare_faces(face_encodings, face_encoding, 0.5)#you can change this third parameter to get best results
    
            # Getting correct name if a match was found
            if True in result:
                name = face_names[result.index(True)]
    
                # Setting coordinates for face location
                top, right, bottom, left = face_location
    
                # Drawing rectangle around face
                imgface = cv2.rectangle(image, (left*scl, top*scl), (right*scl, bottom*scl), (255, 255, 255), 2)
                # Bluring detected faces
                imgface[top*scl:bottom*scl,left*scl:right*scl]=cv2.medianBlur(imgface[top*scl:bottom*scl,left*scl:right*scl],35)
                # Setting font, as well as displaying text of name
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(image, name, (left*scl, bottom*scl + 20), font, 0.8, (255, 255, 255), 1)
        
    
        
        cv2.imshow("Blurring detected faces", image)
        
        #output.write(image)
    
        # Waiting until the Q key pressed
        key=cv2.waitKey(1)
        if key==ord('q'):
            break
    else :
        break
    
video.release()
#output.release()
cv2.destroyAllWindows()
