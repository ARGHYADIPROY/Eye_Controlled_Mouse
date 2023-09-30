import cv2
import mediapipe as mp
import pyautogui
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w ,_ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id,landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w) #give pixels
            y = int(landmark.y * frame_h) #give pixels
            cv2.circle(frame,(x,y), 3, (0,255,0))
            if id==1:
                screen_x = screen_w/frame_w *x
                screen_y = screen_h/frame_h *y
                pyautogui.moveTo(screen_x,screen_y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w) #give pixels
            y = int(landmark.y * frame_h) #give pixels
            cv2.circle(frame,(x,y), 3, (0,255,255))
        print(left[0].y - left[1].y)
        if(left[0].y - left[1].y) <0.02:#this value adjust on your own, changes by distance between camera and u
            print('click')
            pyautogui.click()
            # pyautogui.sleep(1)
        right = [landmarks[380], landmarks[385]]
        for landmark in right:
            x = int(landmark.x * frame_w)  # Convert landmark coordinates to pixels
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))  # Draw circles on the frame
        # Check if the vertical distance between the landmarks is less than 0.004
        if (right[0].y - right[1].y) < 0.019:#this value adjust on your own, changes by distance between camera and u
            print('clicku')
            pyautogui.rightClick()  # Trigger a mouse click event
        # #     pyautogui.sleep(1)
    cv2.imshow('Eye Tracking', frame)
    cv2.waitKey(1)