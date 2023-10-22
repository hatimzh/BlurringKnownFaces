# BlurringKnownFaces
Python program based on computer vision to bluring detected known faces.
# Usage
- Install opencv and face_recognition:
  
    ```terminal
    pip install opencv-python face_recognition
    ```
    or
    ```terminal 
    python -m pip install opencv-python face_recognition
    ```
- Running the program:
    - You can add a folder to (<a href="./known_faces">This folder</a>) with the name of the person who you want to detect his face to blurring it, this folder must contains at least two photos to detect the faces better.
      > **Note:** More photos get best detection.
    - There are two methodes to detect and blurring faces:
      - Detection from cam : <br>
        You can just run <a href="./face_detection.py">this program</a> using this command:
        ```terminal
        python face_detection.py
        ```
        > **Note:** If you want to run an externel cam you should modify <a href="./blob/main/face_detection.py#L27">this line</a>.<br>
      _Example : <a href="./tree/main/Example">Example of an external Cam.</a>_
      - Detection from given video :<br>
        You can do this by adding a video or a GIF file in <a href="./Test">this folder</a>.
        >**Note:** You should modify <a href="./blob/main/face_detection.py">this script </a> by commenting <a href="./blob/main/face_detection.py#L27">this line</a> and uncomment these lines : <a href="./blob/main/face_detection.py#L29">29</a> to <a href="./blob/main/face_detection.py#L29">34</a>, <a href="./blob/main/face_detection.py#L80">80</a> and <a href="./blob/main/face_detection.py#L90">90</a>.<br>
      _You can see the example in the Demo_
        
# Demo

https://github.com/hatimzh/BlurringKnownFaces/assets/96501113/91fd7583-e35f-45c4-b080-35af30ce2ada


> **Note:** As you see in the demo, it's so slow because I use only the CPU, so you can run it in a GPU to make it more fast. <br>
> You may need to install Cmake to run the code without errors.
